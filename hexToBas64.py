import binascii
import base64


def hexTObase64(hex_str):
    hex_byetes = bytes.fromhex(hex_str)
    base64_bytes = base64.b64encode(hex_byetes)
    return base64_bytes.decode("utf-8")

hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_encode = hexTObase64(hex_str)
print(base64_encode)


    