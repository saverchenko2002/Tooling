maker_traits = 33471150795161712739625987854073848363835857092057853625728090127334710968320
taker_traits = 57896063301902404314357746292922536297367813999492154336304622249516154782649
args_hex = "0x00000295000001e4000001e4000000f0000000f0000000780000000000000000399740157391a9f1bf4e9921a8834f9bc8f2678e00013f000000e469fc580900012c02e0cf0300c58b003c00c2f2009c00013f0054000000012c6406b09498030ae3416b66dc74db31d09524fa87b1f76ea9a11ae13b29f5c555d18bd45f0b94f54a968fc90ed87a54c23dc480b395770895ad27ad6b0d95399740157391a9f1bf4e9921a8834f9bc8f2678e00013f000000e469fc580900012c02e0cf0300c58b003c00c2f2009c00013f0054000000012c6406b09498030ae3416b66dc74db31d09524fa87b1f76ea9a11ae13b29f5c555d18bd45f0b94f54a968fc90ed87a54c23dc480b395770895ad27ad6b0d9557e114b691db790c35207b2e685d4a43181e6061000000000000000000000000746f313283d0b58a244c6e58612f91aa0dc5b129000000000000000000000000111111125421ca6dc452d289314280a0f8842a65ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000069fda8ff000000000000000000000000000000000000000000000000000000000000001b8a8935d84a75cf45320337248fcb0726885760078bd0156abf827debaffc3cbf5f1a8458ad94ef4c78832204d80628b7f66b145c09df67be97304df67a37929a399740157391a9f1bf4e9921a8834f9bc8f2678e00000000000000000000000000000000000000000090cbe4bdd538d6e9b379bff5fe72c3d67a521de5000000012c6469fc579106b09498030ae3416b66dc000074db31d09524fa87b1f700006ea9a11ae13b29f5c5550000d18bd45f0b94f54a968f0000c90ed87a54c23dc480b3000095770895ad27ad6b0d9500000000000000000000000000000000000000000000000000000000000c59dda25700beef02961503351625926ea9a11ae13b29f5c55520000000000000000000000000000000000000000000061577c549a9344e26c000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000048146b73e8011000000000000000000000000a0b86991c6218b36c1d19d4a2e9eb0ce3606eb4800000000000000000000000000000000000000000000000000000000cf1214d90000000000000000000000007a819fa46734a49d0112796f9377e024c350fb26000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000001e4baba5855000000000000000000000000000000000000000069fc57d363f30597771a3d0c000000000000000000000000a0b86991c6218b36c1d19d4a2e9eb0ce3606eb4800000000000000000000000057e114b691db790c35207b2e685d4a43181e6061000000000000000000000000bee3211ab312a8d065c4fef0247448e17a8da000000000000000000000000000beef02961503351625926ea9a11ae13b29f5c55500000000000000000000000000000000000000000000000000000000cf130ca900000000000000000000000000000000000000000000061577c549a9344e26ca0000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000061577c549a9344e26ca000000000000000000000000beef02961503351625926ea9a11ae13b29f5c55500000000000000000000000000000000000000000000000000000000000000413760dd0d8b9749302b2a2aa4bf923452b0b9e19072176af3c4b0e59d34a6c8922604ed922f2b158d688dbe8ee1800624cda369062a0821af102c2d4483fd056f1b0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

print("=" * 60)
print("MAKER TRAITS (из MakerTraitsLib)")
print("=" * 60)
print(f"Hex: 0x{maker_traits:064x}")
print(f"Dec: {maker_traits}")
print()

NO_PARTIAL_FILLS_FLAG = 1 << 255
ALLOW_MULTIPLE_FILLS_FLAG = 1 << 254
PRE_INTERACTION_CALL_FLAG = 1 << 252
POST_INTERACTION_CALL_FLAG = 1 << 251
NEED_CHECK_EPOCH_MANAGER_FLAG = 1 << 250
HAS_EXTENSION_FLAG = 1 << 249
USE_PERMIT2_FLAG = 1 << 248
UNWRAP_WETH_FLAG = 1 << 247

