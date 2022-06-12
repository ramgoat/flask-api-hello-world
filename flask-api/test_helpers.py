from init_logger import flogger, logger

def randomFunction(val):
    import inspect
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__

    log_message = {
        "function_name": "randomFunction",
        "message": val,
        "filename": module.__file__
    }

    if not flogger.emit('follow', log_message):
        logger.error(flogger.last_error)
        flogger.clear_last_error() # clear stored error after handled errors