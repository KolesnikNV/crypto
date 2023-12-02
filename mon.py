from web3 import Web3, EthereumTesterProvider
from eth_account import Account

infura_url = "https://goerli.infura.io/v3/bab09561236b40d481215a2d4d529d04"
w3 = Web3(EthereumTesterProvider())


def create_eth_wallets():
    account1 = Account.create()
    print(f"Адрес кошелька 1: {account1.address}")
    print(f"Закрытый ключ кошелька 1: {account1.key}")
    account2 = Account.create()
    print(f"Адрес кошелька 2: {account2.address}")
    print(f"Закрытый ключ кошелька 2: {account2.key}")
    return account1, account2


def create_transaction():
    account1, account2 = create_eth_wallets()
    transaction = {
        "from": "0xE872F8731acb89197D0CbcF6F2389eEe748F1a81",
        "to": "0x7ddc24EcAcF0f37D83b69462AAD67632A17deB9C",
        "value": 1,
        "gas": 100_000,
        "gasPrice": w3.eth.gas_price,
        "nonce": w3.eth.get_transaction_count(
            "0xeaa8Dd26A8B11C605a64153f1D64735aC9367064"
        ),
    }
    nonce = w3.eth.get_transaction_count("0xeaa8Dd26A8B11C605a64153f1D64735aC9367064")
    print(nonce)
    # Подписываем транзакцию
    signed_transaction = w3.eth.account.sign_transaction(
        transaction,
        "0x4e91cd852741c2499b8923fcaaf152886cc7b1579a9ce632cb944a579c69eed7",
    )
    # Отправляем транзакцию
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    print(f"Транзакция отправлена. Хэш транзакции: {transaction_hash}")
    txn_receipt = w3.eth.get_transaction_receipt(transaction_hash)
    print(txn_receipt)


create_eth_wallets()
# create_transaction()
# Адрес кошелька 1: 0xE872F8731acb89197D0CbcF6F2389eEe748F1a81
# Закрытый ключ кошелька 1: b'\xc1\xef\xa7M\xd3CV\xe3\xd0\xc5\x1b\xaf@\n\x06\xf9T\x891\xfc\x03C\xf6\x7ft\xf2\xbe\x9f\xc6\xc5\xa8\x82'
# Адрес кошелька 2: 0x7ddc24EcAcF0f37D83b69462AAD67632A17deB9C
# Закрытый ключ кошелька 2: b'\x1a\xd8\xe0\xd2\x0c(\xbf\xe1\xa1~P\xab\xeb\x19(\x1bN\xbe\xec\xb6I!\xe1\x93\x7f\xb9q;\xd0}62'