EXPIRATION_OFFSET = 80
EXPIRATION_MASK = (1 << 40) - 1
NONCE_OR_EPOCH_OFFSET = 120
NONCE_OR_EPOCH_MASK = (1 << 40) - 1
SERIES_OFFSET = 160
SERIES_MASK = (1 << 40) - 1
ALLOWED_SENDER_MASK = (1 << 80) - 1

print("ФЛАГИ MAKER:")
print(f"  HAS_EXTENSION:                 {'✅ ДА' if (maker_traits & HAS_EXTENSION_FLAG) != 0 else '❌ НЕТ'}")
print(f"  ALLOW_PARTIAL_FILLS:           {'✅ ДА' if (maker_traits & NO_PARTIAL_FILLS_FLAG) == 0 else '❌ НЕТ'}")
print(f"  ALLOW_MULTIPLE_FILLS:          {'✅ ДА' if (maker_traits & ALLOW_MULTIPLE_FILLS_FLAG) != 0 else '❌ НЕТ'}")
print(f"  NEED_PRE_INTERACTION_CALL:     {'✅ ДА' if (maker_traits & PRE_INTERACTION_CALL_FLAG) != 0 else '❌ НЕТ'}")
print(f"  NEED_POST_INTERACTION_CALL:    {'✅ ДА' if (maker_traits & POST_INTERACTION_CALL_FLAG) != 0 else '❌ НЕТ'}")
print(f"  NEED_CHECK_EPOCH_MANAGER:      {'✅ ДА' if (maker_traits & NEED_CHECK_EPOCH_MANAGER_FLAG) != 0 else '❌ НЕТ'}")
print(f"  USE_PERMIT2:                   {'✅ ДА' if (maker_traits & USE_PERMIT2_FLAG) != 0 else '❌ НЕТ'}")
print(f"  UNWRAP_WETH:                   {'✅ ДА' if (maker_traits & UNWRAP_WETH_FLAG) != 0 else '❌ НЕТ'}")

print()
print("ЗНАЧЕНИЯ MAKER:")
print(f"  Allowed Sender:  0x{(maker_traits & ALLOWED_SENDER_MASK):020x}")
print(f"  Expiration:      {(maker_traits >> EXPIRATION_OFFSET) & EXPIRATION_MASK}")
print(f"  Nonce/Epoch:     {(maker_traits >> NONCE_OR_EPOCH_OFFSET) & NONCE_OR_EPOCH_MASK}")
print(f"  Series:          {(maker_traits >> SERIES_OFFSET) & SERIES_MASK}")

print()
print("=" * 60)
print("TAKER TRAITS (из TakerTraitsLib)")
print("=" * 60)
print(f"Hex: 0x{taker_traits:064x}")
print(f"Dec: {taker_traits}")
print()

MAKER_AMOUNT_FLAG = 1 << 255
UNWRAP_WETH_FLAG_TAKER = 1 << 254
SKIP_ORDER_PERMIT_FLAG = 1 << 253
USE_PERMIT2_FLAG_TAKER = 1 << 252
ARGS_HAS_TARGET = 1 << 251

ARGS_EXTENSION_LENGTH_OFFSET = 224
ARGS_EXTENSION_LENGTH_MASK = 0xffffff
ARGS_INTERACTION_LENGTH_OFFSET = 200
ARGS_INTERACTION_LENGTH_MASK = 0xffffff

AMOUNT_MASK = 0x000000000000000000ffffffffffffffffffffffffffffffffffffffffffffff

