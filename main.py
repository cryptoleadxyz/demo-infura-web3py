# Author: CryptoLead at https://www.cryptolead.xyz
# Date: 2023-03-14

import os
from datetime import date, datetime
from dotenv import load_dotenv
from web3 import Web3

# Access Infura API key
load_dotenv()
infura_prefix = "https://mainnet.infura.io/v3/"
infura_key = infura_prefix + os.getenv("INFURA_KEY")

# Instantiate and check the Web3 connection
web3 = Web3(Web3.HTTPProvider(infura_key))
print("Successfully connected to Web3?", web3.isConnected())


# 1) Extract information on a public wallet address
public_address_checksum = (
    "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"  # Vitalik Buterin - checksum version
)
public_address_nonchecksum = Web3.toChecksumAddress(
    "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
)  # Vitalik Buterin - non-checksum version
public_address_ens = web3.ens.address("vitalik.eth")  # Vitalik Buterin - ENS version
balance1 = web3.eth.getBalance(public_address_checksum)
balance2 = web3.eth.getBalance(public_address_nonchecksum)
balance3 = web3.eth.getBalance(public_address_ens)
print("Vitalik wallet balance in ETH:", web3.fromWei(balance1, "ether"))
print("Vitalik wallet balance in ETH:", web3.fromWei(balance2, "ether"))
print("Vitalik wallet balance in ETH:", web3.fromWei(balance3, "ether"))
print("/////")

# 2) Extract Ethereum block information
# Get the hash of a transaction by its index in a specific block
block_number = 10000000
tx_index = 0
tx_hash = web3.eth.get_transaction_by_block(block_number, tx_index).hash
print(f"The hash of transaction {tx_index} in block {block_number} is {tx_hash}")
# Get the receipt hash of a transaction
tx_hash = "0xd753f5a381e10e89651efd02558bd60e6e48b352e576912440ae7a06a3382de8"  # Uniswap transaction
receipt = web3.eth.get_transaction_receipt(tx_hash)
print(f"The receipt of transaction {tx_hash} is {receipt}")
# Get the gas price for the next transaction
gas_price = web3.eth.gas_price
print(f"The gas price for the next transaction is {gas_price}")
# Get the current Ethereum network ID:
network_id = web3.eth.chain_id
print(f"The current Ethereum network ID is {network_id}")
# Get the latest block number
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
latest_block_number = web3.eth.block_number
print(
    f"The latest block number: {latest_block_number} on {date.today()} at {current_time}"
)
# Get the latest block timestamp:
latest_block_timestamp = web3.eth.get_block("latest").timestamp
print(f"The timestamp of the latest block is {latest_block_timestamp}")
print("/////")

# 3) Extract information from a deployed smart contract
cryptopunks_contract_address = "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB"
cryptopunks_contract_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"punksOfferedForSale","outputs":[{"name":"isForSale","type":"bool"},{"name":"punkIndex","type":"uint256"},{"name":"seller","type":"address"},{"name":"minValue","type":"uint256"},{"name":"onlySellTo","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"enterBidForPunk","outputs":[],"payable":true,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"},{"name":"minPrice","type":"uint256"}],"name":"acceptBidForPunk","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"addresses","type":"address[]"},{"name":"indices","type":"uint256[]"}],"name":"setInitialOwners","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"withdraw","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"imageHash","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"nextPunkIndexToAssign","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"punkIndexToAddress","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"standard","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"punkBids","outputs":[{"name":"hasBid","type":"bool"},{"name":"punkIndex","type":"uint256"},{"name":"bidder","type":"address"},{"name":"value","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"allInitialOwnersAssigned","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"allPunksAssigned","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"buyPunk","outputs":[],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"punkIndex","type":"uint256"}],"name":"transferPunk","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"withdrawBidForPunk","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"punkIndex","type":"uint256"}],"name":"setInitialOwner","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"},{"name":"minSalePriceInWei","type":"uint256"},{"name":"toAddress","type":"address"}],"name":"offerPunkForSaleToAddress","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"punksRemainingToAssign","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"},{"name":"minSalePriceInWei","type":"uint256"}],"name":"offerPunkForSale","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"getPunk","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"pendingWithdrawals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"punkIndex","type":"uint256"}],"name":"punkNoLongerForSale","outputs":[],"payable":false,"type":"function"},{"inputs":[],"payable":true,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"punkIndex","type":"uint256"}],"name":"Assign","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"punkIndex","type":"uint256"}],"name":"PunkTransfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"},{"indexed":false,"name":"minValue","type":"uint256"},{"indexed":true,"name":"toAddress","type":"address"}],"name":"PunkOffered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":true,"name":"fromAddress","type":"address"}],"name":"PunkBidEntered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":true,"name":"fromAddress","type":"address"}],"name":"PunkBidWithdrawn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":true,"name":"fromAddress","type":"address"},{"indexed":true,"name":"toAddress","type":"address"}],"name":"PunkBought","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"punkIndex","type":"uint256"}],"name":"PunkNoLongerForSale","type":"event"}]'
contract = web3.eth.contract(
    address=cryptopunks_contract_address, abi=cryptopunks_contract_abi
)
# Call functions from the ABI
name = contract.functions.name().call()
symbol = contract.functions.symbol().call()
total_supply = contract.functions.totalSupply().call()
print(f"Collection name: {name}")
print(f"Collection symbol: {symbol}")
print(f"Total supply: {total_supply}")
# Listen to the latest 5 blocks' "Assign" events from the Cryptopunks smart contract
assign_event_name = "Assign"
event_filter = contract.events[assign_event_name].createFilter(
    fromBlock=0, toBlock="latest"
)  # define the event name and filter parameters
events = event_filter.get_all_entries()  # get all the events
events = events[-5:]  # get only the last x events
for event in events:
    print(events)
