from httpx import AsyncClient, Timeout, Limits
from tronpy import AsyncTron, AsyncContract
from tronpy.providers import AsyncHTTPProvider
from tronpy.keys import PrivateKey
from tronpy.defaults import CONF_MAINNET


class TRX:

    def __init__(self, api_key, public_key, private_key=""):
        self.api_key = api_key
        self.public_key = public_key
        self.private_key = PrivateKey(bytes.fromhex(private_key))

    async def client(self):
        _http_client = AsyncClient(limits=Limits(max_connections=100, max_keepalive_connections=20),
                                   timeout=Timeout(timeout=10, connect=5, read=5))
        provider = AsyncHTTPProvider(CONF_MAINNET, client=_http_client, api_key=self.api_key)
        client = AsyncTron(provider=provider)
        # client = await client.get_contract(self.usdt_contract)
        return client

    async def balance(self):
        client = await self.client()
        return await client.get_account_balance(self.public_key)
    
    async def transaction(self, to, amount):
        client = await self.client()
        amount = amount * 10**6
        txn = (
                client.trx.transfer(self.public_key, to, amount)
                .fee_limit(30_000_000)
        )
        txn = await txn.build()
        # txn = txn.inspect()
        txn = await txn.sign(self.private_key).broadcast()
        txn = await txn.wait()
        return txn

    async def delegate(self):
        pass

    async def undelegate(self):
        pass
