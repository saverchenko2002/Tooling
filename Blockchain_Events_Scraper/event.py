POOL_INITIALIZED_EVENT_ABI = [
    "bytes32",
    "tuple(address, address, bytes32)",
    "int32",
    "uint96"
]

POOL_INITIALIZED_EVENT = [
    {
        "anonymous": False,
        "type": "event",
        "name": "PoolInitialized",
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "poolId",
                "type": "bytes32",
            },
            {
                "indexed": False,
                "internalType": "tuple",
                "name": "poolKey",
                "components": [
                    {
                        "internalType": "address",
                        "name": "token0",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "token1",
                        "type": "address",
                    },
                    {
                        "internalType": "bytes32",
                        "name": "config",
                        "type": "bytes32",
                    },
                ],
            },
            {
                "indexed": False,
                "internalType": "int32",
                "name": "tick",
                "type": "int32",
            },
            {
                "indexed": False,
                "internalType": "uint96",
                "name": "sqrtRatio",
                "type": "uint96",
            },
        ],
    }
]