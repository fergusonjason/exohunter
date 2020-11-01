import platform
import datetime

from quart import Blueprint, jsonify

util_blueprint = Blueprint("util", __name__)

@util_blueprint.route("/info")
def info():
    result = { 'osversion':platform.system(), 'kernel': platform.release(), 'cpu': platform.processor(), 'pyversion': platform.python_version(),}
    return result

@util_blueprint.route("/mission/list")
def get_missions():
    result = ("TESS","Kepler","K2",)

    return jsonify(result)

@util_blueprint.route("/mission/kepler/quarters")
def get_kepler_quarters():

    result = (1,2,3,4,5,6,7, 8,9,10,11,12,13,14,15,16,17)

    return jsonify(result)

@util_blueprint.route("/mission/k2/campaigns")
def get_k2_campaigns():

    result = ("C0", "C1", "C2", "C3", "C4", "C5","C6","C7","C8","C9a","C9b","C10","C11","C12","C13","C14","C15","C16","C17","C18","C19")

    return jsonify(result)

@util_blueprint.route("/mission/tess/sectors")
def get_tess_sectors():

    result = list(range(1,37))


    # lookup_dict = {1:datetime.date(2018,7,25),
    #     2:datetime.date(2018,8, 22),
    #     3:datetime.date(2018,9.20),
    #     4:datetime.date(2018,10,18),
    #     5:datetime.date(2018,11,15),
    #     6:datetime.date(2018,12,11),
    #     7:datetime.date(2019,1,7),
    #     8:datetime.date(2019,2,2),
    #     9:datetime.date(2019,3,26),
    #     10:datetime.date(2019,4,22)}

    return jsonify(result)