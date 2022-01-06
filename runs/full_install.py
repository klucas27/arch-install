import os
import time
from runs import install_tools
from runs import new_file


def full_run():
    os.system("clear")
    print("\n", "*" * 50, "\n\n\t\tFull Install Started!\n\n", "*" * 50)
    time.sleep(3)

    execs = install_tools.Install()

    print("Start Pre-Install")
    execs.pre_install()             # Exec Pré Install.
    os.system("clear")
    time.sleep(1)

    print("Start Partition Bios")
    execs.partition_bios(55, 96)    # Partition Bios.
    os.system("clear")
    time.sleep(1)

    print("Start Run New File")
    new_file.run_new_file()         # Creator script.
    os.system("clear")
    time.sleep(1)

    print("Start Install System")
    execs.install_system()          # Install System.
    os.system("clear")
    time.sleep(1)

    print("Start Config User")      # Config User.
    execs.config_user()
    os.system("clear")
    time.sleep(1)

    print("Finished!")
    exit()


if __name__ == '__main__':
    full_run()
