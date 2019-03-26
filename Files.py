import sys


def canopen(filedirecrory, filename):
    try:
        file = open(filedirecrory, 'r')
        file.close()
        return True
    except FileNotFoundError or FileExistsError as err:
        print("\nCan't open ", filename, " file directory."
              "\nError: ", err)
        sys.exit(0)


def change_back_slash_to_slash(path):
    path = path.replace("\\", "/")
    return path
