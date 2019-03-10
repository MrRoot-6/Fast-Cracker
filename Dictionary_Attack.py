import time
import sys
from Hasher import md5_hasher, sha_1_hasher, sha_224_hasher, sha_256_hasher, sha_384_hasher, sha_512_hasher
from AdditionalComponents import spacereplace
from ReportCreate import createcrackingreport


def dictionary_attack(hash, dict_location, algorithm, output, start_time):
    print("\tStarting Dictionary Attack...")
    time.sleep(1)

    dictionary = open(dict_location, 'r', encoding="ISO-8859-1")

    hashed = ''
    password = ''
    counter = 0

    print("\tProgress is:")

    while hashed != hash:
        password = dictionary.readline()
        if algorithm == 'md5':
            hashed = md5_hasher(spacereplace(password))
        elif algorithm == 'sha1':
            hashed = sha_1_hasher(spacereplace(password))
        elif algorithm == 'sha224':
            hashed = sha_224_hasher(spacereplace(password))
        elif algorithm == 'sha256':
            hashed = sha_256_hasher(spacereplace(password))
        elif algorithm == 'sha384':
            hashed = sha_384_hasher(spacereplace(password))
        elif algorithm == 'sha512':
            hashed = sha_512_hasher(spacereplace(password))

        counter += 1

        if counter % 1000000 == 0:
            print("\t\t<---|", counter, "passwords", "|--->")
        if hashed == '':
            print("Password not found.")
            sys.exit(0)

    dictionary.close()

    print("\tHash:", hash, "\n\tCracked successfully.\n\tPassword is:", password, "\n\tGenerating report. Please wait...")
    time.sleep(2)
    createcrackingreport(output, hash, algorithm, password, start_time, time.asctime(), "Dictionary Attack")
