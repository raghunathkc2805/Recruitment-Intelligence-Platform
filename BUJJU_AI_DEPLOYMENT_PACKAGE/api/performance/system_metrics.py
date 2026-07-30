import os
import psutil


def system_metrics():

    process = psutil.Process(os.getpid())

    return {

        "cpu_percent": psutil.cpu_percent(),

        "memory_percent": process.memory_percent(),

        "rss_mb": round(
            process.memory_info().rss/1024/1024,
            2,
        ),

        "threads": process.num_threads(),

        "open_files": len(process.open_files()),

    }
