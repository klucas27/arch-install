from runs import install_tools


def run_new_file():

    run = install_tools.Install()
    username = run.username
    disk = run.disk
    download = run.download
    upload = run.upload

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

        "echo 'Activate NetworkManager'",                   # active rede
        "systemctl enable NetworkManager",


        # Apps Audio
        "pacman -Sy pavucontrol --noconfirm",
        "pacman -Sy pulseaudio-equalizer --noconfirm",
        "pacman -Sy alsa-utils --noconfirm",


        # Navegadores
        "pacman -Sy firefox --noconfirm",


        # Editores
        "pacman -Sy nano --noconfirm",
        "pacman -Sy vim --noconfirm",


        # System
        "pacman -Sy gnome-terminal --noconfirm",
        "pacman -Sy konsole --noconfirm",
        "pacman -Sy dosfstools --noconfirm",
        "pacman -Sy mtools --noconfirm",
        "pacman -Sy dialog --noconfirm",
        "pacman -Sy gnome-control-center --noconfirm",


        # Startup
        "pacman -Sy os-prober --noconfirm",
        "pacman -Sy xorg-xinit --noconfirm",
        "pacman -Sy xorg-server --noconfirm",


        # Others
        "pacman -Sy git --noconfirm",
        "pacman -Sy grub-customizer --noconfirm",
        "pacman -Sy p7zip --noconfirm",
        "pacman -Sy gnome-calculator --noconfirm",
        "pacman -Sy libreoffice-fresh --noconfirm",
        "pacman -Sy libreoffice-fresh-pt-br --noconfirm",


        # Install Grub
        "echo 'Download Grub'",
        "pacman -Sy grub --noconfirm",

        "echo 'Install Grub'",
        f"grub-install --force --target=i386-pc --recheck {disk}",

        "echo 'Copy grub.mo'",
        "cp /usr/share/locale/en@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo",

        "echo 'Config Grub'",                           # personalize Grub
        "grub-mkconfig -o /boot/grub/grub.cfg",
        "cp -r Xenlism-Arch /usr/share/grub/themes/",
        "echo 'GRUB_THEME=\"/usr/share/grub/themes/Xenlism-Arch/theme.txt\"' >> /etc/default/grub",
        "echo 'GRUB_DISABLE_OS_PROBER=true' >> /etc/default/grub",
        "grub-mkconfig -o /boot/grub/grub.cfg",


        # install GUI
        "pacman -Sy budgie-desktop --noconfirm",



        # Install KDE
        # "pacman -Sy plasma-desktop --noconfirm",


        # Install GNOME
        # "echo Install GNOME",
        # "pacman -Sy gnome gnome-terminal nautilus gnome-tweaks gnome-control-center gnome-backgrounds "
        # "adwaita-icon-theme --noconfirm",


        # Install LXQT
        # "echo 'Install LXQT'",
        # "pacman -Sy lxqt --noconfirm",


        # "echo 'Install XFCE4'",
        # "pacman -Sy xfce4 --noconfirm",
        # "pacman -Sy xfce4-goodies --noconfirm",


        # install Display manager
        "pacman -Sy lxdm-gtk3 --noconfirm",

        "echo 'Activate LXDM'",                         # active Display
        "systemctl enable lxdm.service",

        "echo 'Config set-default'",                    # config set-default
        "systemctl set-default graphical.target",


        # Config xinit
        # "echo 'Config xinitrc'",
        # "echo \"startplasma-x11\" > ~/.xinitrc",
        # "echo \"DESKTOP_SESSION=plasma\" > ~/.xinitrc",
        # "echo \"exec startxfce4\" > ~/.xinitrc",

        # xinit budgie
        "echo 'Config xinitrc'",
        "echo \"export XDG_CURRENT_DESKTOP=Budgie:GNOME\" > ~/.xinitrc",
        "echo \"exec budgie-desktop\" > ~/.xinitrc",

        # Create User
        f"useradd -m {username}",

    ]

    with open("scp.sh", "w+") as script:
        for pas in file:
            script.write(f"{pas}\n")
            script.write("sleep 1\n")

    script.close()
    print("*"*80)
    print(f"\n{username}", f"\n\n{disk}\n", f"\n\n{download}\n", f"\n\n{upload}\n")
    print("*"*80)


if __name__ == '__main__':
    run_new_file()
