
from tronpy.keys import PrivateKey
from .trx import TRX
from .usdt import USDT


class TRON:
    def __init__(self, api_key, public_key, private_key):
        self.api_key = api_key
        self.public_key = public_key
        self.private_key = private_key

        self.trx = TRX(self.api_key, self.public_key, self.private_key)
        self.usdt = USDT(self.api_key, self.public_key, self.private_key)

    @staticmethod
    def create_account():
        private_key = PrivateKey.random()
        public_key = private_key.public_key.to_base58check_address()
        return public_key, private_key






