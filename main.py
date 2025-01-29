from database import init_db
from cli import cli

if __name__ == "__main__":
    init_db()  # Ensure tables are created
    cli()
