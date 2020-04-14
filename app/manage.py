from flask_migrate import Migrate, MigrateCommand
from flask_script import Command, Manager, Server, Shell
from commands.fixture import LoadFixturesCommand


import config
from model.abc import db
from app import create_app

app = create_app(config)
app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('load_fixtures', LoadFixturesCommand)

if __name__ == '__main__':
    manager.run()
