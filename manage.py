from app import create_app, db
from flask.cli import with_appcontext
import click

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db}

@app.cli.command("create-db")
@with_appcontext
def create_db():
    db.create_all()
    click.echo("Database created.")