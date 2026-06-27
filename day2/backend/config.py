class configurations():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite2"
    SECRET_KEY = "it should be a secret, but for now im keeping it static for testing or development purposes"

    SECURITY_LOGIN_URL = "/2345678BJJHJVCR456788N;'.[.]"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authorization"


class DevelopmentConfig(configurations):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(configurations):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False