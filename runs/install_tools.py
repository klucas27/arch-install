import subprocess
import os
import time


def run_os(cmd):
    os.system(cmd)


class Install:
    def __init__(self):
        pass

    @classmethod
    def pre_install(cls):
        run_os("clear")
        print("\nInstall Tools...\n")
        run_os("pip install --upgrade pip")
        time.sleep(2)
        run_os("pip install PyQt5")
        time.sleep(2)


if __name__ == "__main__":
    test = Install()
    test.pre_install()

