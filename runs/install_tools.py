import subprocess
import os
import time
import re


def run_os(cmd):
    os.system(cmd)


def get_output(cmd):
    return subprocess.getoutput(cmd)


class Install:
    def __init__(self, *args):
        pass

    @staticmethod
    def install_system():

        with open("log.txt", "r+") as file:
            install_commands = {
                "Install System": "pacstrap /mnt base base-devel linux linux-firmware",
                "Gen fstab": "genfstab -U -p /mnt >> /mnt/etc/fstab",
                "Install Python": "pacstrap /mnt python3",
                "Edit Domain": "echo chmod 777 scp.sh'",
                "Edit bash": "echo './scp.sh'",
                "Enter System": "arch-chroot /mnt",
            }

            for key, vlr in install_commands.items():
                print(key)
                time.sleep(1)
                x = get_output(str(vlr))
                file.write(f"\n{x}")

        file.close()
        run_os("cp log.txt /mnt/etc")
        run_os("cp info.txt /mnt/etc")
        run_os("cp scp.sh /mnt/etc")

    @staticmethod
    def partition_bios(size_root, size_home):

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
            mount_disk = {
                "Create label": f"parted {disk} mklabel gpt -s",
                "Create boot": f"parted {disk} mkpart primary ext4 1Mib 1GiB",
                "Set boot": f"parted {disk} set 1 bios on",
                "Create root": f"parted {disk} mkpart primary ext4 1GiB {size_root}%",
                "Create home": f"parted {disk} mkpart primary ext4 {size_root}% {size_home}%",
                "Create swap": f"parted {disk} mkpart primary linux-swap {size_home}% 100%",
                "Format boot": f"mkfs.fat -F32 {disk}1",
                "Format root": f"mkfs.ext4 {disk}2",
                "Format home": f"mkfs.ext4 {disk}3",
                "Format swap": f"mkswap {disk}4",
                "Mount root": f"mount {disk}2 /mnt",
                "Create /home": f"mkdir /mnt/home",
                "Create /boot": f"mkdir /mnt/boot",
                "Mount home": f"mount {disk}3 /mnt/home",
                "Mount swap": f"swapon {disk}4",
            }

            for key, vlr in mount_disk.items():
                print(key)
                time.sleep(1)
                x = get_output(str(vlr))
                file.write(f"\n{x}")

        file.close()

    @staticmethod
    def get_disks():

        print("Geting Disks...")
        with open("log.txt", "a+") as file:
            fdisk = get_output("fdisk -l")
            file.write(f"\n{fdisk}")
            for pas in fdisk.splitlines():
                if pas.startswith("Disk /dev/s"):
                    with open("info.txt", "a+") as file2:
                        file2.write(f"\n{pas}")
                        file.write(f"\n\t\t{pas}")

                    file2.close()
        file.close()

    @staticmethod
    def pre_install():

        run_os("clear")
        get_output("rm -rf log.txt")
        get_output("rm -rf info.txt")
        list_execs = {
            "Configurando MirrorList": "reflector --verbose --latest 5 --sort rate --save /etc/pacman.d/mirrorlist",
            "Verificando Python": "pacman -Sy python3 --noconfirm",
            "Instalando SpeedTest": "pacman -Sy speedtest-cli --noconfirm",
            "Configura Teclado": "loadkeys br-abnt2",
            "Mudando Idioma": 'echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen',
            "Mudando Codificação": "export LANG=pt_BR.UTF-8",
            "Generate Locale": "locale-gen",
            "Verificando tipo de Inicialização": "ls /sys/firmware/efi/efivars",
            "Testando Rede": "speedtest-cli",
            "Configurando Relógio": "timedatectl set-ntp true",
        }

        with open("log.txt", "a+") as logfile:

            for info, command in list_execs.items():
                print(info)
                if info == "Verificando tipo de Inicialização":
                    with open("info.txt", "a+") as file:
                        saida = get_output(command)
                        logfile.writelines(f"\n{saida}")
                        if saida.count("cannot access"):
                            file.write("\ninici: BIOS")
                            print("\t\tInicialização do tipo: BIOS")
                            time.sleep(2)
                        else:
                            file.write("\ninici: UEFI")
                            print("\t\tInicialização do tipo: UEFI")
                            time.sleep(2)
                        continue

                if info == "Testando Rede":

                    with open("info.txt", "a+") as file:
                        saida = get_output(command).splitlines()
                        logfile.writelines(f"\n{saida}")
                        for ver in saida:
                            if ver.startswith("Download:"):
                                file.write(f"\n{ver}")
                                print("\t\t", ver)
                            if ver.startswith("Upload:"):
                                file.write(f"\n{ver}")
                                print("\t\t", ver)
                                time.sleep(2)
                        continue

                comd = get_output(command)
                logfile.writelines(f"\n{comd}")

        logfile.close()
        file.close()


if __name__ == "__main__":
    test = Install()
    test.pre_install()
    test.get_disks()
    test.partition_bios(55, 96)
