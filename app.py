#from flask import Flask, jsonify, request
from quart import Quart, jsonify, request, send_file
import platform
from lightkurve import search_targetpixelfile

from astroquery.mast import Catalogs

app = Quart(__name__)

@app.route("/info")
def info():
    result = { 'osversion':platform.system(), 'kernel': platform.release(), 'cpu': platform.processor(), 'pyversion': platform.python_version(),}
    return result

async def query_mast():
    return await Catalogs.query_object_async("M10", catalog="TIC")

@app.route("/catalog/getEntry", methods = ["POST"])
async def get_catalog_entry():

    print(f"content_type: {request.content_type}. content encoding: {request.content_encoding}, mimetype: {request.mimetype}")

    request_json = await request.get_json()
    target = request_json["target"]
    catalog = request_json["catalog"]
    radius = request_json["radius"]

    responses = Catalogs.query_object_async(target, catalog=catalog, radius=radius)
    response_data = responses[0].json()
    return {"result": response_data}

@app.route("/getPixelfile", methods = ["POST"])
async def get_pixelfile():

    request_json = await request.get_json()

    print(f"request json: {request_json}")
    target = request_json.get("target")
    if target == None:
        return {"ERROR":"No target specified"}

    mission = request_json.get("mission")
    if mission == None:
        mission = "TESS"

    tpf = None
    if mission == "TESS":
        sector = request_json.get("sector")
        tpf = search_targetpixelfile(target=target, mission="TESS", sector=sector).download()
    elif mission == "K2":
        campaign = request_json.get("campaign")
        tpf = search_targetpixelfile(target=target, mission="K2", campaign=campaign).download()
    elif mission == "Kepler":
        quarter = request_json.get("quarter")
        tpf = search_targetpixelfile(target=target, mission="Kepler", quarter=quarter).download()
        pass

    if tpf == None:
        return {"ERROR":"No results from search_targetpixelfile"}


    # tpf = search_targetpixelfile(target=target, quarter=quarter, mission=mission).download()

    tpf_plot = tpf.plot()
    tpf_plot.get_figure().savefig("test.png")
    return await send_file("test.png", mimetype="application/png", as_attachment=True)


def tess_search(target, sector):

    result = search_targetpixelfile(target=target, sector=sector, mission="TESS")
    return result

app.run()