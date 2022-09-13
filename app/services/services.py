import os


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return True
    return False


def io_operation():

    PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")

    FILE_TEXT = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
              tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
              quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
              consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
              cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
              proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
              """

    with open(PATH, "w+") as file:
        file.write(FILE_TEXT)
        file.seek(0, 0)
        lines = file.readline()
        first = lines.split('\n', 1)[0]

    try:
        os.remove(PATH)
    except OSError as e:
        print(f"Error {e.filename}, {e.strerror}")

    return first
