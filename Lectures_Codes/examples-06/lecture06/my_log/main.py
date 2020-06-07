"""
Assignment: Develop a module for logging. It should be used as given below. It defines three functions:
- set_log_fn - allows the client to provide custom output function for log entries. The parameters to the function are the
    log message and a set of custom parameters that can be passed via function log
- set_severity - sets the logging threshold. Possible values are DEBUG, INFO, ERROR
- log - logs an entry if its severity is equal or higher than the severity set via set_severity. Parameters are: format and
    a variable number of positional argument for the format (the syntax of the format is the same as for str.format), severity and
    variable number of key-value pairs that are passed to the log output function
"""

import mlog
from mlog import log

def custom_log_fn(msg, **kwargs):
    print(f'{kwargs["client_ip"]}: {msg}')

    with open('main.log', 'a') as log_file:
        print(f'{kwargs["client_ip"]}: {msg}', file=log_file)

mlog.set_log_fn(custom_log_fn)
mlog.set_severity(mlog.DEBUG)

log('Page {} not found', '/home/test', severity=mlog.ERROR, client_ip='15.20.25.30')
