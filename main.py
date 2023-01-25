import sys


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def save_to_file(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)


def contains(name):
    plik = read_file("baza.txt")
    if name in plik:
        print(plik)


def run_program(name, params):
    print(params)
    if params[0] == 'push':
        pass
    if params[0]=='contains':
        contains(params[1])


if __name__ == '__main__':
    args = sys.argv
    run_program('PyCharm', sys.argv[1:])




