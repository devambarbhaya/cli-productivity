import pytest
from tasks import add_task
from database import SessionLocal, Task

def test_add_valid_task():
    session = SessionLocal()
    task_id = add_task("Test Task", "A sample description", "high", "work", "2025-01-30")
    assert isinstance(task_id, int)

def test_add_task_without_title():
    with pytest.raises(ValueError):
        add_task("", "Missing title", "medium", "work", "2025-01-30")

def test_database_insertion():
    session = SessionLocal()
    task = Task(title="DB Test", description="Testing DB", priority="low", tags="test", deadline="2025-01-30", status="pending")
    session.add(task)
    session.commit()
    
    retrieved_task = session.query(Task).filter_by(title="DB Test").first()
    assert retrieved_task is not None
