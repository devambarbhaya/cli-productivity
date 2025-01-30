import pytest
from click.testing import CliRunner
from cli import add

runner = CliRunner()

def test_cli_add_task():
    result = runner.invoke(add, ["--title", "CLI Test", "--priority", "high"])
    assert "Task added successfully!" in result.output

def test_cli_missing_title():
    result = runner.invoke(add, ["--priority", "high"])
    assert "Error: Title is required" in result.output
