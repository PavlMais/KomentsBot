import os

try:
    import local_config 

    DB_URL = local_config.DB_URL
    TOKEN  = local_config.TOKEN
    TGPH_TOKEN = local_config.TGPH_TOKEN
except ImportError:
    DB_URL = os.environ('DB_URL')
    TOKEN  = os.environ('TOKEN')
    TGPH_TOKEN  = os.environ('TGPH_TOKEN')




COMMENTS_OF_PARTY = 5