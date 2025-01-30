# Task - Command Line Task Manager

Task is a simple lightweight command-line tool for managing tasks efficiently. It allows users to add, list, edit, and delete tasks using an SQLite Database.

## Features

- Add tasks with a title, description, priority, tags, deadline, and status.
- List tasks with filtering options.
- Edit existing tasks.
- Delete tasks.
- Get notifications for upcoming tasks.

## Installation

1. Clone the repository

```
git clone https://github.com/devambarbhaya/cli-productivity.git

cd cli-productivity
```

2. Create virtual environment

```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

3. Install Dependencies

```
pip install -r requirements.txt
```

4. Install as a Python Package

```
pip install --editable .
```

5. Now, you can use the task CLI command globally:

```
task --help
```

## Usage

📌 Add a Task

```
task add "Finish report" --description "Complete the financial report" --priority High --tags work,urgent --deadline "2025-02-01 18:00:00"
```

📌 List all tasks

```
task list
```

📌 List tasks with filter

```
task list --priority High --status pending
```

📌 Edit tasks

```
task edit <task_id> --status completed
```

📌 Edit tasks

```
task delete <task_id>
```

📌 Enable Notifications for Upcoming Tasks

```
python notifications/scheduler.py  # Run this script to check for upcoming tasks
```

## Packaging as Standalone Executable

📌 Install PyInstaller

```
pip install pyinstaller
```

📌 Build the executable

```
pyinstaller --onefile --name task main.py
```

📌 Run the Executable

```
./dist/task-cli --help  # Linux/Mac
dist\task-cli.exe --help  # Windows
```

## License

This project is protected under the MIT License

## Author

Developed by Devam Barbhaya

📧 Contact: [barbhaya.devam@gmail.com]
