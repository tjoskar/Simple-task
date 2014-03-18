#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Testfall för att se om true är true
"""

import nose

def test_that_index_page_is_working():
    """ Test to see if True is equal True """
    assert True == True

def test_that_true_is_true():
    """ Test to see if True is equal True """
    assert True == True

if __name__ == '__main__':
    nose.main()
