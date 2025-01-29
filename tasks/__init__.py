from database import SessionLocal, Task
from sqlalchemy.exc import SQLAlchemyError

def add_tasks(title, description, priority, tags, deadline):
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