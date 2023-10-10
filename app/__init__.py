from quart import Quart
import quart_cors
from .views import todo, auth, manifest

def create_app():
    app = Quart(__name__, static_folder='static')
    app = quart_cors.cors(app, allow_origin="https://chat.openai.com")

    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(manifest.bp)

    return app
