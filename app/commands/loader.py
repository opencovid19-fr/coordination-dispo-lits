import os
from flask_script import Command, Option
from covidbed.util.loader import load_regions, load_finess_etablissements
from covidbed.repository.user import create_organization, get_or_create_region

import config


class LoadRegionsCommand(Command):

    def run(self):

        filepath = os.path.join(config.DATA_DIR, "regions.csv")
        for item in load_regions(filepath):
            get_or_create_region(**item)


class LoadFinessEtablissementsCommand(Command):

    option_list = (
        Option(help="file to import", dest="filename"),
    )

    def run(self, filename):
        filepath = os.path.join(config.DATA_DIR, filename)
        for item in load_finess_etablissements(filepath):
            create_organization(**item)
