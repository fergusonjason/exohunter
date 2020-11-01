from quart import Quart, jsonify, request, send_file, make_response
from routes import catalog_blueprint, util_blueprint, pixelfile_blueprint

if __name__ == "__main__":

    app = Quart(__name__)

    # register the blueprints
    app.register_blueprint(catalog_blueprint, url_prefix="/catalog")
    app.register_blueprint(util_blueprint, url_prefix="/util")
    app.register_blueprint(pixelfile_blueprint, url_prefix="/pixelfile")

    # run the webapp
    app.run()
