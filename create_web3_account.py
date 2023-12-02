from web3 import Web3, HTTPProvider
from eth_account import Account
from eth_utils import to_hex

binance_testnet_rpc_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(HTTPProvider(binance_testnet_rpc_url))


def create_eth_wallets():
    account1 = Account.create()
    account2 = web3.eth.account.create()
    private_key1 = to_hex(account1.key)
    private_key2 = to_hex(account2.key)

    print(f"Адрес кошелька 1: {account1.address}")
    print(f"Приватный ключ кошелька 1: {private_key1}")
    print(f"Адрес кошелька 2: {account2.address}")
    print(f"Приватный ключ кошелька 2: {private_key2}")


create_eth_wallets()
