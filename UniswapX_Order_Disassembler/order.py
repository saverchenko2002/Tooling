from eth_abi import decode
from eth_utils import to_checksum_address
import datetime
import json

RAW_HEX = "000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000001000000000000000000000000004449cd34d1eb1fedcf02a1be3834ffde8e6a6180000000000000000000000000f19304e6bfe0a18d2a0171758aa433921f1928970000000000000000000000000000000000000000000004583064b47fa3304e150000000000000000000000000000000000000000000004583064b47fa3304e1500000000000000000000000000000000000000000000000000000000000001e00000000000000000000000000000000000000000000000000000000000000280000000000000000000000000000000000000000000000000000000000000038000000000000000000000000000000011f84b9aa48e5f8aa8b9897600006289be000000000000000000000000f89a5b7b532b52b1019955976ec23fa2f301ebc6046832b38ac621c4dbbffa48e3a992f21c87a52230c2f68977cbd82b7a5036010000000000000000000000000000000000000000000000000000000069ddb955000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000374ffd5e391fffb000000000000000000000000000000000000000000000000037093094cac2661000000000000000000000000f89a5b7b532b52b1019955976ec23fa2f301ebc60000000000000000000000000000000000000000000000000000000069ddb84a0000000000000000000000000000000000000000000000000000000069ddb8860000000000000000000000008392876883cf0e9e7ee24d9b1f606ed88644f23b0000000000000000000000000000000000000000000000000000000000000064000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000037736f0fbaab8b600000000000000000000000000000000000000000000000000000000000000416f10394cbaebd3d5e1347b978bac14db08057f075d107c25a6ae02661d42d1de339b5f151632ba7097cbe56915df00e6b36d44dedf883b43fb0abdbbc391c77e1c00000000000000000000000000000000000000000000000000000000000000"

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