from runs import full_install
from runs import custom_install

import os

while True:
    os.system("clear")
    options = {
        1: ["Full Install", "full_install.full_run()"],
        2: ["Custom Install", "custom_install.full_run()"],
    }

    for key, option in options.items():
        print(f"[{key}] -->> {option[0]}")

    set_option = input("\n>> ")

    exec(options.get(int(set_option))[1])
