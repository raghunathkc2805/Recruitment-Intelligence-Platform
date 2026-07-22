import uuid

from .trace_context import trace_id

def start_trace():

    tid=str(uuid.uuid4())

    trace_id.set(tid)

    return tid
