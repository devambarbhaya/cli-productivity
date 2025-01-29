from database import SessionLocal, Task
from sqlalchemy.exc import SQLAlchemyError

def add_task(title, description, priority, tags, deadline):
    session = SessionLocal()
    try:
        task = Task(
            title=title,
            description=description,
            priority=priority,
            tags=",".join(tags) if tags else "",
            deadline=deadline
        )
        session.add(Task)
        session.commit()
        print(f"Task '{title}' added successfully")
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()
        
def list_tasks():
    session = SessionLocal()
    tasks = session.query(Task).all()
    session.close()
    return tasks

def delete_task(task_id):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.close()
        print(f"Task ID {task_id} deleted.")
    else:
        print("Task not found.")
    session.close()