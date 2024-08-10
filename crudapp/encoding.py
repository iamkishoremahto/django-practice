import base64

def encode_id(id):
    return base64.urlsafe_b64encode(id.encode()).decode()

def decode_id(encoded_id):
    return base64.urlsafe_b64decode(encoded_id.encode()).decode()
