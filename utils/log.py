#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:44:25 2023

@author: zby
"""

import logging


logging.basicConfig(format='%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s'
                    , level=logging.DEBUG)



class Log:

    def __init__(self, name, filename=None):
        self._logger = logging.getLogger(name)
        
        if filename is not None:
            if len(self._logger.handlers) != 0:
                for hdlr in self._logger.handlers:
                    self._logger.removeHandler(hdlr)
            fmt = logging.Formatter('%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s')
            hdlr = logging.FileHandler(filename, mode='a', encoding='utf-8')
            hdlr.setFormatter(fmt)
            self._logger.addHandler(hdlr)

    def info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

