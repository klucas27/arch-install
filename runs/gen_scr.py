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
    "echo KEYMAP=br-abnt2 >> /etc/vconsole.conf"
    'locale-gen',
    "export LANG=pt_BR.UTF-8",
    "timedatectl set-ntp true",

]


if __name__ == '__main__':
    pass
