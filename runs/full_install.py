import os
import time
import install_tools


def full_run():
    os.system("clear")
    print("\n", "*" * 50, "\n\n\t\t\tFull Install Started!\n\n", "*" * 50)
    time.sleep(3)
    # file = open("info.txt", "w")
    # time.sleep(1)
    # file.close()
    execs = install_tools.Install()

    execs.pre_install()     # Exec Pré Install

    execs.get_disks()       # Get Disks



if __name__ == '__main__':
    full_run()
