
def run_newfile():
    disk = ""
    with open("info.txt", "r+") as file:
        for pas in file.readline():
            if pas.startswith("Selected Disk:"):
                disk = pas[14:]

        new_file = [
            'echo "enter System /mnt!"',
            "ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime",
            "hwclock --systohc",
            "reflector --verbose --latest 5 --sort rate --save /etc/pacman.d/mirrorlist",
            "pacman -Sy python3 --noconfirm",
            "pacman -Sy speedtest-cli --noconfirm",
            "loadkeys br-abnt2",
            'echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen',
            "echo LANG=pt_BR.UTF-8 >> /etc/locale.conf",
            "echo KEYMAP=br-abnt2 >> /etc/vconsole.conf",
            'locale-gen',
            "export LANG=pt_BR.UTF-8",
            "timedatectl set-ntp true",
            "pacman -S dosfstools os-prober mtools network-manager-applet "
            "networkmanager wpa_supplicant wireless_tools dialog sudo --noconfirm",
            "pacman -S grub --noconfirm",
            f"grub-install --target=i386-pc --recheck {disk}",
            "cp /usr/share/locale/en@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo",

        ]

        with open("scp.sh", "w+") as newfile:
            for index in new_file:
                newfile.write(f"\n{index}")

    file.close()
    newfile.close()


if __name__ == "__main__":
    run_newfile()
