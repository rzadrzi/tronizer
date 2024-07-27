import pymongo
from fastapi import HTTPException

import config
from coins import TRON
from models import WalletModel


class WalletController:
    def __init__(self):
        self.settings = config.Settings()

    async def choice(self) -> WalletModel:
        """
        check all wallets return wallet with MAX balance
        if all wallets are in order create new wallet and return it
        :return: wallet
        """
        wallets = await WalletModel.find(WalletModel.in_order == False) \
            .sort([(WalletModel.balance, pymongo.DESCENDING)]).to_list()
        if wallets is []:
            raise HTTPException(status_code=404, detail="Purchase was not crearted")

        if len(wallets) != 0:
            wallet = wallets[0]
            wallet.in_order = True
            await wallet.save()
            return wallet
        else:
            public_key, private_key = TRON.create_account()
            new_wallet = await WalletModel(
                public_key=public_key,
                private_key=str(private_key),
                in_order=True).create()
            return new_wallet
