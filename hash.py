import hashlib

s = "Python Bootcamp"


def hash_1(given_string):
    print(hash(given_string))
    return hash(given_string)


def hash_2(given_string):
    print(hashlib.sha3_512(given_string.encode()).hexdigest())
    return hashlib.sha3_512(given_string.encode()).hexdigest()


hash_1(s)
hash_2(s)
