from plyer import notification
from database import SessionLocal, Task
import datetime
import logging

def send_notification(task):
    # Send a desktop notification for a task
    notification.notify(
        title=f"Task Reminder: {task.title}",
        message=f"Deadline: {task.deadline}\nPriority: {task.priority}",
        timeout=10  # Time in seconds the notification stays on screen
    )

logging.basicConfig(filename="notifications.log", level=logging.INFO)

def check_and_notify():
    session = SessionLocal()
    now = datetime.datetime.now()
    logging.info(f"Checking for all tasks that are not completed.")

    # Modify query to fetch any task that isn't completed
    tasks = session.query(Task).filter(
        Task.status != "completed"  # Ignore tasks that are completed
    ).all()

    logging.info(f"Found {len(tasks)} task(s) to notify.")

    for task in tasks:
        send_notification(task)
        logging.info(f"Notification sent for task {task.id} - {task.title} at {now}")

    session.close()
