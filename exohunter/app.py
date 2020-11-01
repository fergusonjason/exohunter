#
# API Interface to the lighkurve functions
#
# TODO: refactor this into a decent-looking webapp
# TODO: use path variables to determine which catalog to use
# TODO: validate contents of request body

from quart import Quart, jsonify, request, send_file, make_response
import platform
import sys
from lightkurve import search_targetpixelfile
# from .api.util.services import get_flattened_lightkurve, get_folded_lightkurve, compute_lightkurve, get_targetpixelfile
from astroquery.mast import Catalogs

from exohunter.api.routes.catalog import catalog_blueprint
# from exohunter.api.routes.catalog import catalog_blueprint
from .api.routes.util import util_blueprint


app = Quart(__name__)
app.register_blueprint(util_blueprint, url_prefix="/util")
app.register_blueprint(catalog_blueprint, url_prefix="/catalog")

# @app.route("/catalog/getEntry2", methods = ["POST"])
# async def get_catalog_entry_with_criteria():
#     pass

# @app.route("/getPixelfile", methods = ["POST"])
# async def get_pixelfile():

#     request_json = await request.get_json()

#     target = request_json.get("target")
#     if target == None:
#         return {"ERROR":"No target specified"}

#     mission = request_json.get("mission")
#     if mission == None:
#         mission = "TESS"

#     tpf = None
#     if mission == "TESS":
#         sector = request_json.get("sector")
#         tpf = await get_targetpixelfile(mission=mission, target=target, sector=sector)
#         #tpf = search_targetpixelfile(target=target, mission="TESS", sector=sector).download()
#     elif mission == "K2":
#         campaign = request_json.get("campaign")
#         tpf = await get_targetpixelfile(target=target, mission="K2", campaign=campaign)
#         #tpf = await search_targetpixelfile(target=target, mission="K2", campaign=campaign).download()
#     elif mission == "Kepler":
#         quarter = request_json.get("quarter")
#         tpf = await get_targetpixelfile(target=target, mission="Kepler", quarter=quarter)
#         #tpf = await search_targetpixelfile(target=target, mission="Kepler", quarter=quarter).download()

#     # TODO: be restful and return a 404 here
#     if tpf == None:
#         resp = make_response("Record not found", 400)
#         return resp
#         #return {"ERROR":"No results from search_targetpixelfile"}


#     tpf_plot = tpf.plot()
#     tpf_plot.get_figure().savefig("test.png")
#     return await send_file("test.png", mimetype="application/png", as_attachment=True)

# @app.route("/lightkurve")
# async def get_lightkurve():

#     request_json = await request.get_json()
#     mission = request_json.get("mission")
#     target = request_json.get("target")

#     tpf = None
#     if mission == "TESS":
#         sector = request_json.get("sector")
#         tpf = compute_lightkurve(mission=mission, target=target, sector=sector)
#         #tpf = search_targetpixelfile(target=target, mission="TESS", sector=sector).download()
#     elif mission == "Kepler":
#         pass
#     elif mission == "K2":
#         pass
#     else:
#         return {"ERROR":"Bad mission name"}

#     if tpf == None:
#         # TODO: be restful and return a 404 here
#         return {}

#     lightkurve_options = request_json.get("options")
#     if lightkurve_options == None:
#         lightkurve_options = {}

#     result = tpf.to_lightkurve(aperture_mask="ALL")
#     if (lightkurve_options.get("flatten") == True):
#         result = result.flatten(window_length=401)

#     result_plot = result.plot()
#     result_plot.figure().savefig("test.png")

#     return await send_file("test.png", mimetype="application/png", as_attachment=True)

# TODO: options is a bad idea, use **kwargs with default of None or whatever lk expects as default
# TODO: find out what other options for to_lightkurve are to give the option of using them
def get_basic_lightkurve(pixelfile, options):

    aperture_mask = options.get("aperture_mask")

    return pixelfile.to_lightkurve(aperture_mask = aperture_mask)

# TODO: options is a bad idea, use **kwargs with default of None or whatever lk expects as default
# TODO: find out the other options of flatten to give the option of using them
def flatten_lightkurve(lightkurve, options):

    window_length = options.get("window_length")

    return lightkurve.flatten(window_length=window_length)

def fold_lightkurve(lightkurve, period):

    return lightkurve.fold(period = period)

# yes, this is temporary, values will either be database or stored in a flat file
@app.route("/lookup/<code>", methods=["GET"])
def get_lookups(code):

    value = None
    if code == "catalogs":
        value = ["TESS","K2","Kepler"]

    return jsonify(value)



# init()

if __name__ == "__main__":
    in_env = sys.prefix == sys.base_prefix
    print(f"osversion: {platform.system()}, kernel: {platform.release()}, cpu: {platform.processor()}, pyversion: {platform.python_version()}, virtualenv: {in_env}")

    app.run()