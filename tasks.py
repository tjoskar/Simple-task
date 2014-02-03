import os
import logging
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from wsgiref.simple_server import make_server
import sqlite3

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

##
## Views
##
@view_config(route_name='list', renderer='list.mako')
def list_view(request):
    req = request.db.execute("select id, name from tasks where closed = 0")
    tasks = [dict(id=row[0], name=row[1]) for row in req.fetchall()]
    return {'tasks': tasks}

@view_config(route_name='new', renderer='new.mako')
def new_view(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            request.db.execute(
                'insert into tasks (name, closed) values (?, ?)',
                [request.POST['name'], 0])
            request.db.commit()
            request.session.flash('New task was successfully added!')
            return HTTPFound(location=request.route_url('list'))
        else:
            request.session.flash('Please enter a name for the task!')
    return {}

@view_config(route_name='close')
def close_view(request):
    task_id = int(request.matchdict['id'])
    request.db.execute("update tasks set closed = ? where id = ?",
                       (1, task_id))
    request.db.commit()
    request.session.flash('Task was successfully closed!')
    return HTTPFound(location=request.route_url('list'))

##
## Special views
##

@view_config(context='pyramid.exceptions.NotFound', renderer='notfound.mako')
def notfound_view(request):
    request.response.status = '404 Not Found'
    return {}

##
## Subscribers
##
@subscriber(ApplicationCreated)
def application_created_subscriber(event):
    log.warn('Initializing database...')
    with open(os.path.join(here, 'schema.sql')) as f:
        stmt = f.read()
        settings = event.app.registry.settings
        db = sqlite3.connect(settings['db'])
        db.executescript(stmt)

@subscriber(NewRequest)
def new_request_subscriber(event):
    request = event.request
    settings = request.registry.settings
    request.db = sqlite3.connect(settings['db'])
    request.add_finished_callback(close_db_connection)

##
## Help functions
##
def close_db_connection(request):
    request.db.close()


if __name__ == '__main__':
    # configuration settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['db'] = os.path.join(here, 'tasks.db')
    settings['mako.directories'] = os.path.join(here, 'templates')
    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    # configuration setup
    config = Configurator(settings=settings, session_factory=session_factory)
    # routes setup
    config.add_route('list', '/')
    config.add_route('new', '/new')
    config.add_route('close', '/close/{id}')
    config.add_static_view('static', os.path.join(here, 'static'))
    config.scan()
    # add mako templating
    config.include('pyramid_mako')
    # serve app
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    print '0.0.0.0:8080'
    server.serve_forever()

