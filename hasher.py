import hashlib
import sys


def hashcheck(hash, algorithm):
    allowed_char = {"a", "b", "c", "d", "e", "f",
                    "0", "1", "2", "3", "4",
                    "5", "6", "7", "8", "9"}
    if algorithm == 'md5':
        if len(hash) == 32:
            for i in range(0, 32):
                if hash[i] not in allowed_char:
                    sys.exit(0)
            return True
        else:
            print("Hash is not valid!!!")
            sys.exit(0)
    elif algorithm == 'sha1':
        if len(hash) == 40:
            for i in range(0, 40):
                if hash[i] not in allowed_char:
                    sys.exit(0)
            return True
        else:
            print("Hash is not valid!!!")
            sys.exit(0)
    elif algorithm == 'sha224':
        if len(hash) == 64:
            for i in range(0, 64):
                if hash[i] not in allowed_char:
                    sys.exit(0)
            return True
        else:
            print("Hash is not valid!!!")
            sys.exit(0)
    elif algorithm == 'sha256':
        if len(hash) == 64:
            for i in range(0, 64):
                if hash[i] not in allowed_char:
                    sys.exit(0)
            return True
        else:
            print("Hash is not valid!!!")
            sys.exit(0)
    elif algorithm == 'sha384':
        if len(hash) == 96:
            for i in range(0, 96):
                if hash[i] not in allowed_char:
                    sys.exit(0)
            return True
        else:
            print("Hash is not valid!!!")
            sys.exit(0)
    elif algorithm == 'sha512':
        if len(hash) == 128:
            for i in range(0, 128):
                if hash[i] not in allowed_char:
                    sys.exit(0)
            return True
        else:
            print("Hash is not valid!!!")
            sys.exit(0)


def md5_hasher(to_hash):
    md5 = hashlib.md5()
    md5.update(to_hash.encode('utf-8'))
    return md5.hexdigest()


def sha_1_hasher(to_hash):
    sha1 = hashlib.sha1()
    sha1.update(to_hash.encode('utf-8'))
    return sha1.hexdigest()


def sha_224_hasher(to_hash):
    sha224 = hashlib.sha224()
    sha224.update(to_hash.encode('utf-8'))
    return sha224.hexdigest()


def sha_256_hasher(to_hash):
    sha256 = hashlib.sha256()
    sha256.update(to_hash.encode('utf-8'))
    return sha256.hexdigest()


def sha_384_hasher(to_hash):
    sha384 = hashlib.sha384()
    sha384.update(to_hash.encode('utf-8'))
    return sha384.hexdigest()


def sha_512_hasher(to_hash):
    sha512 = hashlib.sha512()
    sha512.update(to_hash.encode('utf-8'))
    return sha512.hexdigest()


def hashgenerate(text, algorithm):
    if algorithm == 'md5':
        hashed = md5_hasher(text)
        return hashed
    elif algorithm == 'sha1':
        hashed = sha_1_hasher(text)
        return hashed
    elif algorithm == 'sha224':
        hashed = sha_224_hasher(text)
        return hashed
    elif algorithm == 'sha256':
        hashed = sha_256_hasher(text)
        return hashed
    elif algorithm == 'sha384':
        hashed = sha_384_hasher(text)
        return hashed
    elif algorithm == 'sha512':
        hashed = sha_512_hasher(text)
        return hashed
