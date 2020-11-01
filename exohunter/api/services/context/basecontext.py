
# Base class containing "abstract" methods
class BaseContext():

    async def query_single_object(self, target, **kwargs):
        pass
    # async def query_single_object(self, target, mission, radius = None):
    #     pass

    async def query_with_constraints(self, mission, **kwargs):
        pass
    pass