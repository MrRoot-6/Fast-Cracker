
# Copyright 2019 MrRoot-6.
#All rights reserved.
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other
# materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import getopt
from Brute_Force_Attack import *
from Dictionary_Attack import *
from AdditionalComponents import *
from Files import *
from Hasher import hashcheck, hashgenerate
from ReportCreate import hashcreatereport


def main():

    global start_time
    global out_file
    global dictionary
    global hash1
    global hash_file
    global hash_crack
    global max_char
    global min_char
    global brute_force
    global numbers
    global letters
    global upper_case
    global special
    global dict_attack
    global generate
    global hash_generate
    global algorithm

    allowedalgorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

    start_time = time.asctime()
    out_file = 'report.txt'
    dictionary = ''
    hash1 = ''
    hash_file = ''
    hash_crack = ''
    hash_generate = ""
    algorithm = 'md5'
    max_char = 6
    min_char = 4
    brute_force = True
    numbers = True
    letters = True
    upper_case = True
    special = False
    dict_attack = False
    generate = False

    logo()

    if not len(sys.argv[1:]):
        usage()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:t:f:o:a:d:m:n:z:x:c:v:g:",   ["help", "hash",
                                                                                  "file-hash", "output",
                                                                                  "algorithm",
                                                                                  "dictionary", "max-char",
                                                                                  "min-char", "no-numbers",
                                                                                  "no-letters", "no-upper",
                                                                                  "special", "generate"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-t", "--hash"):
            hash1 = a
        elif o in ("-f", "--file_hash"):
            hash_file = change_back_slash_to_slash(a)
        elif o in ("-o", "--output"):
            out_file = change_back_slash_to_slash(a)
        elif o in ("-a", "--algorithm"):
            algorithm = a
        elif o in ("-d", "--dictionary"):
            dictionary = change_back_slash_to_slash(a)
            brute_force = False
            dict_attack = True
        elif o in ("-m", "--max-char"):
            max_char = a
        elif o in ("-n", "--min-char"):
            min_char = a
        elif o in ("-z", "--no-numbers"):
            numbers = False
        elif o in ("-x", "--no-letters"):
            letters = False
        elif o in ("-c", "--no-upper"):
            upper_case = False
        elif o in ("-v", "--special"):
            special = True
        elif o in ("-g", "--generate"):
            hash_generate = a
            brute_force = False
            dict_attack = False
            generate = True
        else:
            assert False, "Option not accepted."

    if algorithm in allowedalgorithms:
        print("\tAlgorithm: %s" % algorithm)
    else:
        print("\tSpecified algorithm not allowed. \n\tUse one of the following: ", allowedalgorithms)

    if generate:
        hash = hashgenerate(spacereplace(hash_generate), algorithm)
        print("\tHashing text: ", hash_generate)
        time.sleep(1)
        print("\tHash is: ", hash)
        time.sleep(1)
        print("\tGenerating report. Please wait...")
        time.sleep(1)
        hashcreatereport(hash_generate, hash, algorithm, out_file)

    if hash1 == '' and hash_file == '':
        print("\tGive hash or specify path to hash file.")
        sys.exit(0)
    elif hash1 != '' and hash_file != '':
        print("\tGive hash or specify path to hash file.\tNot both!")
        sys.exit(0)
    elif hash1 != '' and hash_file == '':
        if hashcheck(hash1.lower(), algorithm):
            hash_crack = hash1
            print("\tHash is correct!")
    elif hash1 == '' and hash_file != '':
        if canopen(dictionary, "dictionary"):
            file = open(dictionary, 'r+')
            hash = file.readline()
            if hashcheck(hash, algorithm):
                print("\t\tFile contains correct hash!")

    crack_char = ["0", "0", "0", "0"]
    if letters:
        crack_char[3] = "1"
    if upper_case:
        crack_char[2] = "1"
    if numbers:
        crack_char[1] = "1"
    if special:
        crack_char[0] = "1"

    time.sleep(1)

    if brute_force:
        to_brute_force = ""
        for i in range(0, len(crack_char)):
            to_brute_force += crack_char[i]
        brute_force_attack(max_char, min_char, hash_crack, to_brute_force, out_file, algorithm, start_time)
    elif dict_attack:
        dictionary_attack(hash_crack, dictionary, algorithm, out_file, start_time)


main()
