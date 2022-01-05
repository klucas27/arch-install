import os
import time
from runs import install_tools
from runs import new_file


def full_run():
    os.system("clear")
    print("\n", "*" * 50, "\n\n\tFull Install Started!\n\n", "*" * 50)
    time.sleep(5)
    execs = install_tools.Install()

    execs.get_disks()               # Get Disks.

    username = input("\nEnter your username: ")

    with open("log.txt", "a+") as file:
        file.write(f"Username: {str(username)}")
    file.close()

    execs.pre_install()             # Exec Pré Install.

    execs.partition_bios(55, 96)    # Partition Bios.

    new_file.run_new_file()         # Creator script.

    execs.install_system()          # Install System.

    with open("/mnt/etc/shadow", "r+") as shadow:
        x = open("shadow", "w+")
        for pas in shadow.readlines():
            if pas.startswith(str(username)):
                pas.replace(":!:", "::")
            x.write(f"\n{pas}")
        x.close()
    shadow.close()

    with open("/mnt/etc/passwd", "r+") as passwd:
        x = open("passwd", "w+")
        for pas in passwd.readlines():
            if pas.startswith(str(username)):
                pas.replace(":x:", "::")
            x.write(f"\n{pas}")

    time.sleep(1)
    os.system("rm -rf /mnt/etc/shadow")
    time.sleep(1)
    os.system("cp shadow /mnt/etc/")
    time.sleep(1)
    os.system("rm -rf /mnt/etc/passwd")
    time.sleep(1)
    os.system("cp passwd /mnt/etc/")
    time.sleep(1)

    exit()


if __name__ == '__main__':
    full_run()
