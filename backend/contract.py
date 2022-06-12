from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
import json
from dotenv import load_dotenv
import os
load_dotenv()

w3 = Web3(Web3.HTTPProvider(
    "https://speedy-nodes-nyc.moralis.io/accc41150589d35dd52f06ea/avalanche/testnet"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


abi = json.loads("""[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "GLN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GTIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GSIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SSCC",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "w_id",
				"type": "uint256"
			}
		],
		"name": "addUnitInfo",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			}
		],
		"name": "Addworker",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			}
		],
		"name": "get_unit",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "GLN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "GTIN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "GSIN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SSCC",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "data",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "worker_id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					}
				],
				"internalType": "struct Supplychain.Unit",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "GTIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SN",
				"type": "string"
			}
		],
		"name": "history",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "GLN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "GTIN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "GSIN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SSCC",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "data",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "worker_id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					}
				],
				"internalType": "struct Supplychain.Unit[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "historyAll",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "GLN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "GTIN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "GSIN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SSCC",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "SN",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "data",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "worker_id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					}
				],
				"internalType": "struct Supplychain.Unit[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "particularunit",
		"outputs": [
			{
				"internalType": "string",
				"name": "GLN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GTIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GSIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SSCC",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "worker_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "UnitInfo",
		"outputs": [
			{
				"internalType": "string",
				"name": "GLN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GTIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GSIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SSCC",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "worker_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "units",
		"outputs": [
			{
				"internalType": "string",
				"name": "GLN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GTIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GSIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SSCC",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "worker_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "units_list",
		"outputs": [
			{
				"internalType": "string",
				"name": "GLN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GTIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "GSIN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SSCC",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "SN",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "worker_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "WorkerInfo",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "workers",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "workers_list",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "workersInfo",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					}
				],
				"internalType": "struct Supplychain.Worker[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]""")

#key = os.getenv("RINKEBY_KEY")
key = "3601d0875a0ff4fd45ca1e7f8d75f68ffb5adbecb23d8a33ea55a2c47c9eb3f0"
print(key)  # private key account
account = w3.toChecksumAddress(
    '0x6a92c4f51f4F036230116Ca01332867D82583644')  # account

address = w3.toChecksumAddress('0xb8f91d0C5cc906855f56E91232c655bE06c2dD4a')
# '0xFa56954976bA7d616945c09A7e360499e7038d98')  # contrat address
deployed_contract = w3.eth.contract(address=address, abi=abi)

# print(deployed_contract.functions.getWorkerssList().call())


def Addworker(name):
    transaction = deployed_contract.functions.Addwork(
        name).buildTransaction({'from': account})
    transaction.update({'nonce': w3.eth.get_transaction_count(account)})
    signed_tx = w3.eth.account.sign_transaction(transaction, key)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(txn_receipt)
    return "worker added"


def addUnitInfo(GLN,GTIN,GSIN,SSCC,SN,name,data,w_id):
    transaction = deployed_contract.functions.addUnitInfo(GLN,GTIN,GSIN,SSCC,SN,name,data,w_id).buildTransaction({'from': account})
    transaction.update({'nonce': w3.eth.get_transaction_count(account)})
    signed_tx = w3.eth.account.sign_transaction(transaction, key)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(txn_receipt)
    return "product added"


def get_unit(id):
    return deployed_contract.functions.get_unit(id).call()


def workersInfo():
    return deployed_contract.functions.workersInfo().call()


def historyAll():
    return deployed_contract.functions.historyAll().call()


def history(GTIN,SN):
    return deployed_contract.functions.history(GTIN,SN).call()
