import os, csv
from pyproj import Proj, transform


inProj = Proj(init='epsg:2154')
outProj = Proj(init='epsg:4326')


def load_regions(filepath):
    with open(filepath, "r", encoding="utf-8") as fp:
        reader = csv.reader(fp, delimiter=",")
        headers = {}
        for i, row in enumerate(reader):
            if i == 0:
                headers = {item: j for j, item in enumerate(row)}
                continue
            yield {
                "code": row[headers["reg"]],
                "tncc": row[headers["tncc"]],
                "libelle": row[headers["libelle"]]
            }


def load_finess_etablissements(filepath):
    """
    gid,finess,finess_for,siret,datemaj,rs,categorie,reg_code,com_code,adresse,loc_ign,loc_score,post_code,com_lib,id_ign,x,y,x_wgs84,y_wgs84,finess_ej

    :param filepath:
    :return:
    """
    if not os.path.isfile(filepath):
        raise ValueError("No file exist.")

    with open(filepath, "r", encoding="ISO-8859-1") as fp:
        reader = csv.reader(fp, delimiter=",")
        headers = {}
        for i, row in enumerate(reader):
            if i == 0:
                headers = {item:j for j, item in enumerate(row)}
                continue

            x1, y1 = float(row[headers["x"]]), float(row[headers["y"]])
            x2, y2 = transform(inProj, outProj, x1, y1)

            yield {
                "name": row[headers["rs"]],
                "reg_code": row[headers["reg_code"]],
                "address": {
                    "street": row[headers["adresse"]],
                    "zipcode": row[headers["post_code"]],
                    "city": row[headers["com_lib"]],
                    "insee_code": row[headers["com_code"]],
                    "lon": x2,
                    "lat": y2,
                },
                "etfiness": {
                    "finess_et": row[headers["finess"]],
                    "finess_ej": row[headers["finess"]],
                }
            }
