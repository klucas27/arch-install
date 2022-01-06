import subprocess
import os
import time


def run_os(cmd):
    os.system(cmd)


def get_output(cmd):
    return subprocess.getoutput(cmd)


class Install:
    def __init__(self):
        ...

    @classmethod
    def vars(cls, username, disk):
        cls.username = username
        cls.disk = disk

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
                            time.sleep(1)
                        else:
                            file.write("\ninici: UEFI")
                            print("\t\tInicialização do tipo: UEFI")
                            time.sleep(1)
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
                                time.sleep(1)
                        continue

                comd = get_output(command)
                logfile.writelines(f"\n{comd}")

        logfile.close()
        file.close()

    def partition_bios(self, size_root, size_home):
        disk = self.disk
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

        with open("log.txt", "a+") as filelog:
            for key, vlr in mount_disk.items():
                print(key)
                time.sleep(1)
                x = get_output(str(vlr))
                filelog.write(f"\n{x}")
                # run_os(f"{vlr}")
        filelog.close()

    @staticmethod
    def install_system():
        with open("log.txt", "r+") as file:
            install_commands = {
                "Install System": "pacstrap /mnt base base-devel linux linux-firmware",
                "Gen fstab": "genfstab -U -p /mnt >> /mnt/etc/fstab",
                "Install Python": "pacstrap /mnt python3",
                "Install Reflector": "pacstrap /mnt reflector",
                "echo sleep #1": "echo \"sleep 2\" >> /mnt/etc/bash.bashrc",
                "echo exit": "echo \"exit\" >> /mnt/etc/bash.bashrc",
                "Copy script": "cp scp.sh /mnt/etc",
                "Copy Info": "cp info.txt /mnt/etc",
                "Copy theme-grub": "cp -r Xenlism-Arch /mnt/etc",
                "Copy evdev /mnt": "cp -r 10-evdev.conf /mnt/etc/X11/xorg.conf.d/",
                "Copy Log": "cp log.txt /mnt/etc",
                "Copy evdev": "cp 10-evdev.conf /mnt/etc",
                "Enter System #1": "arch-chroot /mnt",
                "Remove exit": "sed -i '$ d' /mnt/etc/bash.bashrc",
                "Edit Enter /etc": 'echo "cd /etc" >> /mnt/etc/bash.bashrc',
                "Edit Domain": 'echo "sudo chmod 777 /etc/scp.sh" >> /mnt/etc/bash.bashrc',
                "echo sleep #2": "echo \"sleep 2\" >> /mnt/etc/bash.bashrc",
                "Edit bash": "echo \"sudo ./scp.sh\" >> /mnt/etc/bash.bashrc",
                "Edit exit": "echo \"exit\" >> /mnt/etc/bash.bashrc",
                "Remove password root": "sed -i '1d' /mnt/etc/passwd",
                "Putting root": 'echo "\nroot::0:0:root:/root:/bin/bash\n" >> /mnt/etc/passwd',
                "Enter System - 2": "arch-chroot /mnt",
                "Remove enter /etc": "sed -i '$ d' /mnt/etc/bash.bashrc",
                "Remove Permission": "sed -i '$ d' /mnt/etc/bash.bashrc",
                "Remove sleep": "sed -i '$ d' /mnt/etc/bash.bashrc",
                "Remove Script": "sed -i '$ d' /mnt/etc/bash.bashrc",
                "Remove exit #2": "sed -i '$ d' /mnt/etc/bash.bashrc",
            }

            for key, vlr in install_commands.items():
                print(key)
                time.sleep(1)
                # x = get_output(str(vlr))
                run_os(str(vlr))
                # file.write(f"\n{x}")
                # print(f"\t\t\t {x}")

        file.close()

    def config_user(self):
        username = self.username

        temp_shadow = open("/mnt/etc/shadow", "r").readlines()
        with open("shadow", "w+") as shadow:
            for pas in temp_shadow:
                print(pas)
                if pas.startswith("root:"):
                    pas_new = pas.replace(":!:", "::")
                    shadow.write(pas_new)
                    continue
                if pas.startswith(f"{str(username)}"):
                    pas_new = pas.replace(":!:", "::")
                    shadow.write(pas_new)
                    continue
                shadow.write(pas)

        shadow.close()

        temp_passwd = open("/mnt/etc/passwd", "r").readlines()
        with open("passwd", "w+") as passwd:
            for pas in temp_passwd:
                print(pas)
                if pas.startswith("root:"):
                    pas_new = pas.replace(":x:", "::")
                    passwd.write(pas_new)
                    continue
                if pas.startswith(f"{str(username)}"):
                    pas_new = pas.replace(":x:", "::")
                    passwd.write(pas_new)
                    continue
                passwd.write(pas)

        passwd.close()

        temp_sudoers = open("/mnt/etc/sudoers", "r").readlines()
        with open("sudoers", "w+") as sudoers:
            for pas in temp_sudoers:
                print(pas)
                if pas.startswith("root"):
                    sudoers.write(pas)
                    sudoers.write(f"{username} ALL=(ALL) ALL\n")
                    continue
                sudoers.write(pas)

        sudoers.close()

        time.sleep(1)
        run_os("rm -rf /mnt/etc/passwd")
        time.sleep(1)
        run_os("rm -rf /mnt/etc/shadow")
        time.sleep(1)
        run_os("rm -rf /mnt/etc/sudoers")
        time.sleep(1)
        run_os("cp -f passwd /mnt/etc/")
        time.sleep(1)
        run_os("cp -f shadow /mnt/etc/")
        time.sleep(1)
        run_os("cp -f sudoers /mnt/etc/")
        time.sleep(1)

        with open("log.txt", "a+") as file:
            file.write(f"\nUsername: {str(username)}")
        file.close()


if __name__ == "__main__":
    pass
