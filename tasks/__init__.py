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
        print(f"✅ Task '{title}' added successfully.")
    except SQLAlchemyError as e:
        print(f"❌ Error: {e}")
        session.rollback()
    finally:
        session.close()
    list_tasks()  # Show updated task list

def list_tasks():
    session = SessionLocal()
    tasks = session.query(Task).order_by(Task.id).all()
    session.close()

    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📌 Tasks:")
        for task in tasks:
            print(f" - [{task.id}] {task.title} (Status: {task.status}, Priority: {task.priority})")
    return tasks

def delete_task(task_id):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            session.delete(task)
            session.commit()
            print(f"🗑️ Task ID {task_id} deleted.")
            reindex_tasks(session)  # Reindex after deletion
        else:
            print("⚠️ Task not found.")
    except SQLAlchemyError as e:
        print(f"❌ Error: {e}")
        session.rollback()
    finally:
        session.close()
    list_tasks()  # Show updated task list

def edit_task(task_id, title, description, priority, tags, deadline, status):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            if title: task.title = title
            if description: task.description = description
            if priority: task.priority = priority
            if tags: task.tags = ",".join(tags)
            if deadline: task.deadline = deadline
            if status: task.status = status
            session.commit()
            print(f"✏️ Task ID {task_id} updated successfully.")
        else:
            print("⚠️ Task not found.")
    except SQLAlchemyError as e:
        print(f"❌ Error: {e}")
        session.rollback()
    finally:
        session.close()
    list_tasks()  # Show updated task list

def reindex_tasks(session):
    """Reorders task IDs to maintain sequential numbering."""
    tasks = session.query(Task).order_by(Task.id).all()
    for index, task in enumerate(tasks, start=1):
        task.id = index
    session.commit()
    print("🔄 Task IDs reindexed.")
