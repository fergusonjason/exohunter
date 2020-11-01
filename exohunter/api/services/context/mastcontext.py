from astroquery.mast import Catalogs as MastCatalogs
from .basecontext import BaseContext

# context for catalog queries to use MAST database
class MastContext(BaseContext):

    # take decorator in form "col < value" and convert it to "col.lt = value" as expected by MAST
    def convert_to_decorator(self, constraint):
        pass

    async def query_single_object(self, target, **kwargs):

        pass
        # return await MastCatalogs.query_object_async(target, catalog=catalog, radius=radius)
    # async def query_single_object(self, target, catalog, radius=None):

    #     return await MastCatalogs.query_object_async(target, catalog=catalog, radius=radius)

    #MAST uses query constraints as defined in https://catalogs.mast.stsci.edu/docs/general_catalog_service.html#basic-filtering
    async def query_with_constraints(self, target, catalog, constraints):
        pass
    pass