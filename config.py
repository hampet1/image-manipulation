from app import app


class Config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


class ProductionConfig(Config):

    def init_app(app):
        Config.init_app(app)

    DEBUG = False
    UPLOADS = app.root_path + '\static\images'
    SESSION_COOKIE_SECURE = False
    UPLOAD_FOLDER = "app\static\images/"
    PROCESSED_IMAGE = app.root_path + '\static\images'




class DevelopmentConfig(Config):
    DEBUG = True
    UPLOADS = app.root_path + '\static\images'
    SESSION_COOKIE_SECURE = False
    UPLOAD_FOLDER = "app\static\images/"
    PROCESSED_IMAGE = app.root_path + '\static\images'
    SEND_FILE_MAX_AGE_DEFAULT = 0


class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
