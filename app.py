#
# API Interface to the lighkurve functions
#
# TODO: refactor this into a decent-looking webapp
# TODO: use path variables to determine which catalog to use
# TODO: validate contents of request body

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

    # TODO: be restful and return a 404 here
    if tpf == None:
        return {"ERROR":"No results from search_targetpixelfile"}


    tpf_plot = tpf.plot()
    tpf_plot.get_figure().savefig("test.png")
    return await send_file("test.png", mimetype="application/png", as_attachment=True)

@app.route("/lightkurve")
async def get_lightkurve():

    request_json = await request.get_json()
    mission = request_json.get("mission")
    target = request_json.get("target")

    tpf = None
    if mission == "TESS":
        sector = request_json.get("sector")
        tpf = search_targetpixelfile(target=target, mission="TESS", sector=sector).download()
        pass

    if tpf == None:
        # TODO: be restful and return a 404 here
        return {}

    lightkurve_options = request_json.get("options")
    if lightkurve_options == None:
        lightkurve_options = {}

    result = tpf.to_lightkurve(aperture_mask="ALL")
    if (lightkurve_options.get("flatten") == True):
        result = result.flatten(window_length=401)

    result_plot = result.plot()
    result_plot.figure().savefig("test.png")

    return await send_file("test.png", mimetype="application/png", as_attachment=True)

# TODO: options is a bad idea, use **kwargs with default of None or whatever lk expects as default
# TODO: find out what other options for to_lightkurve are to give the option of using them
def get_lightkurve(pixelfile, options):

    aperture_mask = options.get("aperture_mask")

    return pixelfile.to_lightkurve(aperture_mask = aperture_mask)

# TODO: options is a bad idea, use **kwargs with default of None or whatever lk expects as default
# TODO: find out the other options of flatten to give the option of using them
def flatten_lightkurve(lightkurve, options):

    window_length = options.get("window_length")

    return lightkurve.flatten(window_length=window_length)

def fold_lightkurve(lightkurve, period):

    return lightkurve.fold(period = period)

app.run()