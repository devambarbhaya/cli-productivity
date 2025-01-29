import click
from tasks import add_task, get_tasks, delete_task, edit_task
import datetime

@click.group()
def cli():
    """Task Management CLI"""
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
    tags_list = tags.split(",") if tags else []  # Convert tags to a list
    add_task(title, description, priority, tags_list, deadline)

@click.command(name="list")
@click.option("--title", help="Filter by task title")
@click.option("--priority", type=click.Choice(["Low", "Medium", "High"]), help="Filter by priority")
@click.option("--status", type=click.Choice(["pending", "completed", "in-progress"]), help="Filter by status")
@click.option("--tags", help="Filter by tag")
@click.option("--deadline-before", help="Filter tasks with deadlines before a given date (YYYY-MM-DD)")
@click.option("--deadline-after", help="Filter tasks with deadlines after a given date (YYYY-MM-DD)")
def list(title, priority, status, tags, deadline_before, deadline_after):
    """List tasks with optional filters."""
    filters = {k: v for k, v in {
        "title": title,
        "priority": priority,
        "status": status,
        "tags": tags,
        "deadline_before": deadline_before,
        "deadline_after": deadline_after
    }.items() if v is not None}  # Remove None values

    tasks = get_tasks(filters)

    if not tasks:
        click.echo("No tasks found.")
    else:
        click.echo("Tasks:")
        for task in tasks:
            click.echo(f"- [{task.id}] {task.title} ({task.priority}) - Status: {task.status}, Deadline: {task.deadline}, Tags: {task.tags}")

@click.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task by ID."""
    delete_task(task_id)
    click.echo(f"Task {task_id} deleted.")

@click.command()
@click.argument("task_id", type=int)
@click.option("--title", default=None, help="New title of the task")
@click.option("--description", default=None, help="New description of the task")
@click.option("--priority", type=click.Choice(["Low", "Medium", "High"]), default=None, help="New priority")
@click.option("--tags", default=None, help="New comma-separated tags")
@click.option("--deadline", default=None, help="New deadline (YYYY-MM-DD HH:MM:SS)")
@click.option("--status", type=click.Choice(["pending", "completed", "in-progress"]), help="New status (e.g., pending, completed)")
def edit(task_id, title, description, priority, tags, deadline, status):
    """Edit an existing task."""
    deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S") if deadline else None
    tags_list = tags.split(",") if tags else None  # Convert tags to a list or None
    edit_task(task_id, title, description, priority, tags_list, deadline, status)
    click.echo(f"Task {task_id} updated.")

# Register commands
cli.add_command(add)
cli.add_command(list)
cli.add_command(delete)
cli.add_command(edit)
