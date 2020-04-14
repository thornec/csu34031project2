from cryptography.fernet import Fernet


def key_gen():
    # generate key
    key = Fernet.generate_key()
    return key


