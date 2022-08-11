import time

from .celery import app


@app.task(
    track_started=True,
    acks_late=True,
    reject_on_worker_lost=True,
    acks_on_failure_or_timeout=False,
)
def example():
    print("Start my task")
    time.sleep(999999)
    print("End my task")
