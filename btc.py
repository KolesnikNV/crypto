import time

from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
import json
from bit import PrivateKeyTestnet as Key

ENTROPY: str = generate_entropy()
DEFAULT_FEE_FAST = 72
DEFAULT_FEE_HOUR = 62


#
# def generate_wallet_btc() -> json:
#     hdwallet: HDWallet = HDWallet(symbol="BTC", use_default_path=False)
#     hdwallet.from_entropy(entropy=ENTROPY)
#     hdwallet.from_index(44, hardened=True)
#     hdwallet.from_index(0, hardened=True)
#     hdwallet.from_index(0, hardened=True)
#     hdwallet.from_index(0)
#     hdwallet.from_index(0)
#     print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))
#     return hdwallet.dumps()
#
#
def move_money(source_k: Key, dest_k: Key, value: float, fee: int = 40):
    print(f"Send from {source_k.address} to {dest_k.address}")
    # time.sleep(10)
    # source_k.send([(dest_k.address, value, "btc")], fee=fee)
    # print(f"Разница {balance_now} USD")
    # print(source_k.get_balance("usd"))
    # print(dest_k.get_balance("usd"))


#
#
source_k = Key("L4zGoWDsUbHg9pZaXD3zQV5dfotSTChVHYE2DCyaDfMVxjtfqogB")
dest_k = Key("cP2Z27v1ZaBz3VQRRSTQRhgYt2x8BtcmAL9zi2JsKaDBHobxj5rx")
# move_money(
#     source_k,
#     dest_k,
#     0.001,
# )

# generate_wallet_btc()
import requests


def get_bitcoin_fee():
    url = "https://mempool.space/api/v1/fees/recommended"

    try:
        response = requests.get(url)
        data = response.json()

        fastest_fee = data["fastestFee"]
        half_hour_fee = data["halfHourFee"]
        hour_fee = data["hourFee"]

        print(f"Fastest Fee: {fastest_fee} sat/byte")
        print(f"Half Hour Fee: {half_hour_fee} sat/byte")
        print(f"Hour Fee: {hour_fee} sat/byte")

        return fastest_fee, half_hour_fee, hour_fee

    except Exception as e:
        print(f"Error getting Bitcoin fees: {e}")
        return None


bitcoin_fees = get_bitcoin_fee()
