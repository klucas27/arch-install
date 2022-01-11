from runs import install_tools


def run_new_file(b_dev=True,
                 grub_custom=True,
                 grub_type="BIOS",
                 gui="budgie",
                 display="lxdm",
                 ):

    run = install_tools.Install()
    username = run.username
    disk = run.disk
    country = run.country
    zoneinfo = run.zoneinfo
    layout = run.layout
    variant = run.variant
    lang = run.lang
    coding = run.coding

    new_evdev = [
        'Section "InputClass"',
        '\tIdentifier "evdev keyboard catchall"',
        '\tMatchIsKeyboard "on"',
        '\tMatchDevicePath "/dev/input/event*"',
        '\tDriver "evdev"',
        f'\tOption "XkbLayout" "{layout}"',
        f'\tOption "XkbVariant" "{variant}"',
        'EndSection',
    ]

    with open("./files/xorg.conf.d/10-evdev.conf", "w+") as evdev:
        for pas in new_evdev:
            evdev.write(f"{pas}\n")

    evdev.close()

    file = [
        "# !/bin/bash",

        "",

        'echo "***Install Arch Linux in ROOT***"',
        'sleep 5',

        # apps Necessaries started
        "pacman -Sy reflector --noconfirm",
        "pacman -Sy sudo --noconfirm",
        "pacman -Syu python3 --noconfirm",

        # Configs Iniciais
        "echo 'Config Iniciais'",

        # Config Mirrorlist locale
        f"reflector --verbose --latest 3 --sort rate --country {country} --save /etc/pacman.d/mirrorlist",

        # Config local
        f"ln -sf /usr/share/zoneinfo/{zoneinfo} /etc/localtime",

        # Config Relogio
        "hwclock --systohc",

        # Config Locale teclado
        f"echo 'LANG = {lang}' >> /etc/locale.conf",
        f"echo 'KEYMAP = {layout}-{variant}' >> /etc/vconsole.conf",
        f"loadkeys {layout}-{variant}",
        f"echo '{lang} {coding}' >> /etc/locale.gen",
        "locale-gen",
        "sudo rm -rf /etc/X11/xorg.conf.d",
        "sudo cp -rf xorg.conf.d /etc/X11",


        # Install Tools
        "echo 'Install Tools:'",

        # Apps Files
        "pacman -Sy gvfs --noconfirm",
        "pacman -Sy thunar --noconfirm",
        "pacman -Sy xarchiver --noconfirm",
        "pacman -Sy unrar --noconfirm",

        # Apps redes
        "pacman -Sy networkmanager --noconfirm",
        "pacman -Sy network-manager-applet --noconfirm",
        "pacman -Sy wpa_supplicant --noconfirm",
        "pacman -Sy wireless_tools --noconfirm",
        "pacman -Sy libnm --noconfirm",
        "pacman -Sy libnma --noconfirm",
        "pacman -Sy systemd --noconfirm",
        "pacman -Sy systemd-libs --noconfirm",
        "pacman -Sy systemd-ui --noconfirm",
        "pacman -Sy net-tools --noconfirm",
        "pacman -Sy iproute2 --noconfirm",
        "systemctl enable NetworkManager",  # active rede
        "systemctl enable systemd-networkd.service",  # active rede
        "systemctl enable systemd-resolved.service",  # active rede

        # Apps Audio
        "pacman -Sy pavucontrol --noconfirm",
        "pacman -Sy pulseaudio --noconfirm",
        "pacman -Sy pulseaudio-equalizer --noconfirm",
        "pacman -Sy alsa-utils --noconfirm",

        # Navegadores
        "pacman -Sy firefox --noconfirm",
        # "pacman -Sy tor --noconfirm",

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
        "pacman -Sy p7zip --noconfirm",
        "pacman -Sy gnome-calculator --noconfirm",
        "pacman -Sy libreoffice-fresh --noconfirm",
        "pacman -Sy libreoffice-fresh-pt-br --noconfirm",

        # Create User
        f"useradd -m {username}",

    ]

    dev_bib = [
        "pacman -Sy code --noconfirm",
        "pacman -Sy pycharm-community-edition --noconfirm",
        "pacman -Sy konsole --noconfirm",

        # Install Vbox
        "sudo pacman -Sy virtualbox --noconfirm",
        "sudo pacman -Sy virtualbox-host-modules-arch --noconfirm",
        f"sudo gpasswd -a {username} vboxusers",
        "sudo modprobe vboxdrv",
        "sudo depmod -a",
        "sudo modprobe vboxdrv",
        "sudo echo 'vboxdrv' >> /etc/modules-load.d/virtualbox.conf",

    ]

    grub_custom_bib = [

        "pacman -Sy grub-customizer --noconfirm",

        # personalize Grub
        "echo 'Config Grub'",
        "cp -r Xenlism-Arch /usr/share/grub/themes/",
        "echo 'GRUB_THEME=\"/usr/share/grub/themes/Xenlism-Arch/theme.txt\"' >> /etc/default/grub",
        "echo 'GRUB_DISABLE_OS_PROBER=true' >> /etc/default/grub",
        "grub-mkconfig -o /boot/grub/grub.cfg",

    ]

    grub_bios = [

        # Install Grub
        "echo 'Download Grub'",
        "pacman -Sy grub --noconfirm",

        "echo 'Install Grub'",
        f"grub-install --force --target=i386-pc --recheck {disk}",

        "echo 'Copy grub.mo'",
        "cp /usr/share/locale/en@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo",
        "grub-mkconfig -o /boot/grub/grub.cfg",

    ]

    budgie_bib = [
        # install Budgie-desktop
        "pacman -Sy budgie-desktop --noconfirm",

        # xinit budgie
        "echo \"export XDG_CURRENT_DESKTOP=Budgie:GNOME\" > ~/.xinitrc",
        "echo \"exec budgie-desktop\" > ~/.xinitrc",

    ]

    kde_plasma_bib = [
        # Install KDE
        "pacman -Sy plasma-desktop --noconfirm",

        # xinit KDE
        "echo \"export DESKTOP_SESSION=plasma\" > ~/.xinitrc",
        "echo \"exec startplasma-x11\" > ~/.xinitrc",
    ]

    gnome_bib = [
        # Install GNOME
        "pacman -Sy gnome --noconfirm",

        # xinit Gnome
        "echo \"export XDG_SESSION_TYPE=x11\" > ~/.xinitrc",
        "echo \"export GDK_BACKEND=x11\" > ~/.xinitrc",
        "echo \"exec gnome-session\" > ~/.xinitrc",
    ]

    lxqt_bib = [
        # Install LXQT
        "pacman -Sy lxqt --noconfirm",

        # xinit lxqt
        "echo \"exec startlxqt\" > ~/.xinitrc",
    ]

    xfce4_bib = [
        "pacman -Sy xfce4 --noconfirm",
        "pacman -Sy xfce4-goodies --noconfirm",

        # xinit fxce4
        "echo \"exec startxfce4\" > ~/.xinitrc",
    ]

    lxdm_bib = [
        # install lxdm
        "pacman -Sy lxdm-gtk3 --noconfirm",
        "systemctl enable lxdm.service",
        "systemctl set-default graphical.target",
        "sudo cp -rf Arch-Dark /usr/share/lxdm/themes/",
        "sudo rm -f /etc/lxdm/lxdm.conf",
        "sudo cp -f lxdm.conf /etc/lxdm/",
    ]

    sddm_bib = [
        # install lxdm
        "pacman -Sy sddm --noconfirm",
        "pacman -Sy sddm-kcm --noconfirm",
        "systemctl enable sddm.service",
        "systemctl set-default graphical.target",
    ]

    with open("./files/scp.sh", "w+") as script:
        for pas in file:
            script.write(f"{pas}\n")
            script.write("sleep 1\n")

        if b_dev:
            for pas in dev_bib:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

        if grub_custom:
            for pas in grub_custom_bib:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

        if grub_type == "BIOS":
            for pas in grub_bios:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

        if gui == "budgie":
            for pas in budgie_bib:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

        if gui == "kde-plasma":
            for pas in kde_plasma_bib:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

        if gui == "GNOME":
            for pas in gnome_bib:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

        if gui == "lxqt":
            for pas in lxqt_bib:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

        if gui == "xfce4":
            for pas in xfce4_bib:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

        if display == "lxdm":
            for pas in lxdm_bib:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

        if display == "sddm":
            for pas in sddm_bib:
                script.write(f"{pas}\n")
                script.write("sleep 1\n")

    script.close()


if __name__ == '__main__':
    run_new_file()
