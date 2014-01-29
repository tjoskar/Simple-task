#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import time
import os
import sqlite3


class ToDoTest(unittest.TestCase):
    """
    A simple unit-test for a simple task python app.
    """

    __browser = None
    __db = None
    __task_name = 'Test'

    def _restore_database(self):
        """ Restore the database """
        self.__db.execute(
            'DELETE FROM tasks WHERE name=?',
            [self.__task_name]
        )
        self.__db.commit()

    def setUp(self):
        here = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(here, 'tasks.db')
        self.__db = sqlite3.connect(db_path)
        self._restore_database()
        self.__browser = webdriver.Remote(
            command_executor='http://yalla.dev:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )

    def test_add_new_item(self):
        """Test to see if we can add a new item"""
        browser = self.__browser
        self.__browser.get("http://yalla.dev:8080/")
        self.assertIn("Simple TODO List", browser.title)

        add_new_link = browser.find_element_by_link_text("Add a new task")
        add_new_link.click()

        name_input = self.__browser.find_element_by_name('name')
        name_input.send_keys(self.__task_name)
        button = browser.find_element_by_class_name('button')
        button.click()

        browser.find_element_by_xpath("(.//ul/li/span[@class='name'])[last()]")

        # time.sleep(2);
        if not browser.get_screenshot_as_file('/Users/oskar/vagrant/yalla/data/todo.png'):
            print 'Unable to save screenshot'

    def tearDown(self):
        self.__browser.close()
        self._restore_database()

if __name__ == "__main__":
    unittest.main()
