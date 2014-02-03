"""
Testing like a boss
"""

import unittest
from pyramid import testing
import tasks
from mock import Mock

class ViewTests(unittest.TestCase):
    """ Test that all views is working as expected """

    def setUp(self):
        self.config = testing.setUp()
        self.config.add_route('list', '/list')
        self.config.add_route('new', '/new')
        self.config.add_route('close', '/close/{id}')
        self._db_tasks = [
            {0: 1, 1: 'Name 1'},
            {0: 2, 1: 'Name 2'}
        ]

    def tearDown(self):
        testing.tearDown()

    def test_list_view(self):
        """ Test list view """
        request = testing.DummyRequest()

        db_mock = Mock()
        db_result_mock = Mock()
        db_result_mock.fetchall.return_value = self._db_tasks
        db_mock.execute.return_value = db_result_mock

        request.db = db_mock

        result = tasks.list_view(request)
        taskts = [dict(id=row[0], name=row[1]) for row in self._db_tasks]
        assert all([True for value in result.get('tasks') if value in taskts])

        return True

    def test_get_new_view(self):
        """ GET req. new view """
        request = testing.DummyRequest()

        request.method = 'GET'
        result = tasks.new_view(request)

        self.assertEqual(result, {})

    def test_post_new_view(self):
        """ POST req. new view """

        request = testing.DummyRequest()
        request.method = 'POST'
        request.POST = {'name': ''}

        session_mock = Mock()
        session_mock.flash.return_value = None
        request.session = session_mock

        result = tasks.new_view(request)
        session_mock.flash.assert_called_once_with(
            'Please enter a name for the task!'
        )
        self.assertEqual(result, {})

        request.POST['name'] = 'New name'
        db_mock = Mock()
        db_mock.commit.return_value = None
        db_mock.execute.return_value = None
        request.db = db_mock

        session_mock = Mock()
        session_mock.flash.return_value = None
        request.session = session_mock

        tasks.new_view(request)

        request.db.execute.assert_called_once_with(
            'insert into tasks (name, closed) values (?, ?)',
            [request.POST['name'], 0]
        )
        request.db.commit.assert_called_once_with()
        request.session.flash.assert_called_once_with(
            'New task was successfully added!'
        )

        return True

    def test_close_view(self):
        """ New view test """
        request = testing.DummyRequest()
        request.matchdict = {'id': '1'}

        db_mock = Mock()
        db_mock.commit.return_value = None
        db_mock.execute.return_value = None
        request.db = db_mock

        session_mock = Mock()
        session_mock.flash.return_value = None
        request.session = session_mock

        tasks.close_view(request)

        request.db.execute.assert_called_once_with(
            'update tasks set closed = ? where id = ?',
            (1, 1)
        )
        request.db.commit.assert_called_once_with()
        request.session.flash.assert_called_once_with(
            'Task was successfully closed!'
        )

    def test_notfound_view(self):
        """ Test 404 view """
        request = testing.DummyRequest()

        request.response.status = '200 OK'

        result = tasks.notfound_view(request)

        self.assertEqual(
            request.response.status,
            '404 Not Found'
        )
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()
