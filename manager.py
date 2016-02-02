"""
Manager script :)

Takes the following commands:
- runserver
- shell
- setup_tables
- update_packs
- update_ids
"""

from app import app
from flask.ext.script import Manager

manager = Manager(app)


@manager.command
def update_packs():
    from app.scripts.scripts import update_packs
    update_packs()


@manager.command
def update_ids():
    from app.scripts.scripts import update_ids
    update_ids()


@manager.command
def setup_tables():
    from app.scripts.scripts import setup_tables
    setup_tables()

if __name__ == "__main__":
    manager.run()