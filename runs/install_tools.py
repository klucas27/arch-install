import subprocess
import os
import time


def run_os(cmd):
    os.system(cmd)


def get_output(cmd):
    return subprocess.getoutput(cmd)


class Install:
    def __init__(self):
        pass

    @staticmethod
    def pre_install():

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
                            file.write("inici: BIOS")
                            print("\t\tInicialização do tipo: BIOS")
                            time.sleep(2)
                        else:
                            file.write("inici: UEFI")
                            print("\t\tInicialização do tipo: UEFI")
                            time.sleep(2)
                        continue

                if info == "Testando Rede":
                    with open("info.txt", "a+") as file:
                        saida = get_output(command).split()
                        logfile.writelines(f"\n{saida}")
                        for ver in saida:
                            if ver.startswith("Download:"):
                                file.write(ver)
                                print("\t\t", ver)
                            if ver.startswith("Upload:"):
                                file.write(ver)
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


