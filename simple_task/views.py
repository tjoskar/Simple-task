import logging
import os
import PyMySQL

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.events import NewRequest
from pyramid.events import ApplicationCreated
from pyramid.events import subscriber

logging.basicConfig()
log = logging.getLogger(__file__)
here = os.path.dirname(os.path.abspath(__file__))

##
## Views
##
@view_config(route_name='list', renderer='list.mako')
def list_view(request):
    request.db_cursor.execute("select id, name from tasks where closed = 0")
    tasks = [dict(id=row[0], name=row[1]) for row in request.db_cursor.fetchall()]
    return {'tasks': tasks}

@view_config(route_name='new', renderer='new.mako')
def new_view(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            request.db_cursor.execute("insert into tasks (name, closed) values (%s, %s)", (request.POST['name'], '0'))
            request.db.commit()
            request.session.flash('New task was successfully added!')
            return HTTPFound(location=request.route_url('list'))
        else:
            request.session.flash('Please enter a name for the task!')
    return {}

@view_config(route_name='close')
def close_view(request):
    task_id = int(request.matchdict['id'])
    request.db_cursor.execute("update tasks set closed = %s where id = %s", (1, task_id))
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
@subscriber(NewRequest)
def new_request_subscriber(event):
    request = event.request
    settings = request.registry.settings
    settings['db'] = PyMySQL.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 db="local")
    request.db = settings['db']
    request.db_cursor = request.db.cursor()
    request.add_finished_callback(close_db_connection)

##
## Help functions
##
def close_db_connection(request):
    request.db.close()
