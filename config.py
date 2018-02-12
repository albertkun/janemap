import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'password'
    SSL_DISABLE = False

    @staticmethod
    def init_app(app):
        pass

    @classmethod
    def init_app(app):
        Config.init_app(app)

config = {

}
