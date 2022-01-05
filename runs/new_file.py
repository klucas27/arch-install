
def run_new_file():
    disk = ""

    with open("info.txt", "r") as info:
        for pas in info.readlines():
            if pas.startswith("Selected Disk"):
                disk = pas[15:]

    info.close()

    file = [
        "# !/bin/bash",

        "",

        'echo "Install Arch Linux in ROOT"',
        'sleep 10',

        "echo 'zoneinfo config..'",
        "ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime",

        "echo 'hwclock sync:'",
        "hwclock --systohc",

        "echo 'Config Mirror List'",
        "reflector --verbose --latest 5 --sort rate --save/etc/pacman.d/mirrorlist",

        "echo 'Install Tools:'",
        "pacman -Sy firefox reflector xorg-server nano vim dosfstools os-prober mtools network-manager"
        "-applet networkmanager wpa_supplicant wireless_tools dialog sudo --noconfirm",

        "echo 'Locale Config..'",
        "echo LANG = pt_BR.UTF-8 >> /etc/locale.conf",

        "echo 'Config KeyMap'",
        "echo KEYMAP = br-abnt2 >> /etc/vconsole.conf",
        "loadkeys br-abnt2",

        "echo 'Config Local'",
        "echo pt_BR.UTF-8 UTF-8 >> /etc/locale.gen",

        "echo 'Gen Local'",
        "locale-gen",

        "echo 'Install Python3'",
        "pacman -Sy python3 --noconfirm",

        "echo 'Download Grub'",
        "pacman -Sy grub --noconfirm",

        "echo 'Install Grub'",
        f"grub-install --force --target=i386-pc --recheck {disk}",

        "echo 'Copy grub.mo'",
        "cp /usr/share/locale/en@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo",

        "echo 'Config Grub'",
        "grub-mkconfig -o /boot/grub/grub.cfg",

        "echo 'Install XFCE4'",         # install XFCE4
        "pacman -Sy xfce4 xfce4-goodies xfce4-terminal pavucontrol lightdm lightdm-gtk-greeter gvfs xarchiver thunar gn"
        "ome-terminal xorg-xinit pulseaudio-equalizer --noconfirm",

        "echo 'Config xinitrc'",         # Config XFCE4
        "echo \"exec startxfce4\" > ~/.xinitrc",

        "echo 'Activate lightdm'",
        "systemctl enable lightdm",

        "echo 'Activate NetworkManager'",
        "systemctl enable NetworkManager",

    ]

    with open("scp.sh", "w+") as script:
        for pas in file:
            script.write(f"{pas}\n")
            script.write("sleep 2\n")

    script.close()


if __name__ == '__main__':
    run_new_file()
