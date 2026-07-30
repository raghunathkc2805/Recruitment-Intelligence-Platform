import os
import threading
import psutil

class RuntimeDiagnostics:

    def collect(self):

        process = psutil.Process(os.getpid())

        return {

            "cpu_percent":process.cpu_percent(),

            "memory_percent":process.memory_percent(),

            "rss_mb":round(process.memory_info().rss/1024/1024,2),

            "threads":threading.active_count(),

            "handles":len(process.open_files()),

            "status":"HEALTHY"

        }

runtime_diagnostics = RuntimeDiagnostics()
