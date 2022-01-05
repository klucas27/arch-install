import os
import time
from runs import install_tools
from runs import new_file


def full_run():
    os.system("clear")
    print("\n", "*" * 50, "\n\n\t\t\tFull Install Started!\n\n", "*" * 50)
    time.sleep(3)
    execs = install_tools.Install()

    execs.pre_install()             # Exec Pré Install.

    execs.get_disks()               # Get Disks.

    execs.partition_bios(55, 96)    # Partition Bios.

    new_file.run_new_file()         # Creator script.

    execs.install_system()          # Install System.


if __name__ == '__main__':
    full_run()
