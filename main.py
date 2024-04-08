from fastapi import FastAPI
import time
from threading import Thread

app = FastAPI()

# Variable to keep track of the task status
task_status = "ready"

def dummy_task():
    global task_status
    task_status = "running"
    # Simulating a long-running task
    time.sleep(5)
    task_status = "ready"

@app.get("/run")
def run_task():
    global task_status
    if task_status == "ready":
        # Start the dummy task in a background thread
        thread = Thread(target=dummy_task)
        thread.start()
        return {"message": "Task started"}
    else:
        return {"message": "A task is already running"}

@app.get("/status")
def get_status():
    return {"status": task_status}
