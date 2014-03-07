#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Testfall för att se om texten hej kan se på startsidan
"""

from driverwrapper import DriverWrapper
import nose

def test_that_index_page_is_working():
    """ Test that index page is working """
    I = DriverWrapper(timeout=5, poll=0.5, delay=1)

    I.connect_local('phantomjs')
    # I.connect_remote('firefox', 'http://yalla.dev:4444/wd/hub')

    I.take_screenshot_on_failure = True

    I.get("http://localhost/simple_task")

    I.see('Hej')
    I.do_not_see('07:00–16:00')

    assert I.am_on == 'http://localhost/simple_task/'

    I.close()

if __name__ == '__main__':
    nose.main()
