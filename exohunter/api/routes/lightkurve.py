from quart import Blueprint, request, make_response, send_file

from services import LightKurveService
from util.constants import missions, kepler_quarters, k2_campaigns

lightkurve_blueprint = Blueprint("lighkurve", __name__)

@lightkurve_blueprint.route("", methods = ["GET"])
def get_lightkurve():

    service = LightKurveService()

    target = request.args.get("target")
    if target == None:
        return await make_response("You must provide a target", 400)

    mission = request.args.get("mission")
    if mission == None:
        return await make_response("You must specify the mission", 400)
    if mission not in missions:
        return await make_response("Invalid mission", 400)

    lkf = None

    if mission == "TESS":
        sector = request.args.get("sector")
        if sector == None:
            return await make_response("You must specify a TESS sector", 400)

        # TODO: Even the brain dead could do better than this
        if sector not in range(1,39):
            return await make_response("Invalid TESS sector", 400)

        lkf = service.compute_lightkurve(mission, target, sector=sector)
        pass
    elif mission == "K2":
        campaign = request.args.get("campaign")
        if campaign == None:
            return await make_response("You must specify a K2 campaign", 400)

        valid_campaign = campaign in k2_campaigns
        if valid_campaign == False:
            return await("You must specify a valid K2 campaign")

        lkf = service.compute_lightkurve(mission, target, campaign=campaign)

    elif mission == "Kepler":
        quarter = request.args.get("quarter")

        if quarter == None:
            return await make_response("You must specify a Kepler quarter", 400)

        int_quarter = int(quarter)
        valid_quarter = int_quarter in kepler_quarters
        if valid_quarter == False:
            return await make_response("Invalid Kepler quarter", 400)
        lkf = service.compute_lightkurve(mission, target, quarter=quarter)

    if lkf == None:
        return await make_response("Unable to generate lightkurve", 400)

    plot = lkf.plot()
    plot.get_figure().savefig("test.png")

    return await send_file("test.png", mimetype="application/png", as_attachment=True)