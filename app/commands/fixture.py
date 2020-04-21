import os

from flask import current_app
from flask_script import Command
from flask_fixtures import load_fixtures, loaders

import config
from covidbed.model.abc import db

class LoadFixturesCommand(Command):

    def run(self):

        db.drop_all()
        # Setup the database
        db.create_all()
        # Rollback any lingering transactions
        db.session.rollback()

        # Construct a list of paths within which fixtures may reside
        default_fixtures_dir = os.path.join(current_app.root_path, 'fixtures')
        # All relative paths should be relative to the app's root directory.
        fixtures_dirs = [default_fixtures_dir]

        # Load all of the fixtures
        for filename in config.FIXTURES_LIST.split(","):
            for directory in fixtures_dirs:
                filepath = os.path.join(directory, filename)
                if not os.path.exists(filepath):
                    continue

                load_fixtures(db, loaders.load(filepath))
                break

            else:
                raise IOError("Error loading '{0}'. File could not be found".format(filename))
