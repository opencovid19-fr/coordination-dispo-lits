import os
import config

from util.loader import load_finess_etablissements, load_regions
from repository.user import get_or_create_region, create_organization
from tests.utils.mixins import BaseTest


class TestLoader(BaseTest):
    fixtures = ["users.json"]

    def test_load_regions(self):
        filepath = os.path.join(config.DATA_DIR, "regions.csv")
        result = {item["code"]: item for item in load_regions(filepath)}
        self.assertEqual(len(result), 18)
        self.assertEqual(result["84"], {'code': '84', 'tncc': '1', 'libelle': 'Auvergne-Rhône-Alpes'})
        get_or_create_region(**result["84"])

    def test_load_etablissements(self):
        filepath = os.path.join(config.DATA_DIR, "test_ars.csv")
        result = [item for item in load_finess_etablissements(filepath)]

        get_or_create_region(**{'code': '84', 'tncc': '1', 'libelle': 'Auvergne-Rhône-Alpes'})
        create_organization(**result[0])

        self.assertEqual(result,
                         [{'name': 'CH DE FLEYRIAT',
                           'reg_code': '84',
                           'address': {'street': '900 RTE DE PARIS',
                                       'zipcode': '01440',
                                       'city': 'VIRIAT',
                                       'insee_code': '01451',
                                       'lon': 5.208596132279133,
                                       'lat': 46.22274478219284},
                           'etfiness': {
                               'finess_et': '010000024',
                               'finess_ej': '010000024'
                           }},
                          {'name': 'CH DE BELLEY',
                           'reg_code': '84',
                           'address': {'street': '52 R GEORGES GIRERD',
                                       'zipcode': '01300',
                                       'city': 'BELLEY',
                                       'insee_code': '01034',
                                       'lon': 5.684976115612651,
                                       'lat': 45.761208103246986},
                           'etfiness': {
                               'finess_et': '010000032',
                               'finess_ej': '010000032',
                           }},
                          {'name': 'CH DE TREVOUX - MONTPENSIER',
                           'reg_code': '84',
                           'address': {'street': '14 R DE L HOPITAL',
                                       'zipcode': '01606',
                                       'city': 'TRÃ\x89VOUX',
                                       'insee_code': '01427',
                                       'lon': 4.771956994861633,
                                       'lat': 45.9410740302987},
                           'etfiness': {
                               'finess_et': '010000065',
                               'finess_ej': '010000065'
                           }},
                          {'name': 'CH DU PAYS DE GEX',
                           'reg_code': '84',
                           'address': {'street': '160 R MARC PANISSOD',
                                       'zipcode': '01174',
                                       'city': 'GEX',
                                       'insee_code': '01173',
                                       'lon': 6.057731423296567,
                                       'lat': 46.32233765353798},
                           'etfiness': {
                               'finess_et': '010000081',
                               'finess_ej': '010000081',
                           }},
                          {'name': 'CH DE MEXIMIEUX',

                           'reg_code': '84',
                           'address': {'street': '13 AV DU DOCTEUR BOYER',
                                       'zipcode': '01800',
                                       'city': 'MEXIMIEUX',
                                       'insee_code': '01244',
                                       'lon': 5.194579440045477,
                                       'lat': 45.906191628020245},
                           'etfiness': {
                               'finess_et': '010000099',
                               'finess_ej': '010000099'
                           }}])
