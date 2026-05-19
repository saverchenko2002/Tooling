from eth_abi import decode
from eth_utils import to_checksum_address
import datetime
import json

RAW_HEX = "000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000001000000000000000000000000004449cd34d1eb1fedcf02a1be3834ffde8e6a6180000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec7000000000000000000000000000000000000000000000000000000090ce1e605000000000000000000000000000000000000000000000000000000090e0a759f00000000000000000000000000000000000000000000000000000000000001e00000000000000000000000000000000000000000000000000000000000000280000000000000000000000000000000000000000000000000000000000000038000000000000000000000000000000011f84b9aa48e5f8aa8b9897600006289be000000000000000000000000e77aa058febc085fcdb05e792ace2911f4c0416b046832af7707012801bf8e21a7e6987fb807dfdf69ca034c77f8ec15bfc1990c000000000000000000000000000000000000000000000000000000006a05d65d000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000eef9bac3b83a0000000000000000000000000000000000000000000000000000eef9bac3b83a0000000000000000000000000000e77aa058febc085fcdb05e792ace2911f4c0416b000000000000000000000000000000000000000000000000000000006a05d558000000000000000000000000000000000000000000000000000000006a05d594000000000000000000000000225a38bc71102999dd13478bfabd7c4d53f2dc1700000000000000000000000000000000000000000000000000000000000000640000000000000000000000000000000000000000000000000000000908f6b56700000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004171b05770315051e74c872d0afbf4616efce4f1a7bcbac1756544cebdc933d7484fff9084fa2162d146bc974be628e7c3db3749b737c7a26943ab0d9dde8da88f1c00000000000000000000000000000000000000000000000000000000000000"

data = bytes.fromhex(RAW_HEX)


def ts(x):
    try:
        return datetime.datetime.utcfromtimestamp(x).strftime("%Y-%m-%d %H:%M:%S UTC")
    except:
        return "invalid"


def pretty(obj):
    print(json.dumps(obj, indent=2))


# ABI тип
abi_type = [
    "(\
(address,address,uint256,uint256,address,bytes),\
address,\
(address,uint256,uint256),\
(address,uint256,uint256,address)[],\
(uint256,uint256,address,uint256,uint256,uint256[]),\
bytes\
)"
]


decoded = decode(abi_type, data)[0]

# -------------------------
# OrderInfo
# -------------------------
order_info = decoded[0]

order_info_parsed = {
    "reactor": to_checksum_address(order_info[0]),
    "swapper": to_checksum_address(order_info[1]),
    "nonce": order_info[2],
    "deadline": {
        "raw": order_info[3],
        "human": ts(order_info[3])
    },
    "additionalValidationContract": to_checksum_address(order_info[4]),
    "additionalValidationData_len": len(order_info[5])
}

# -------------------------
# Cosigner
# -------------------------
cosigner = to_checksum_address(decoded[1])

# -------------------------
# DutchInput
# -------------------------
base_input = decoded[2]

base_input_parsed = {
    "token": to_checksum_address(base_input[0]),
    "startAmount": base_input[1],
    "endAmount": base_input[2]
}

# -------------------------
# DutchOutputs[]
# -------------------------
outputs_raw = decoded[3]

outputs_parsed = []
for o in outputs_raw:
    outputs_parsed.append({
        "token": to_checksum_address(o[0]),
        "startAmount": o[1],
        "endAmount": o[2],
        "recipient": to_checksum_address(o[3])
    })

# -------------------------
# CosignerData
# -------------------------
cosigner_data = decoded[4]

cosigner_data_parsed = {
    "decayStartTime": {
        "raw": cosigner_data[0],
        "human": ts(cosigner_data[0])
    },
    "decayEndTime": {
        "raw": cosigner_data[1],
        "human": ts(cosigner_data[1])
    },
    "exclusiveFiller": to_checksum_address(cosigner_data[2]),
    "exclusivityOverrideBps": cosigner_data[3],
    "exclusivityOverridePercent": cosigner_data[3] / 100,
    "inputAmount": cosigner_data[4],
    "outputAmounts": cosigner_data[5]
}

# -------------------------
# Signature
# -------------------------
cosignature = decoded[5]

# -------------------------
# Final object
# -------------------------
result = {
    "orderInfo": order_info_parsed,
    "cosigner": cosigner,
    "baseInput": base_input_parsed,
    "baseOutputs": outputs_parsed,
    "cosignerData": cosigner_data_parsed,
    "cosignature": {
        "length": len(cosignature),
        "hex_preview": cosignature.hex()[:64] + "..."
    }
}

# -------------------------
# PRINT
# -------------------------
pretty(result)