from httpx import AsyncClient, Timeout, Limits
from tronpy import AsyncTron, AsyncContract, Tron
from tronpy.providers import AsyncHTTPProvider, HTTPProvider
from tronpy.keys import PrivateKey
from tronpy.defaults import CONF_MAINNET, CONF_NILE


class USDT:
    def __init__(self, api_key, public_key, private_key=""):
        self.usdt_contract = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"
        self.api_key = api_key
        self.public_key = public_key
        self.private_key = PrivateKey(bytes.fromhex(private_key))

    async def client(self):
        _http_client = AsyncClient(limits=Limits(max_connections=100, max_keepalive_connections=20),
                                   timeout=Timeout(timeout=10, connect=5, read=5))
        provider = AsyncHTTPProvider(CONF_MAINNET, client=_http_client, api_key=self.api_key)
        client = AsyncTron(provider=provider)
        client = await client.get_contract(self.usdt_contract)
        return client

    async def balance(self):
        client = await self.client()
        decimals = await client.functions.decimals()
        return await client.functions.balanceOf(self.public_key) / 10 ** decimals

    async def transaction(self, to, amount):
        client = await self.client()
        decimals = await client.functions.__getitem__("decimals").call()
        amount = amount * (10 ** (decimals))

        txn = await client.functions.__getitem__("transfer").call(to, amount)
        txn = txn.with_owner(self.public_key)
        txn = txn.fee_limit(30000000)
        txn = await txn.build()
        txn = txn.sign(self.private_key)
        txn = await txn.broadcast()
        txn = await txn.wait()
        return txn
        
