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
        session.add(task)
        session.commit()
        print(f"Task '{title}' added successfully.")
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
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            session.delete(task)
            session.commit()  # ✅ Commit the delete operation
            print(f"Task ID {task_id} deleted.")
        else:
            print("Task not found.")
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()
        
def edit_task(task_id, title=None, description=None, priority=None, tags=None, deadline=None, status=None):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            print("Task not found")
            return
        if title:
            task.title=title
        if description:
            task.description=description
        if priority:
            task.priority=priority
        if tags:
            task.tags=",".join(tags)
        if deadline:
            task.deadline=deadline
        if status:
            task.status=status
            
        session.commit()
        print(f"Task ID {task_id} updated successfully")
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()