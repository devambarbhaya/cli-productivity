import pytest
from notifications import send_notification
from database import Task

def test_send_notification():
    task = Task(title="Test Notification", deadline="2025-01-30", priority="high")
    try:
        send_notification(task)
    except Exception:
        pytest.fail("Notification sending failed")
