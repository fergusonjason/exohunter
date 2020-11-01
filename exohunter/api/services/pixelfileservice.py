from lightkurve import search_targetpixelfile, search_lightcurvefile

class PixelfileService():

    def __init__(self):
        pass

    async def get_targetpixelfile(self, mission, target, sector=None, campaign=None, quarter=None, aperture_mask="ALL"):

        result = None

        if mission == "TESS":
            result = search_targetpixelfile(mission=mission, target=target,sector=sector)
        elif mission == "Kepler":
            result = search_targetpixelfile(mission=mission, target=target, quarter=quarter)
        elif mission == "K2":
            result = search_targetpixelfile(mission=mission, target=target, campaign=campaign)
        else:
            raise ValueError("Unknown mission, must be TESS, Kepler, or K2")

        return result.download()

