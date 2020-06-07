#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import yaml
import logging.config


# Below is universally usable function for setting up the logging configuration
# It tries to load config from the yaml file referenced in the environment variable or from a file with
# the default name or fall back to a default.

def setup_logging(default_path='logging.yaml', default_level=logging.WARN, env_key='LOG_CFG') -> None:
    """Setup logging configuration.

    :param default_path:
    :param default_level:
    :param env_key:
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


setup_logging()

clogger = logging.getLogger('complex_logger')
alogger = logging.getLogger('another_logger')

clogger.warning('I warn you')
alogger.warning('I warn you')
clogger.info('Just an info for you')
alogger.info('Just an info for you')
