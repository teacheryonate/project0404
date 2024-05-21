from config.default import *
from logging.config import dictConfig

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test1000:1@localhost:3306/test1000?serverTimezone=Asia/Seoul"


# SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
#     os.path.join(BASE_DIR, 'pybo.db')
# )



SQLALCHEMY_TRACK_MODIFICATION=False


SECRET_KEY=b'\xe1\xda\x8eq\x17\xcb\xd8\xd63\x01%\x96$\xe1\xd3\xb0'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/project0404.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})