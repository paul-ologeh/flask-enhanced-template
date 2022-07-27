import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = False
    DEBUG = os.environ.get("DEBUG", False)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    CORS_HEADERS = "Content-Type"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")


config = {"DEVELOPMENT": DevelopmentConfig, "TESTING": TestConfig}
