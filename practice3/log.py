import logging


def f():
    try:
        1 / 0
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        return template.format(type(ex).__name__, ex.args)


def run_with_log(func):
    log = logging.getLogger()
    log.exception(func())


run_with_log(f)
