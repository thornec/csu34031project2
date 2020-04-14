from cryptography.fernet import Fernet



def encrypt_message(message, room_name):

    # Get Room Key
    key = 1

    # Convert to Bytes
    encoded = message.encode()

    # Encrypt Message by Creating Fernet Object
    f = Fernet(key)
    encrypted = f.encrypt(encoded)

    # encrypted now contains original message encrypted using room key
    return encrypted