print("ФЛАГИ ТЕЙКЕРА:")
print(f"  IS_MAKING_AMOUNT (based on maker amount):  {'✅ ДА' if (taker_traits & MAKER_AMOUNT_FLAG) != 0 else '❌ НЕТ'}")
print(f"  UNWRAP_WETH:                               {'✅ ДА' if (taker_traits & UNWRAP_WETH_FLAG_TAKER) != 0 else '❌ НЕТ'}")
print(f"  SKIP_MAKER_PERMIT:                         {'✅ ДА' if (taker_traits & SKIP_ORDER_PERMIT_FLAG) != 0 else '❌ НЕТ'}")
print(f"  USE_PERMIT2:                               {'✅ ДА' if (taker_traits & USE_PERMIT2_FLAG_TAKER) != 0 else '❌ НЕТ'}")
print(f"  ARGS_HAS_TARGET:                           {'✅ ДА' if (taker_traits & ARGS_HAS_TARGET) != 0 else '❌ НЕТ'}")

print()
print("ЗНАЧЕНИЯ ТЕЙКЕРА:")
print(f"  Args Extension Length:  {(taker_traits >> ARGS_EXTENSION_LENGTH_OFFSET) & ARGS_EXTENSION_LENGTH_MASK}")
print(f"  Args Interaction Length: {(taker_traits >> ARGS_INTERACTION_LENGTH_OFFSET) & ARGS_INTERACTION_LENGTH_MASK}")
print(f"  Threshold Amount:        {taker_traits & AMOUNT_MASK} (0x{(taker_traits & AMOUNT_MASK):x})")

print()
print("=" * 60)
print("ПОДРОБНО ПО БИТАМ")
print("=" * 60)

print("\nMaker Traits биты (247-255):")
for bit in range(255, 246, -1):
    bit_val = (maker_traits >> bit) & 1
    names = {
        255: "NO_PARTIAL_FILLS",
        254: "ALLOW_MULTIPLE_FILLS",
        253: "RESERVED",
        252: "PRE_INTERACTION",
        251: "POST_INTERACTION",
        250: "CHECK_EPOCH_MGR",
        249: "HAS_EXTENSION",
        248: "USE_PERMIT2",
        247: "UNWRAP_WETH"
    }
    print(f"  bit {bit} ({names.get(bit, 'UNKNOWN'):20}): {bit_val}")

print("\nTaker Traits биты (247-255):")
for bit in range(255, 246, -1):
    bit_val = (taker_traits >> bit) & 1
    names = {
        255: "MAKER_AMOUNT",
        254: "UNWRAP_WETH",
        253: "SKIP_PERMIT",
        252: "USE_PERMIT2",
        251: "HAS_TARGET",
        250: "RESERVED",
        249: "RESERVED",
        248: "RESERVED",
        247: "RESERVED"
    }
    print(f"  bit {bit} ({names.get(bit, 'UNKNOWN'):20}): {bit_val}")

print()
print("=" * 60)
print("ПАРСИНГ ARGS")
print("=" * 60)

if args_hex.startswith('0x'):
    args_hex = args_hex[2:]
args = bytes.fromhex(args_hex)

has_target = (taker_traits & ARGS_HAS_TARGET) != 0
extension_length = (taker_traits >> ARGS_EXTENSION_LENGTH_OFFSET) & ARGS_EXTENSION_LENGTH_MASK
interaction_length = (taker_traits >> ARGS_INTERACTION_LENGTH_OFFSET) & ARGS_INTERACTION_LENGTH_MASK

offset = 0

if has_target:
    target = args[offset:offset+20]
    offset += 20
    print(f"\nTarget address: 0x{target.hex()}")
else:
    print(f"\nTarget: msg.sender")

if extension_length > 0:
    extension = args[offset:offset+extension_length]
    offset += extension_length
    print(f"\nExtension ({len(extension)} bytes):")
    print(f"0x{extension.hex()}")
else:
    print(f"\nExtension: empty")

if interaction_length > 0:
    interaction = args[offset:offset+interaction_length]
    offset += interaction_length
    print(f"\nInteraction ({len(interaction)} bytes):")
    print(f"0x{interaction.hex()}")
else:
    print(f"\nInteraction: empty")

if offset < len(args):
    signature = args[offset:]
    print(f"\nSignature ({len(signature)} bytes):")
    print(f"0x{signature.hex()}")