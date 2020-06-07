def _mlog_default_log(msg, **kwargs):
    print(msg)

DEBUG = 0
INFO = 1
ERROR = 2

_log_fn = _mlog_default_log
_log_severity = INFO

def set_log_fn(logfn):
    global _log_fn
    _log_fn = logfn

def set_severity(severity):
    global _log_severity
    _log_severity = severity

def log(fmt, *args, severity, **kwargs):
    if severity >= _log_severity:
        msg = fmt.format(*args)
        _log_fn(msg, **kwargs)