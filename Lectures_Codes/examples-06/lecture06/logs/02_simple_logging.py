#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# Now we modify the configuration

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

logging.warning('I warn you')
logging.info('Just an info for you')  # Now it will be printed

