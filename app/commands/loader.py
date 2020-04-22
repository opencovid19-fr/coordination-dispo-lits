import os
from flask_script import Command, Option
from covidbed.util.loader import load_regions, load_finess_etablissements
from covidbed.repository.user import create_organization, get_or_create_region, create_user

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


class CreatePlatformCommand(Command):

    option_list = (
        Option(help="platform name", dest="platform"),
        Option(help="email", dest="email"),
        Option(help="password", dest="password"),
        Option(help="firstname", dest="firstname"),
        Option(help="lastname", dest="lastname"),
        Option(help="phonenumber", dest="phonenumber"),
    )

    def run(self, platform, email, password, firstname, lastname, phonenumber):
        params = {
            "email": email,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "phone_number": phonenumber
        }
        organization = {
            "name": password,
        }
        create_user(params, platform=organization)
