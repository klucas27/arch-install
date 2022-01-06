import os
import time
from runs import install_tools
from runs import new_file
import re
import subprocess


def full_run():
    os.system("clear")
    print("\n", "*" * 50, "\n\n\t\tFull Install Started!\n\n", "*" * 50)
    time.sleep(3)

    username = input("\nEnter your username: ")

    os.system("clear")
    with open("log.txt", "a+") as file:
        fdisk = subprocess.getoutput("fdisk -l")
        file.write(f"\n{fdisk}")
        for pas in fdisk.splitlines():
            if pas.startswith("Disk /dev/s"):
                with open("info.txt", "a+") as file2:
                    file2.write(f"\n{pas}")
                    file.write(f"\n\t\t{pas}")

                file2.close()
    file.close()

    r = re.compile(r"\D", re.ASCII)
    disks = {}

    with open("info.txt", "r+") as file:
        cont = 1
        for pas in file.readlines():
            if pas.startswith("Disk"):
                disks[cont] = []
                disks.get(cont).append(pas)
                disks.get(cont).append(pas.split(sep=",")[0])
                disks.get(cont).append(r.sub("", pas.split(sep=",")[0].split(sep=":")[1]))
                disks.get(cont).append(pas[5:13])
                cont += 1

        for key, vlr in disks.items():
            print(f"\n[{key}] ---> {vlr[1]}")

        print()
        disk_select = disks.get(int(input("Select your disk: ")))
        print()

        file.writelines(f"\nSelected Disk: {disk_select[3]}")
        file.writelines(f"\nSize Disk: {disk_select[2]}")
        disk = disk_select[3]

    execs = install_tools.Install()

    execs.vars(str(username), str(disk))

    print("\nStart Pre-Install\n")
    execs.pre_install()             # Exec Pré Install.
    os.system("clear")
    time.sleep(1)

    print("\nStart Partition Bios\n")
    execs.partition_bios(55, 96)    # Partition Bios.
    os.system("clear")
    time.sleep(1)

    print("\nStart Run New File\n")
    new_file.run_new_file()         # Creator script.
    os.system("clear")
    time.sleep(1)

    print("\nStart Install System\n")
    execs.install_system()          # Install System.
    os.system("clear")
    time.sleep(1)

    print("\nStart Config User\n")      # Config User.
    execs.config_user()
    os.system("clear")
    time.sleep(1)

    print("*"*80)
    print("\nFinished!\n")
    print("*"*80)
    exit()


if __name__ == '__main__':
    full_run()
