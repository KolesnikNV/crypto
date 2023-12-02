import requests
import pprint as pp

#
#
# url = "https://nile.trongrid.io/wallet/getaccount"
#
# payload = {"address": "TKGYUuHcuadUWvBbudaPv8ukzzSkpymhwU", "visible": True}
# headers = {"accept": "application/json", "content-type": "application/json"}
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.text)
# print(response.status_code)
# TKGYUuHcuadUWvBbudaPv8ukzzSkpymhwU


url = "https://nile.trongrid.io/wallet/createtransaction"

payload = {
    "owner_address": "TRJgg73CBerUMTCRuU4eeV2qQuy3dZfwZ2",
    "to_address": "TJTFWBYs54nqrDewmCF6mDKFobsmrjJAAP",
    "amount": 2000,
    "visible": True,
}
headers = {"accept": "application/json", "content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

pp.pp(response.json())
