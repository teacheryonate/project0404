from config.default import *
from logging.config import dictConfig

from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, '.env'))

SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))


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