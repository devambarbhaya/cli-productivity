from plyer import notification
from database import SessionLocal, Task
import datetime
import time

def send_notification(task):
    # Send a desktop notification for a task
    notification.notify(
        title=f"Task Reminder: {task.title}",
        message=f"Deadline: {task.deadline}\nPriority: {task.priority}",
        timeout=10
    )

def check_and_notify():
    # Check for upcoming deadlines and send notifications
    session = SessionLocal()
    now = datetime.datetime.now()
    
    tasks = session.query(Task).filter(
        Task.deadline != None,  # Ignore tasks without deadlines
        Task.deadline <= now + datetime.timedelta(minutes=10),  # Notify tasks due within 10 minutes
        Task.status != "completed"
    ).all()

    for task in tasks:
        send_notification(task)
    
    session.close()
