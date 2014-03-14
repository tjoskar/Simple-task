#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import ConfigParser
import os
import pymysql
from seleniumdriverwrapper import Driver

__subdomain__ = 'hermod'
__application__ = 'vbanken'
__confing_filename__ = 'test_utvecklingsversion.ini'


class BaseSeleniumTestClass(object):
    """ Base Test Class """

    driver = None
    connect_to_database = True
    db = None
    db_cursor = None
    __selenium_config = {}

    def __init__(self):
        parser = ConfigParser.SafeConfigParser()

        if __subdomain__ is not None:
            config_file_path = '/etc/{0}/{1}/{2}'.format(__application__, __subdomain__, __confing_filename__)
        else:
            config_file_path = '/etc/{0}/{1}'.format(__application__, __confing_filename__)

        if not os.path.isfile(config_file_path):
            raise IOError('ini-file {0} missing!'.format(config_file_path))

        parser.read(config_file_path)

        self.__selenium_config = dict(parser.items('Selenium'))

        if self.connect_to_database:
            self.db = pymysql.connect(parser.items('Database'))
            self.db_cursor = self.db.cursor()

    def setup(self):
        self.driver = Driver(**dict((k, float(self.__selenium_config[k])) for k in ['timeout', 'poll', 'delay']))
        try:
            self.driver.connect_remote(**dict((k, self.__selenium_config[k]) for k in ['driver_name', 'command_executor']))
        except KeyError:
            self.driver.connect_local(driver_name=self.__selenium_config['driver_name'])

    def teardown(self):
        self.driver.die()



# __config__ = {
#     'command_executor': 'http://selenium:4444/wd/hub',
#     'driver_name': 'firefox',
#     'timeout': 5,
#     'poll': 0.5,
#     'delay': 1,
#     'db': {
#         'host': 'localhost',
#         'user': 'root',
#         'passwd': 'root',
#         'db': 'local'
#     },

#     'local': {
#         'driver_name': 'firefox',
#         'timeout': 5,
#         'poll': 0.5,
#         'delay': 1,
#         'db': {
#             'host': 'localhost',
#             'user': 'root',
#             'passwd': 'root',
#             'db': 'local'
#         }
#     }
# }
# self.I = Driver(**dict((k, __config__[k]) for k in ['timeout', 'poll', 'delay']))
# self.I.connect_remote(**dict((k, __config__[k]) for k in ['driver_name', 'command_executor']))
