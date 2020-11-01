from astroquery.vizier import VizierClass as VizierCatalogs

from .basecontext import BaseContext

# context for catalog queries to use Vizier database
class VizierContext(BaseContext):

    # TODO: Not a fan of how I have to reference this
    VIZIER_CATALOGS = {
        "TESS": "IV/38",
        "Kepler": "V/133",
        "K2": None
    }

    DEFAULT_MISSION = "TESS"

    def __init__(self):
        self.vcat = VizierCatalogs()

    def get_catalog_name(self, catalog):
        pass

    async def query_single_object(self, target, **kwargs):

        if target == None:
            # this needs to be an exception
            return None

        if kwargs.get("mission") == None:
            kwargs["mission"] = VizierContext.DEFAULT_MISSION

        kwargs["catalog"] = VizierContext.VIZIER_CATALOGS.get(kwargs.get("mission"))

        return await self.vcat.query_object_async(target, kwargs)

    # query obj needs object_name, catalog, radius (opt), coordinate_system (opt)
    # async def query_single_object(self, target, mission, catalog, radius = None):

    #     # with vizier you have to instantiate an object of the class *eyeroll*
    #     catalog = VizierContext.VIZIER_CATALOGS.get(mission)

    #     return await self.vcat.query_object_async(target, catalog=catalog, radius = None)

    # kwargs is expected to be in the format "{column:expression}, i.e. {"GLON":">49.0 & <51.0","GLAT":"<0"}
    async def query_with_contraints(self, mission, **kwargs):

        catalog = VizierContext.VIZIER_CATALOGS.get(mission)

        return await self.vcat.query_constraints_async(catalog=catalog, **kwargs)