import threading

def thread_status():

    return {

        "active_threads":threading.active_count()

    }
