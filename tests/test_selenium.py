#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Selenium Test
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import PyMySQL


class ToDoTest(unittest.TestCase):
    """
    A simple unit-test for a simple task python app.
    """

    _browser = None
    _db = None
    _task_name = 'Test'

    def _restore_database(self):
        """ Restore the database """
        self._db_cursor.execute(
            'DELETE FROM tasks WHERE name=%s',
            (self._task_name, )
        )
        self._db.commit()

    def setUp(self):
        self._db = PyMySQL.connect(host="localhost",
                                   user="root",
                                   passwd="root",
                                   db="local")
        self._db_cursor = self._db.cursor()

        self._restore_database()
        self._browser = webdriver.Remote(
            command_executor='http://yalla.dev:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )

    def test_add_new_item(self):
        """Test to see if we can add a new item"""
        browser = self._browser
        self._browser.get("http://yalla.dev/simple_task/")
        self.assertIn("Simple TODO List", browser.title)

        add_new_link = browser.find_element_by_link_text("Add a new task")
        add_new_link.click()

        name_input = self._browser.find_element_by_name('name')
        name_input.send_keys(self._task_name)
        button = browser.find_element_by_class_name('button')
        button.click()

        browser.find_element_by_xpath("(.//ul/li/span[@class='name'])[last()]")

    def tearDown(self):
        self._browser.close()
        self._restore_database()

if __name__ == "__main__":
    unittest.main()
