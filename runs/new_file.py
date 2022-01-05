
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


        # apps Necessaries started
        "pacman -Sy reflector --noconfirm",

        "echo 'Config Mirror List'",
        "reflector --verbose --latest 5 --sort rate --save /etc/pacman.d/mirrorlist",

        "pacman -Sy sudo --noconfirm",
        "pacman -Sy python3 --noconfirm",


        "echo 'zoneinfo config..'",
        "ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime",

        "echo 'hwclock sync:'",
        "hwclock --systohc",

        "echo 'Locale Config..'",
        "echo LANG = pt_BR.UTF-8 >> /etc/locale.conf",

        "echo 'Config KeyMap'",
        "echo KEYMAP = br-abnt2 >> /etc/vconsole.conf",
        "loadkeys br-abnt2",

        "echo 'Config Local'",
        "echo pt_BR.UTF-8 UTF-8 >> /etc/locale.gen",

        "echo 'Gen Local'",
        "locale-gen",


        # install GUI
        "echo 'Install XFCE4'",
        "pacman -Sy xfce4 --noconfirm",
        "pacman -Sy xfce4-goodies --noconfirm",
        "echo 'Config xinitrc'",                        # Config XFCE4
        "echo \"exec startxfce4\" > ~/.xinitrc",


        # install Display manager
        "pacman -Sy lxdm-gtk3 --noconfirm",

        "echo 'Activate LXDM'",                         # active Display
        "systemctl enable lxdm.service",

        "echo 'Config set-default'",                    # config set-default
        "systemctl set-default graphical.target",

        "echo 'Install Tools:'",

        # Apps Files
        "pacman -Sy gvfs --noconfirm",
        "pacman -Sy thunar --noconfirm",
        "pacman -Sy xarchiver --noconfirm",


        # Apps redes
        "pacman -Sy networkmanager --noconfirm",
        "pacman -Sy network-manager-applet --noconfirm",
        "pacman -Sy wpa_supplicant --noconfirm",
        "pacman -Sy wireless_tools --noconfirm",

        "echo 'Activate NetworkManager'",               # active rede
        "systemctl enable NetworkManager",


        # Apps Audio
        "pacman -Sy pavucontrol --noconfirm",
        "pacman -Sy pulseaudio-equalizer --noconfirm",


        # Navegadores
        "pacman -Sy firefox --noconfirm",


        # Editores
        "pacman -Sy nano --noconfirm",
        "pacman -Sy vim --noconfirm",


        # System
        "pacman -Sy gnome-terminal --noconfirm",
        "pacman -Sy dosfstools --noconfirm",
        "pacman -Sy mtools --noconfirm",
        "pacman -Sy dialog --noconfirm",


        # Startup
        "pacman -Sy os-prober --noconfirm",
        "pacman -Sy xorg-xinit --noconfirm",
        "pacman -Sy xorg-server --noconfirm",


        # Others
        "pacman -Sy git --noconfirm",
        "pacman -Sy grub-customizer",
        "pacman -Sy p7zip",



        # Install Grub
        "echo 'Download Grub'",
        "pacman -Sy grub --noconfirm",

        "echo 'Install Grub'",
        f"grub-install --force --target=i386-pc --recheck {disk}",

        "echo 'Copy grub.mo'",
        "cp /usr/share/locale/en@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo",

        "echo 'Config Grub'",                           # Config Grub
        "grub-mkconfig -o /boot/grub/grub.cfg",



    ]

    with open("scp.sh", "w+") as script:
        for pas in file:
            script.write(f"{pas}\n")
            script.write("sleep 2\n")

    script.close()


if __name__ == '__main__':
    run_new_file()
