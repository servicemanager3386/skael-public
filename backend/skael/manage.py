from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand
from skael.skael import create_app

app = create_app()

manager = Manager(app)
migrate = Migrate(app, app.db)
manager.add_command('db', MigrateCommand)

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        app.db.drop_all()

if __name__ == '__main__':
    manager.run()