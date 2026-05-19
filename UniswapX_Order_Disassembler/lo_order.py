from eth_abi import decode
from eth_utils import to_checksum_address
import datetime
import json

RAW_HEX = "00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000120000000000000000000000000000000000000000000000000000000006856bb8e000000000000000000000000000000000000000000000000000000006856bb8e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002bb84fd8f7ed0ffae3da36ad60d4d7840bdeeada000000000000000000000000000000000000000000000085eef8db77de713661000000000000000000000000000000000000000000000085eef8db77de71366100000000000000000000000000000000000000000000000000000000000002000000000000000000000000006000da47483062a0d734ba3dc7576ce6a0b645c400000000000000000000000090524b9f43d8ec8c7f14f831de7493116ee6348204683287e9fa3bfbc9ba3937649c45198e8d83987ea71afe820a1b0d2acfe406000000000000000000000000000000000000000000000000000000006a37ef0e000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000086af913629d6a60000000000000000000000000000000000000000000000000086af913629d6a600000000000000000000000090524b9f43d8ec8c7f14f831de7493116ee63482"

data = bytes.fromhex(
    RAW_HEX[2:] if RAW_HEX.startswith("0x") else RAW_HEX
)


def ts(x):
    try:
        return datetime.datetime.utcfromtimestamp(x).strftime(
            "%Y-%m-%d %H:%M:%S UTC"
        )
    except Exception:
        return "invalid"


def pretty(obj):
    print(json.dumps(obj, indent=2))


# ============================================================
# ABI TYPE
# ExclusiveDutchOrder
# ============================================================
abi_type = [
    "(\
(address,address,uint256,uint256,address,bytes),\
uint256,\
uint256,\
address,\
uint256,\
(address,uint256,uint256),\
(address,uint256,uint256,address)[]\
)"
]


decoded = decode(abi_type, data)[0]

# ============================================================
# OrderInfo
# ============================================================
order_info = decoded[0]

order_info_parsed = {
    "reactor": to_checksum_address(order_info[0]),
    "swapper": to_checksum_address(order_info[1]),
    "nonce": order_info[2],
    "deadline": {
        "raw": order_info[3],
        "human": ts(order_info[3])
    },
    "additionalValidationContract": to_checksum_address(
        order_info[4]
    ),
    "additionalValidationData": (
        "0x" + order_info[5].hex()
        if order_info[5]
        else "0x"
    ),
    "additionalValidationData_len": len(order_info[5]),
}

# ============================================================
# Decay params
# ============================================================
decay_start_time = decoded[1]
decay_end_time = decoded[2]

decay_parsed = {
    "decayStartTime": {
        "raw": decay_start_time,
        "human": ts(decay_start_time)
    },
    "decayEndTime": {
        "raw": decay_end_time,
        "human": ts(decay_end_time)
    }
}

# ============================================================
# Exclusive filler
# ============================================================
exclusive_filler = to_checksum_address(decoded[3])

# ============================================================
# Exclusivity override
# ============================================================
exclusivity_override_bps = decoded[4]

exclusivity_parsed = {
    "bps": exclusivity_override_bps,
    "percent": exclusivity_override_bps / 100
}

# ============================================================
# DutchInput
# ============================================================
base_input = decoded[5]

base_input_parsed = {
    "token": to_checksum_address(base_input[0]),
    "startAmount": base_input[1],
    "endAmount": base_input[2]
}

# ============================================================
# DutchOutputs[]
# ============================================================
outputs_raw = decoded[6]

outputs_parsed = []

for o in outputs_raw:
    outputs_parsed.append({
        "token": to_checksum_address(o[0]),
        "startAmount": o[1],
        "endAmount": o[2],
        "recipient": to_checksum_address(o[3])
    })

# ============================================================
# Final object
# ============================================================
result = {
    "orderInfo": order_info_parsed,
    "decay": decay_parsed,
    "exclusiveFiller": exclusive_filler,
    "exclusivityOverride": exclusivity_parsed,
    "input": base_input_parsed,
    "outputs": outputs_parsed
}

# ============================================================
# PRINT
# ============================================================
pretty(result)