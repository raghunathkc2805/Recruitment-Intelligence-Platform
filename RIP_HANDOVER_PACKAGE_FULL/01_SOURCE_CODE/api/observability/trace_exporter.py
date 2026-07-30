import json
from pathlib import Path

TRACE_FILE = Path("logs/traces.jsonl")
TRACE_FILE.parent.mkdir(parents=True,exist_ok=True)

def export(span,trace):

    with TRACE_FILE.open("a",encoding="utf8") as f:

        f.write(json.dumps({

            "trace_id":trace,

            "span_id":span.span_id,

            "name":span.name,

            "duration_ms":span.duration_ms

        })+"\n")
