from bit.exceptions import InsufficientFunds
from bit import PrivateKeyTestnet as Key


def move_money(source_k: Key, dest_k: Key, value: float, fee: int = 1):
    print(
        f"Баланс отправителя до транзакции: {source_k.get_balance('usd')}, {source_k.address}"
    )
    print(f"Баланс получателя до транзакции: {dest_k.get_balance('usd')}")
    unspents = source_k.get_unspents()
    print("Непотраченные выходы отправителя:", unspents)

    source_k.create_transaction([(dest_k.address, value, "btc")], fee=fee)

    print(
        f"Транзакция отправлена с адреса {source_k.address} на адрес {dest_k.address}"
    )
    print(f"Баланс отправителя после транзакции: {source_k.get_balance('usd')}")
    print(f"Баланс получателя после транзакции: {dest_k.get_balance('usd')}")


# Замените адреса на свои фактические адреса
source_k = Key("L4zGoWDsUbHg9pZaXD3zQV5dfotSTChVHYE2DCyaDfMVxjtfqogB")
dest_k = Key("cP2Z27v1ZaBz3VQRRSTQRhgYt2x8BtcmAL9zi2JsKaDBHobxj5rx")

move_money(source_k, dest_k, 0.0001)
