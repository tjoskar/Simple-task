#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import sqlite3

class ToDoTest(unittest.TestCase):

    browser = None
    db = None
    task_name = 'Test'

    def restore_database(self):
	print 'restore database'
	self.db.execute(
	    'DELETE FROM tasks WHERE name=?',
	    [self.task_name]
	)
	self.db.commit()

    def setUp(self):
	here = os.path.dirname(os.path.abspath(__file__))
	db_path = os.path.join(here, 'env/tasks/tasks.db')
	self.db = sqlite3.connect(db_path)
	self.restore_database()
	self.browser = webdriver.Remote(
	    command_executor='http://awesome.dev:4444/wd/hub',
	    desired_capabilities=DesiredCapabilities.FIREFOX
	)

    def test_add_new_item(self):
	self.browser.get("http://awesome.dev:8080/")
	self.assertIn("Simple TODO List", self.browser.title)

	add_new_link = self.browser.find_element_by_link_text("Add a new task")
	add_new_link.click()

	name_input = self.browser.find_element_by_name('name')
	name_input.send_keys(self.task_name)
	button = self.browser.find_element_by_class_name('button')
	button.click()

	new_task = self.browser.find_element_by_xpath("(.//ul/li/span[@class='name'])[last()]")

	# time.sleep(2);
	self.browser.get_screenshot_as_file('/Users/oskar/vagrant/awesome/data/todo.png')

    def tearDown(self):
	self.browser.close()
	self.restore_database()

if __name__ == "__main__":
    unittest.main()
