from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from commands.fixture import LoadFixturesCommand
from commands.loader import LoadRegionsCommand, LoadFinessEtablissementsCommand


import config
from covidbed.model.abc import db
from app import create_app

app = create_app(config)
app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('load_fixtures', LoadFixturesCommand)
manager.add_command('load_regions', LoadRegionsCommand)
manager.add_command('load_finesset', LoadFinessEtablissementsCommand)

if __name__ == '__main__':
    manager.run()
