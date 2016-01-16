"""
Manager script :)

Takes the following commands:
- runserver
- shell
- update_tf2_items (Updates information about TF2 Items stored in the DB - Runs every 24h via cron)
- delete_expired_packages (Deletes packages that have expired - Runs every 24h via cron)
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