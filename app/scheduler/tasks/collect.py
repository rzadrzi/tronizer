import config
from coins.tron.tron import TRON
from models import WalletModel


async def collect():
    settings = config.Settings()
    all_wallets = await WalletModel.find().to_list()
    for wallet in all_wallets:
        if wallet.balance > 20:
            tron = TRON(settings.TRONGRID, wallet.public_key, wallet.private_key)
            await tron.usdt.transaction(settings.PUBLIC_KEY, 20)

            try:
                await tron.usdt.transaction(settings.PUBLIC_KEY, 20)
            except Exception as e:
                print("Collect function Error: ", e)
                pass