import base64
def b64encode_bytes(b: bytes) -> str:
    return base64.b64encode(b).decode('ascii')