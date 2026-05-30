from eth_utils import to_bytes


BASE_1E2 = 100


def parse_fee_data(extra_data_hex: str):
    # убираем 0x если есть
    extra_data_hex = extra_data_hex.removeprefix("0x")
    data = bytes.fromhex(extra_data_hex)

    if len(data) < 6:
        raise ValueError("extraData too short")

    # 2 bytes — integrator fee percentage (1e5)
    integrator_fee = int.from_bytes(data[0:2], "big")

    # 1 byte — integrator share percentage (1e2)
    integrator_share = data[2]
    if integrator_share > BASE_1E2:
        raise ValueError("InvalidIntegratorShare")

    # 2 bytes — resolver fee percentage (1e5)
    resolver_fee = int.from_bytes(data[3:5], "big")

    # 1 byte — whitelist discount numerator (1e2)
    whitelist_discount_numerator = data[5]
    if whitelist_discount_numerator > BASE_1E2:
        raise ValueError("InvalidWhitelistDiscountNumerator")

    # tail = extraData[6:]
    tail = data[6:]

    return {
        "integrator_fee": integrator_fee,
        "integrator_share": integrator_share,
        "resolver_fee": resolver_fee,
        "whitelist_discount_numerator": whitelist_discount_numerator,
        "tail_hex": tail.hex(),
    }


extra_data = "0x00000000326406b09498030ae3416b66dc74db31d09524fa87b1f76ea9a11ae13b29f5c555d18bd45f0b94f54a968fc90ed87a54c23dc480b395770895ad27ad6b0d95"

parsed = parse_fee_data(extra_data)

for k, v in parsed.items():
    print(f"{k}: {v}")