#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from base_selenium_test_class import BaseSeleniumTestClass
import nose

class TestSuite(BaseSeleniumTestClass):
    """docstring for TestSuite"""

    def __init__(self):
        self.driver = None
        self.connect_to_database = False
        super(TestSuite, self).__init__()

    def test_that_index_page_is_working(self):
        """ Test that index page is working """
        I = self.driver
        I.take_screenshot_on_failure = True

        I.get("http://jenkins/simple_task")

        I.see('Hej')
        I.do_not_see('Something else')

        assert I.am_on == 'http://jenkins/simple_task/'


    def test_wikipedia(self):
        I = self.driver
        I.get("http://en.wikipedia.org/wiki/Randomness")

        I.see('Randomness')

        I.find_by_css(".mbox-image")
        I.dump_elm()

        I.find_by_css("img", False)
        I.dump_elm()

if __name__ == '__main__':
    nose.main()
