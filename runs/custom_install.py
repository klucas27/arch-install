import os
import time
from runs import install_tools
from runs import new_file
import re
import subprocess


def full_run():
    start = time.time()
    os.system("clear")
    print("\n", "*" * 50, "\n\n\t\tCustom Install Started!\n\n", "*" * 50)
    time.sleep(3)

    username = input("\nEnter your username: ")

    os.system("clear")
    with open("./files/log.txt", "a+") as file:
        fdisk = subprocess.getoutput("fdisk -l")
        file.write(f"\n{fdisk}")
        for pas in fdisk.splitlines():
            if pas.startswith("Disk /dev/s"):
                with open("./files/info.txt", "a+") as file2:
                    file2.write(f"\n{pas}")
                    file.write(f"\n\t\t{pas}")

                file2.close()
    file.close()

    r = re.compile(r"\D", re.ASCII)
    disks = {}

    with open("./files/info.txt", "r+") as file:
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
    
    ls_inici = subprocess.getoutput("ls /sys/firmware/efi/efivars")

    type_inic = None
    if ls_inici.count("cannot access"):
        type_inic = "BIOS"
    else:
        type_inic = "UEFI"
    
    country = input("\nInsert your country(example: 'Brazil'): ")
    zoneinfo = input("Set your zoneinfo(example: 'America/Sao_Paulo'): ")
    layout = input("Set your Layout(example: 'br'): ")
    variant = input("Set your variant(example: 'abnt2'): ")
    lang = input("Set your Lang(example: 'pt_BR'): ")
    coding = input("Set your Coding(example: 'UTF-8'): ")

    options = {
        "dev": ["Download development tools: ",
                {
                    "Y": ["[Y]es", True],
                    "N": ["[N]o", False],
                },
                ],

        "grub_custom": ['Customize Grub: ',
                 {
                    "Y": ["[Y]es", True],
                    "N": ["[N]o", False],
                 },
                 ],

        "grub_type": [f'Set your Grub Type(Type now: {type_inic}): ',
                      {
                          "BIOS": ["[BIOS]", "BIOS"],
                          "UEFI": ["[UEFI]", "UEFI"],
                      },
                      ],

        "gui": ['Set your Interface GUI: ',
                {
                    "BUDGIE": ["[budgie]", "budgie"],
                    "KDE-PLASMA": ["[kde-plasma]", "kde-plasma"],
                    "GNOME": ["[GNOME]", "gnome"],
                    "LXQT": ["[lxqt]", "lxqt"],
                    "XFCE4": ["[xfce4]", "xfce4"],
                },
                ],

        "display": ['Set your Display Manager: ',
                    {
                    "LXDM": ["[lxdm]", "lxdm"],
                    "SDDM": ["[sddm]", "sddm"],
                    },
                    ],

    }
    
    for key, val in options.items():
        while True:
            print(val[0])
            for vlrs in val[1].values():
                print(f"\t{vlrs[0]}")
            get_option = input(">> ")
            try:
                option_geted = val[1].get(get_option.upper())[1]
                print(option_geted)
                break
            except TypeError:
                pass

        options.get(key).append(option_geted)

    execs.vars(str(username),
               str(disk),
               str(str(country)),
               str(str(zoneinfo)),
               str(str(layout)),
               str(str(variant)),
               str(str(lang)),
               str(str(coding)),

               )

    print("\nStart Pre-Install\n")
    execs.pre_install()  # Exec Pré Install.
    os.system("clear")
    time.sleep(1)

    print("\nStart Partition Bios\n")
    execs.partition_bios(55, 96)  # Partition Bios.
    os.system("clear")
    time.sleep(1)

    print("\nStart Run New File\n")
    new_file.run_new_file(b_dev=options.get("dev")[2],
                          grub_custom=options.get("grub_custom")[2],
                          grub_type=options.get("grub_type")[2],
                          gui=options.get("gui")[2],
                          display=options.get("display")[2],
                          )         # Creator script.
    os.system("clear")
    time.sleep(1)

    print("\nStart Install System\n")
    execs.install_system()           # Install System.
    os.system("clear")
    time.sleep(1)

    print("\nStart Config User\n")  # Config User.
    execs.config_user()
    os.system("clear")
    time.sleep(1)

    end = time.time()

    print("*" * 80)
    print("\nFinished!\n")
    print(f"\nUser: {username}\n")
    print(f"\nPassword: \n")
    time_total = ((end - start) / 60)

    print("\nTime Total: %.2f min\n" % time_total)

    print(f"\ndev = {options.get('dev')[2]}"),
    print(f'\ngrub_custom = {options.get("grub_custom")[2]}'),
    print(f'\ngrub_type = {options.get("grub_type")[2]}'),
    print(f'\ngui = {options.get("gui")[2]}'),
    print(f'\ndisplay = {options.get("display")[2]}'),

    print("*" * 80)
    exit()


if __name__ == '__main__':
    full_run()
