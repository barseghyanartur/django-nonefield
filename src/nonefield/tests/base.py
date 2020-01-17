from __future__ import print_function

import logging

__title__ = 'nonefield.tests.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'LOG_INFO',
    'log_info',
    'OPTIONAL_SKIP',
    'optional_skip',
)


LOGGER = logging.getLogger(__name__)
LOG_INFO = True
TRACK_TIME = False


def log_info(func):
    """Logs some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):

        result = func(self, *args, **kwargs)

        LOGGER.debug('\n{0}'.format(func.__name__))
        LOGGER.debug('============================')
        if func.__doc__:
            LOGGER.debug('""" {0} """'.format(func.__doc__.strip()))
        LOGGER.debug('----------------------------')
        if result is not None:
            LOGGER.debug(result)
        LOGGER.debug('\n')

        return result
    return inner

OPTIONAL_SKIP = False


def optional_skip(func):
    """Simply skips the test."""
    def inner(self, *args, **kwargs):
        if OPTIONAL_SKIP:
            return
        return func(self, *args, **kwargs)
    return inner
