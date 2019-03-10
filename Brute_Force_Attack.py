import sys
import time
from Hasher import md5_hasher, sha_1_hasher, sha_224_hasher, sha_256_hasher, sha_384_hasher, sha_512_hasher
from ReportCreate import createcrackingreport


def numtochar(list, char):
    list2 = list
    for i in range(0, len(list2)):
        list2[i] = char[int(list2[i])]
    word = ""
    for o in range(0, len(list2)):
        word += list2[o]
    return word


def chartonum(list, char, max_char):
    difference = max_char - len(list)
    out_list = []
    for i in range(0, difference):
        out_list.append(0)
    for i in range(0, len(list)):
        out_list.append(char.index(list[i]))
    return out_list


def brute_force_attack(maximum, minimum, hash, char_num, output, algorithm, start_time):

    minimum = int(minimum)
    maximum = int(maximum)

    print("\tStarting Brute Force Attach...")

    time.sleep(1)

    letterslist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    upperletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    numberslist = ['0', '1', '2', '3',
                   '4', '5', '6', '7', '8', '9']
    specials = ['!', '@', '#', '$', '€', '%', '.', ',', '&', '*', '(', ')', '_', '-', '+', '=', '"', "'", '|', '\\', '/', '~',
                '`', '{', '}', '[', ']', ':', ';', '<', '>', '?', '^']

    charlist = [""]

    tocrack = []

    hashed = ""

    counter = 0

    if str(char_num)[3] == "1":
        charlist += letterslist
    if str(char_num)[2] == "1":
        charlist += upperletters
    if str(char_num)[1] == "1":
        charlist += numberslist
    if str(char_num)[0] == "1":
        charlist += specials
    num_of_char = len(charlist) - 1

    last_try = (len(charlist) - 1) ** maximum

    print("\tUsing the following [", num_of_char, "] characters: ")

    if str(char_num)[3] == "1":
        print('\t', letterslist)

    if str(char_num)[2] == "1":
        print('\t', upperletters)

    if str(char_num)[1] == "1":
        print('\t', numberslist)

    if str(char_num)[0] == "1":
        print('\t', specials)

    time.sleep(1)

    for i in range(0, int(maximum) - int(minimum)):
        tocrack.append(0)
    for i in range(0, minimum):
        tocrack.append(1)

    print("\tThere are", last_try, "possible combinations!!!")

    time.sleep(2)

    print("\tProgress is:")

    while hash != hashed:

        numbers_to_char = tocrack

        text = numtochar(numbers_to_char, charlist)

        if algorithm == 'md5':
            hashed = md5_hasher(text)
        elif algorithm == 'sha1':
            hashed = sha_1_hasher(text)
        elif algorithm == 'sha224':
            hashed = sha_224_hasher(text)
        elif algorithm == 'sha256':
            hashed = sha_256_hasher(text)
        elif algorithm == 'sha384':
            hashed = sha_384_hasher(text)
        elif algorithm == 'sha512':
            hashed = sha_512_hasher(text)

        counter += 1

        if counter % 100000 == 0:
            print("\t\t<---| checked", counter, "passwords", "|--->")

        tocrack = chartonum(tocrack, charlist, maximum)

        for i in range(0, len(tocrack)):
            if int(tocrack[len(tocrack) - i - 1]) != num_of_char:
                tocrack[len(tocrack) - i - 1] += 1
                break
            elif int(tocrack[len(tocrack) - i - 1]) == num_of_char:
                tocrack[len(tocrack) - i - 1] = 1

        if counter > last_try:
            print("\tPassword not found.")
            sys.exit(0)

    print("\tHash:", hash, "\n\tCracked successfully.\n\tPassword is:", text, "\n\tGenerating report. Please wait...")
    time.sleep(2)
    createcrackingreport(output, hash, algorithm, text, start_time, time.asctime(), 'Brute Force Attack')
