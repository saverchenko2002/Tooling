import os
import time
from dotenv import load_dotenv
from web3 import Web3
from eth_utils import keccak

load_dotenv(override=True)

RPC_URL = os.getenv("RPC_URL")

if not RPC_URL:
    raise ValueError("RPC_URL missing in .env")

w3 = Web3(Web3.HTTPProvider(RPC_URL))



# =====================================================
# CONFIG
# =====================================================

POOL_MANAGER = Web3.to_checksum_address(
    "0x000000000004444c5dc75cB358380D2e3dE08A90"
)

FROM_BLOCK = 21688329

TO_BLOCK = w3.eth.block_number
BATCH_SIZE = 10_000

WETH = Web3.to_checksum_address(
    "0xC02aaA39b223FE8D0A0E5C4F27eAD9083C756Cc2"
)

USDT = Web3.to_checksum_address(
    "0xdAC17F958D2ee523a2206206994597C13D831ec7"
)

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

# sorted pair (same as PoolKey ordering)
TARGET_PAIR = tuple(sorted(
    [WETH, USDT],
    key=lambda x: int(x, 16)
))

# =====================================================
# EVENT
# =====================================================

EVENT_SIGNATURE = (
    "Initialize(bytes32,address,address,uint24,int24,address,uint160,int24)"
)

TOPIC0 = "0x" + keccak(
    text=EVENT_SIGNATURE
).hex()

DYNAMIC_FEE_FLAG = 0x800000

# =====================================================
# HELPERS
# =====================================================

def is_dynamic_fee(fee: int) -> bool:
    return (fee & DYNAMIC_FEE_FLAG) != 0


def clean_fee(fee: int) -> int:
    return fee & 0x7FFFFF


existing_configs = set()

current_from = FROM_BLOCK

# =====================================================
# SCAN
# =====================================================

while current_from <= TO_BLOCK:
    current_to = min(
        current_from + BATCH_SIZE - 1,
        TO_BLOCK
    )

    print(
        f"Scanning {current_from} -> {current_to}"
    )

    try:
        logs = w3.eth.get_logs({
            "fromBlock": current_from,
            "toBlock": current_to,
            "address": POOL_MANAGER,
            "topics": [TOPIC0]
        })

        for log in logs:
            topics = log["topics"]
            data = log["data"].hex()

            # indexed currencies
            token0 = Web3.to_checksum_address(
                "0x" + topics[2].hex()[-40:]
            )

            token1 = Web3.to_checksum_address(
                "0x" + topics[3].hex()[-40:]
            )

            pair = tuple(sorted(
                [token0, token1],
                key=lambda x: int(x, 16)
            ))

            if pair != TARGET_PAIR:
                continue

            fee_raw = int(data[0:64], 16)

            tick_spacing_raw = int(
                data[64:128],
                16
            )

            # signed int24
            if tick_spacing_raw >= 2**255:
                tick_spacing_raw -= 2**256

            hooks = Web3.to_checksum_address(
                "0x" + data[128 + 24:192]
            )

            # only hook=0
            if hooks != ZERO_ADDRESS:
                continue

            fee = clean_fee(fee_raw)

            dynamic = is_dynamic_fee(fee_raw)

            config = (
                fee,
                tick_spacing_raw,
                dynamic
            )

            existing_configs.add(config)

            print(
                f"FOUND | "
                f"fee={fee} "
                f"tick={tick_spacing_raw} "
                f"dynamic={dynamic}"
            )

        current_from = current_to + 1
        time.sleep(0.2)

    except Exception as e:
        print(f"ERROR: {e}")
        time.sleep(3)

# =====================================================
# RESULT
# =====================================================

print("\n==============================")
print("EXISTING CONFIGS")
print("==============================")

existing_fees = set()

for fee, tick, dynamic in sorted(existing_configs):
    existing_fees.add(fee)

    print(
        f"fee={fee:<8} "
        f"tickSpacing={tick:<6} "
        f"dynamic={dynamic}"
    )

print("\n==============================")
print("USED FEES")
print("==============================")

print(sorted(existing_fees))

# common fee candidates
candidate_fees = [
    1,
    5,
    10,
    30,
    50,
    100,
    200,
    300,
    500,
    1000,
    2500,
    3000,
    5000,
    10000
]

missing = sorted(
    set(candidate_fees)
    - existing_fees
)

print("\n==============================")
print("NOT YET INITIALIZED")
print("==============================")

print(missing)