from astroquery.mast import Catalogs as MastCatalogs
from astroquery.vizier import Vizier as VizierCatalogs
#import MastContext, VizierContext
#from tessservice import TessService

class MastCatalogService():

    def __init__(self):
        pass

    async def query_object(self, target, catalog):

        # need to ensure catalog is only TIC, Kepler, or K2
        result = MastCatalogs.query_object_async(target, catalog=catalog)
        return result

class VizierCatalogService():

    def __init__(self):

        self.vizier_catalogs = {
            "TIC": "IV/38",
            "Kepler": "V/133",
            "K2": None,
        }


    async def query_object(self, target, catalog):

        translated_catalog = self.vizier_catalogs.get(catalog)
        result = VizierCatalogs.query_object_async(target, catalog=translated_catalog)
        return result

# class CatalogService():


#     def __init__(self, source):

#         # hard-code to using TESS from MAST for now
#         self.__service = TessService("MAST")

#         self.__source = source

#     def get_context(self, source):

#         if self.__source == "MAST":
#             return MastContext()
#         elif self.__source == "Vizier":
#             return VizierContext()
#         else:
#             # TODO: should throw exception here
#             return None
#     pass

#     def query_object(self, target):

#         result = self.__service.query_object(target)
#         return result

#     def get_single_object(self, target, **kwargs):

#         requested_source = kwargs.get("source")
#         context = self.get_context(requested_source)
#         context.query_single_object(target, **kwargs)
#         pass

#     def __get_single_object_mast(self):
#         pass

#     def __get_single_object_viz(self):
#         pass

    # def get_object_by_criteria(requested_source="MAST", **kwargs):

    #     context = self.get_context(requested_source)

    #     pass