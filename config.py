import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://stocks_db_opun_user:DRbMaduq4hWj8Axl9tMKiAORzvw8zD9i@dpg-creb5sbv2p9s73cthoag-a/stocks_db_opun')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
