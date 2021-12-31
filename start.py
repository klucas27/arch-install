from runs import full_install


while True:
    options = {
        1: ["Full Install", "full_install.full_run()"]
    }

    for key, option in options.items():
        print(f"[{key}] -->> {option[0]}")

    set_option = input("\n>> ")

    exec(options.get(int(set_option))[1])
