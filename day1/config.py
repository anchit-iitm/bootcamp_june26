class configurations():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite2"
    secret_key = "it should be a secret, but for now im keeping it static for testing or development purposes"


class DevelopmentConfig(configurations):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(configurations):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False