from quart import Blueprint, request
from services import MastCatalogService, VizierCatalogService

catalog_blueprint = Blueprint("catalog", __name__)

 #catalog_service = CatalogService()

def get_catalogs():
    pass

@catalog_blueprint.route("/entry", methods = ["GET"])
async def get_catalog_object():

    target = request.args.get("target")
    source = request.args.get("source")
    catalog = request.args.get("catalog")
    catalog_service = None
    query_result = None
    if source == None:
        source = "MAST"
        catalog_service = MastCatalogService()
        query_result = await catalog_service.query_object(target, catalog=catalog)
    elif source == "Vizier":
        catalog_service = VizierCatalogService()  # this comes back as XML???
        query_result = await catalog_service.query_object(target, catalog=catalog)
        print(query_result.content)

    # query_result = await catalog_service.query_object(target, catalog=catalog)
    # print(type(query_result).__name__)
    query_result_json = query_result.json()

    return query_result_json

# post can handle more criteria than get
@catalog_blueprint.route("/<mission>/entry", methods = ["POST"])
async def get_catalog_entry_post(mission):

    if mission == None:
        # this needs to be an error message, don't know if it could happen w/ a path variable
        return {}

    request_json = await request.get_json()

    target = request_json.get("target")
    # catalog = request_json["catalog"]
    radius = request_json["radius"]

    pass
    # responses = catalog_service.get_single_object(target)


    # # responses = Catalogs.query_object_async(target, catalog=catalog, radius=radius)
    # response_data = responses[0].json()

    # return {"result": response_data}