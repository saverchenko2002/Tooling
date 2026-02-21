import os
from dotenv import load_dotenv
from web3 import Web3
from eth_utils import keccak
import time

load_dotenv(override=True)

RPC_URL = os.getenv("RPC_URL")

w3 = Web3(Web3.HTTPProvider(RPC_URL))

BATCH_NUMBER = 10000

FROM_BLOCK = 22047273
TO_BLOCK = 	24495999

# https://docs.ekubo.org/integration-guides/reference/evm-contracts-v2
CONTRACT_ADDRESS = Web3.to_checksum_address("0xe0e0e08A6A4b9Dc7bD67BCB7aadE5cF48157d444")

EVENT_SIGNATURE = "PoolInitialized(bytes32,(address,address,bytes32),int32,uint96)"
topic0 = "0x" + keccak(text=EVENT_SIGNATURE).hex()

ETH_ADDRESS = Web3.to_checksum_address("0x0000000000000000000000000000000000000000")
USDC_ADDRESS = Web3.to_checksum_address("0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")
TARGET_CONFIG = "0xd4279c050da1f5c5b2830558c7a08e57e12b54ec0020c49ba5e353f700000000"

if int(ETH_ADDRESS, 16) < int(USDC_ADDRESS, 16):
    token_pair = (ETH_ADDRESS, USDC_ADDRESS)
else:
    token_pair = (USDC_ADDRESS, ETH_ADDRESS)

current_from = FROM_BLOCK

found = False

with open("matched_transactions.txt", "a") as f:

    while (current_from <= TO_BLOCK and not found):
        current_to = min(current_from + BATCH_NUMBER - 1, TO_BLOCK)

        filter_params = {
            "fromBlock": current_from,
            "toBlock": current_to,
            "address": CONTRACT_ADDRESS,
            "topics": [topic0],
        }

        logs = w3.eth.get_logs(filter_params)

        for log in logs:
            data =  log["data"]

            token0 = Web3.to_checksum_address(data[32+12:64])
            token1 = Web3.to_checksum_address(data[64+12:96])
            config = "0x" + data[96:128].hex()

            log_pair = tuple(sorted([Web3.to_checksum_address(token0),
                                     Web3.to_checksum_address(token1)],
                                    key=lambda x: int(x, 16)))
            

            if log_pair == token_pair and config == TARGET_CONFIG:
                f.write(log["transactionHash"].hex() + "\n")
                print(f"Found matching transaction: {log['transactionHash'].hex()}")
                found = True
                break

        current_from = current_to + 1
        print(f"Processed up to block {current_to}. Sleeping for 1 second...")
        time.sleep(1)
