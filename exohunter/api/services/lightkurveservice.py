from lightkurve import search_lightcurvefile


class LightKurveService():

    def __init__(self):
        pass

    async def compute_lightkurve(self, mission, target, sector=None, campaign=None, quarter=None, radius=None, month=None, limit=None):

        result = None
        if mission == "TESS":
            result = search_lightcurvefile(mission=mission, target=target, sector=sector, radius=radius, month=month, limit=limit)
        elif mission == "Kepler":
            result = search_lightcurvefile(mission=mission, target=target, quarter=quarter, radius=radius, month=month, limit=limit)
            pass
        elif mission == "K2":
            result = search_lightcurvefile(mission=mission, target=target, campaign=campaign, radius=radius, month=month, limit=limit)
            pass
        else:
            raise ValueError("Unknown mission, must be TESS, Kepler, or K2")

        return result.download()

    def get_flattened_lightkurve(self, lightkurve, window_length, polyorder=None, return_trend=None, break_tolerance=None, niters=None, sigma=None, mask=None):

        return lightkurve.flatten(window_length=window_length, polyorder=polyorder, return_trend=return_trend, break_tolerance=break_tolerance, niters=niters, signma=sigma, mask=mask)

    def get_folded_lightkurve(self, lightkurve, period, t0=0):

        return lightkurve.fold(period=period, t0=t0)