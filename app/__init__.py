import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sassutils.wsgi import SassMiddleware
from werkzeug.urls import url_decode


class MethodRewriteMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if '__method__' in environ.get('QUERY_STRING', ''):
            args = url_decode(environ['QUERY_STRING'])
            method = args.get('__method__')
            if method:
                environ['REQUEST_METHOD'] = method
        return self.app(environ, start_response)

app = Flask(__name__)

app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/css', 'static/css', 'static/css')
})
app.wsgi_app = MethodRewriteMiddleware(app.wsgi_app)

app.config.from_object(os.environ['CHERRY_CARD_CONFIG'])

db = SQLAlchemy(app)
db.create_all()


from .recommendation import recommendation  # noqa
from .routes import app as root  # noqa

app.register_blueprint(recommendation)
app.register_blueprint(root)
