import click
from tasks import add_task, list_tasks, delete_task
import datetime

@click.group()
def cli():
    pass


@click.command()
@click.option("--title", prompt="Task title", help="Title of the task")
@click.option("--description", prompt="Task description", help="Description of the task")
@click.option("--priority", prompt="Task priority", type=click.Choice(["Low", "Medium", "High"]), help="Priority of the task")
@click.option("--tags", default="", help="Comma-separated tags")
@click.option("--deadline", default=None, help="Deadline (YYYY-MM-DD HH:MM:SS)")
def add(title, description, priority, tags, deadline):
    deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S") if deadline else None
    add_task(title, description, priority, tags.split(","), deadline)
    
@click.command()
def list():
    tasks = list_tasks()
    for task in tasks:
        print(f"[{task.id}] {task.title} - {task.status}")
    
cli.add_command(add)
cli.add_command(list)