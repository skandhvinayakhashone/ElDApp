
import sys
import json
from web3 import Web3

# Set up web3 connection with Geth instance
geth_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(geth_url))

# Set a default account to sign transactions
web3.eth.defaultAccount = web3.eth.accounts[0]

# contract ABI
abi=""
with open("abi.json") as file:
abi = json.loads(file)

# contract address
address = web3.toChecksumAddress('0x78b3fd39a49eafe44504763e9b6999da0810de2c14469ac27b5e210aff59917a3')

# get contract from chain instance
contract = web3.eth.contract(address=address, abi=abi)

# Read the current usage
used = contract.functions.getUsage(web3.eth.defaultAccount).call()
new_used = int(sys.argv[1]) #latest used energy amount

total_energy = used + new_used # calculating total energy used

# Read the current bill amount
curr_bill = contract.functions.getBill(web3.eth.defaultAccount).call()
total_bill = 0

#bill calculations
if total_energy <= 100:
	total_bill = curr_bill + new_used*2.96
elif total_energy > 100 and total_energy <= 300:
	total_bill = curr_bill + new_used*5.56
elif total_energy > 300 and total_energy <= 500:
	total_bill = curr_bill + new_used*9.16
elif total_energy > 500:
	total_bill = curr_bill + new_used*10.61

#round up the values
total_energy = round(total_energy)
total_bill = round(total_bill)

# Set the new values
tx_hash = contract.functions.setDebt(total_energy,total_bill,web3.eth.defaultAccount).transact()

# Wait for transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)

