import config
from coins import TRON
from models import WalletModel


async def balance_checker():
    settings = config.Settings()
    wallets = await WalletModel.find().to_list()
    for w in wallets:
        try:
            trn = TRON(settings.TRONGRID, w.public_key, w.private_key)
            balance = await trn.usdt.balance()
            w.balance = balance
            await w.save()
        except Exception as e:
            print("Balance Checker Error: ", e)
            pass
