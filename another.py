from tronpy import Tron, Contract
from tronpy.keys import PrivateKey
from abis import abi
from tronpy.providers import HTTPProvider

# HTTPProvider('https://api.shasta.trongrid.io')
# HTTPProvider(api_key="013b8092-175d-4148-b034-caa4c908a44a")
# client = Tron(HTTPProvider("https://nile.trongrid.io"))
# Wallet address:  TRJgg73CBerUMTCRuU4eeV2qQuy3dZfwZ2
# Private Key:  381d657d1b4fef3c6ea4d1ed31458477073fb01f2ca7af636c996a4dfcd60678
# if network == "shasta":
#         return "TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs"
#     elif network == "nile":
#         return "TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf"
#     elif network == "mainnet":
#         return "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"

client = Tron(network="nile", conf={"fee_limit": 30_000_000})
contract_address = "TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3"
contract = client.get_contract(contract_address)
for f in contract.functions:
    print(f)
print(contract.functions.symbol())
print(contract.functions.balanceOf("TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj"))
balance = client.get_account_balance(str("TAALMsugkEi1aVidzeMnkiUjWgMR1VEh3H"))
print(balance)


def generate_wallet_usdt():
    wallet = client.generate_address()
    print("Wallet address:  %s" % wallet["base58check_address"])
    print("Private Key:  %s" % wallet["private_key"])
    print(wallet)


def transfer_usdt(from_address: str, to_address: str, amount: int, private_key: str):
    priv_key = PrivateKey(bytes.fromhex(private_key))
    owner_address = priv_key.public_key.to_address()

    transfer_txn = (
        contract.functions.transfer(to_address, amount)
        .memo("test memo")
        .fee_limit(10_000_000)
        .with_owner(owner_address)
        .build()
        .inspect()
        .sign(priv_key)
        .broadcast()
    )

    print(transfer_txn)
    print(transfer_txn.wait())


# def transfer_usdt(from_address: str, to_address: str, amount: int, private_key: str):
#     priv_key = PrivateKey(bytes.fromhex(private_key))
#     owner_address = priv_key.public_key.to_address()
#
#     transfer_txn = (
#         contract.functions.transferFrom(from_address, to_address, amount)
#         .memo("test memo")
#         .fee_limit(1_000_000)
#         .with_owner(owner_address)
#         .build()
#         .inspect()
#         .sign(priv_key)
#         .broadcast()
#     )
#
#     print(transfer_txn)
#     print(transfer_txn.wait())

# generate_wallet_usdt()
# #
transfer_usdt(
    "TAALMsugkEi1aVidzeMnkiUjWgMR1VEh3H",
    "TJTFWBYs54nqrDewmCF6mDKFobsmrjJAAP",
    3500000000000000000,
    "3ff9f78c5bd7d972196dd886470f38fe38903d87dc205dafd2d15f28163d1d07",
)


# Wallet address:  e
# Private Key:  308fd8e73d8a310d3d00aa53833a79fab9399f01a97187f16f7738585bd22498
# {'base58check_address': 'TAALMsugkEi1aVidzeMnkiUjWgMR1VEh3H',
# 'hex_address': '41021ab7f1774e47d098230d588a1893b0345cdac2',
# 'private_key': '308fd8e73d8a310d3d00aa53833a79fab9399f01a97187f16f7738585bd22498',
# 'public_key': '8a527d48c65e063a0764653b82440aa3bcf8fc407b37354ab19e805deadb3406004037b0685b5150c9c37f4bb737f93e14cc630d5f9020833d3e3220e607164a'}
