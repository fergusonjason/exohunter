from quart import Blueprint, request, make_response, send_file
from services import PixelfileService
from util.constants import missions, kepler_quarters, k2_campaigns

pixelfile_blueprint = Blueprint("pixelfile", __name__)

@pixelfile_blueprint.route("", methods = ["GET"])
async def get_pixelfile():

    service = PixelfileService()

    target = request.args.get("target")
    if target == None:
        return await make_response("You must provide a target", 400)

    mission = request.args.get("mission")
    if mission == None:
        return await make_response("You must specify the mission", 400)
    if mission not in missions:
        return await make_response("Invalid mission", 400)


    tpf = None
    if mission == "TESS":
        sector = request.args.get("sector")
        if sector == None:
            return await make_response("You must specify a TESS sector", 400)

        # TODO: Validate sector is between 0 and 17
        tpf = await service.get_targetpixelfile(mission=mission, target=target, sector=sector)
    elif mission == "K2":
        campaign = request.args.get("campaign")
        if campaign == None:
            return await make_response("You must specify a K2 campaign", 400)

        valid_campaign = campaign in k2_campaigns
        if valid_campaign == False:
            return await("You must specify a valid K2 campaign")
            
        # TODO: Validate campaign is between C0 and C19
        tpf = await service.get_targetpixelfile(target=target, mission="K2", campaign=campaign)
    elif mission == "Kepler":
        quarter = request.args.get("quarter")
        if quarter == None:
            return await make_response("You must specify a Kepler quarter", 400)

        # TODO: Validate quarter
        int_quarter = int(quarter)
        valid_quarter = int_quarter in kepler_quarters
        if valid_quarter == False:
            return await make_response("Invalid Kepler quarter", 400)

        tpf = await service.get_targetpixelfile(target=target, mission="Kepler", quarter=quarter)

    if tpf == None:
        resp = await make_response("Record not found", 400)
        return resp


    tpf_plot = tpf.plot()
    tpf_plot.get_figure().savefig("test.png")
    return await send_file("test.png", mimetype="application/png", as_attachment=True)