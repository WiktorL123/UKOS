import sys


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def save_to_file(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)


def add(params):
    plik = read_file("baza.txt")
    plik = params + plik
    save_to_file("baza.txt", plik)


def run_program(name, params):
    print(params)
    if params[0] == 'push':
        pass
    if params[0] == 'add':
        add(params[1])


if __name__ == '__main__':
    args = sys.argv
    run_program('PyCharm', sys.argv[1:])
