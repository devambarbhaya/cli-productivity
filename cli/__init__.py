import click
from tasks import add_task, list_tasks, delete_task, edit_task
import datetime

@click.group()
def cli():
    pass

@click.command()
@click.argument("title")
@click.option("--description", default="", help="Description of the task")
@click.option("--priority", type=click.Choice(["Low", "Medium", "High"]), default="Medium", help="Priority of the task")
@click.option("--tags", default="", help="Comma-separated tags")
@click.option("--deadline", default=None, help="Deadline (YYYY-MM-DD HH:MM:SS)")
def add(title, description, priority, tags, deadline):
    """Add a new task."""
    deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S") if deadline else None
    add_task(title, description, priority, tags.split(",") if tags else [], deadline)

@click.command()
def list():
    """List all tasks."""
    list_tasks()

@click.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task by ID."""
    delete_task(task_id)
    
@click.command()
@click.argument("task_id", type=int)
@click.option("--title", default=None, help="New title of the task")
@click.option("--description", default=None, help="New description of the task")
@click.option("--priority", type=click.Choice(["Low", "Medium", "High"]), default=None, help="New priority")
@click.option("--tags", default=None, help="New comma-separated tags")
@click.option("--deadline", default=None, help="New deadline (YYYY-MM-DD HH:MM:SS)")
@click.option("--status", default=None, help="New status (e.g., pending, completed)")
def edit(task_id, title, description, priority, tags, deadline, status):
    """Edit an existing task."""
    deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S") if deadline else None
    edit_task(task_id, title, description, priority, tags.split(",") if tags else None, deadline, status)

cli.add_command(add)
cli.add_command(list)
cli.add_command(delete)
cli.add_command(edit)
