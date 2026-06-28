import time

def time_sleep(seconds):
    time.sleep(seconds)
    return None

def time_sleep_ms(ms):
    time.sleep(ms / 1000.0)
    return None

def time_stamp():
    return int(time.time())

# Registered
LIB_FUNCS["time.freeze.seconds"] = time_sleep    # Sleep in second
LIB_FUNCS["time.freeze.millis"] = time_sleep_ms  # Sleep in millisecond
LIB_FUNCS["time.get.unix.now"] = time_stamp      #  Using timestamp
