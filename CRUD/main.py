from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Write report", "done": False},
    {"id": 3, "title": "Walk the dog", "done": True},
]

@app.get("/")
def root():
    return {"name": "Task API", "version": "1.0.0" ,"endpoints": ["/tasks"]}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}



@app.post("/tasks", status_code=201)
def create_task(task: dict):
    new_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {"id": new_id, "title": task["title"], "done": False}
    tasks.append(new_task)
    return new_task
