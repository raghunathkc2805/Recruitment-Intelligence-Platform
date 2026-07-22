from __future__ import annotations

from threading import Thread

from .task import BackgroundTask
from .task_queue import task_queue
from .monitor import background_monitor


class BackgroundTaskManager:

    def __init__(self):

        self.worker = Thread(
            target=self._worker,
            daemon=True,
        )

        self.worker.start()

    def submit(
        self,
        name,
        function,
        *args,
        **kwargs,
    ):

        task = BackgroundTask(
            name=name,
            function=function,
            args=args,
            kwargs=kwargs,
        )

        task_queue.put(task)

        return task

    def _worker(self):

        while True:

            task = task_queue.get()

            background_monitor.job_started(task)
            task.status = "RUNNING"

            try:

                task.result = task.function(
                    *task.args,
                    **task.kwargs,
                )

                task.status = "SUCCESS"
                background_monitor.job_completed(task)

            except Exception as ex:

                task.error = str(ex)

                task.status = "FAILED"
                background_monitor.job_failed(task)

            finally:

                task_queue.task_done()


background_manager = BackgroundTaskManager()

