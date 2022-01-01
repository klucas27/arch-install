import os
import time


def full_run():
    os.system("clear")
    print("\n", "*" * 50, "\n\n\t\t\tFull Install Started!\n\n", "*" * 50)
    time.sleep(3)
    file = open("info.txt", "w")
    time.sleep(1)
    file.close()



if __name__ == '__main__':
    full_run()
