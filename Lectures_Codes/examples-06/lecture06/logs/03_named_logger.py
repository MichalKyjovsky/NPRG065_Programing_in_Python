#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# We can use many loggers in a single program
logger = logging.getLogger('named_logger')

logger.warning('I warn you')
logger.info('Just an info for you')


# A good practice is to use a module-named logger

print(f'Module name is {__name__}')

# But in this case it is not ideal as the name is __main__

mlogger = logging.getLogger(__name__)
print(f'Logger name is {mlogger.name}')
