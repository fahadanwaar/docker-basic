from celery import Celery
import os

app = Celery("tasks", broker=os.getenv("REDIS_URL"))


@app.task
def example_task(param):
    print(f"Executing task with param: {param}")
