from web3 import Web3, Account
import json
from pprint import pprint

binance_testnet_rpc_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(binance_testnet_rpc_url))
wallet_address = "0x8d6B248F723fc19AF6e9394f7080afeC41f08a7A"
checksum_address = Web3.to_checksum_address(wallet_address)

balance = web3.eth.get_balance(checksum_address)
print(f"balance of {wallet_address}={balance}")
account = Account.create()
private_key = account.key
ERC20_ABI = json.loads(
    """[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_initialSupply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"decimals_","type":"uint8"}],"name":"setupDecimals","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]"""
)

# USDT токен
usdt_contract_address = "0xA11c8D9DC9b66E209Ef60F0C8D969D3CD988782c"

# инициализация USDT контракта
usdt_contract = web3.eth.contract(usdt_contract_address, abi=ERC20_ABI)

user_address = "0x8d6B248F723fc19AF6e9394f7080afeC41f08a7A"
someone_address = "0x698F00D64233F6FD0CC6F4Aea7A63621669feB33"

nonce = str(web3.eth.get_transaction_count(checksum_address))
dict_transaction = {
    "chainId": web3.eth.chain_id,
    "from": user_address,
    "gasPrice": web3.eth.gas_price,
    "nonce": web3.eth.get_transaction_count(
        "0x698F00D64233F6FD0CC6F4Aea7A63621669feB33"
    ),
}
usdt_decimals = usdt_contract.functions.decimals().call()
one_usdt = 1 * 10**usdt_decimals  # отправляем 1 USDT

# создаём транзакцию
transaction = usdt_contract.functions.transfer(
    someone_address, one_usdt
).buildTransaction(dict_transaction)
print(transaction)
# # подписываем
signed_txn = web3.eth.account.sign_transaction(
    transaction, "0xd5722a8cf20d7a656676f81b612ca82d7e9442379ae7d275e9c752fff4222673"
)
print(signed_txn)

txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(txn_hash.hex())

# Адрес кошелька 1: 0x8d6B248F723fc19AF6e9394f7080afeC41f08a7A
# Приватный ключ кошелька 1: 0xd5722a8cf20d7a656676f81b612ca82d7e9442379ae7d275e9c752fff4222673
# Адрес кошелька 2: 0x698F00D64233F6FD0CC6F4Aea7A63621669feB33
# Приватный ключ кошелька 2: 0x762c142fe867d747790b9f90e53d008106bf25a1b11cc3e8da0361d2f9baa5ef
# jVhfynCRBmgdnmgx3Z
# IhSVg5okgXhSD8aWRBxXONiR2U0LaSi6LIh5
