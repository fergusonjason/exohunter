from astroquery.vizier import Vizier
from astroquery.mast import Catalogs as Mast
from context import MastContext, VizierContext

class TessService():

    # source is either MAST or Vizier
    def __init__(self, source):

        self.mission = "TESS"
        self.__source = source

        self.context = None
        if source == "MAST":
            self.context = MastContext()
        if source == "Vizier":
            self.context = VizierContext()
        pass

    async def query_object(self, target):

        result = None
        if self.__source == "MAST":
            result = await Mast.query_object_async(target, catalog="TESS")
            pass
        elif self.__source == "Vizier":
            result = await Vizier.query_object_async(target, catalog="TESS")

        return result


    async def __query_object_mast(self, targer):
        pass

    async def query_by_criteria(self, target, columns=None, column_filters=None):

        # TODO: process column filters

        result = await Vizier.query_object_async(target, catalog="TESS")

        return result

    async def query_constraints(self, target, columns=None, column_filters=None):

        pass