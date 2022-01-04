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
    def get_disks():
        print("Geting Disks...")
        fdisk = get_output("fdisk -l")
        for pas in fdisk.splitlines():
            if pas.startswith("Disk /dev/s"):
                with open("info.txt", "a+") as file:
                    file.write(f"\n{pas}")

        file.close()

    @staticmethod
    def partition_bios():
        r = re.compile(r"\D", re.ASCII)
        disks = {}
        with open("info.txt", "r") as file:
            cont = 1
            for pas in file.readlines():
                if pas.startswith("Disk"):
                    disks[cont] = []
                    disks.get(cont).append(pas)
                    disks.get(cont).append(pas.split(sep=",")[0])
                    disks.get(cont).append(r.sub("", pas.split(sep=",")[0].split(sep=":")[1]))
                    disks.get(cont).append(pas[5:13])
                    cont += 1

        file.close()

        for key, vlr in disks.items():
            print(f"[{key}] ---> {vlr[1]}\n")

        print()
        disk_select = disks.get(int(input("Select your disk: ")))
        print()
        print(disk_select)

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
    test.partition_bios()



