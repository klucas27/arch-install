#!/bin/bash

echo "Install Arch Linux in ROOT"
echo 'zoneinfo config..'
ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
sleep 2
echo "hwclock sync:"
hwclock --systohc
sleep 2
echo 'Config Mirror List'
reflector --verbose --latest 5 --sort rate --save /etc/pacman.d/mirrorlist
sleep 2
echo "Install Tools:"
pacman -Sy firefox reflector xorg-server nano vim dosfstools os-prober mtools network-manager-applet networkmanager wpa_supplicant wireless_tools dialog sudo --noconfirm
sleep 2
echo 'Locale Config..'
echo LANG = pt_BR.UTF-8 >> /etc/locale.conf
sleep 2
echo 'Config KeyMap'
echo KEYMAP = br-abnt2 >> /etc/vconsole.conf
loadkeys br-abnt2
sleep 2
echo 'Config Local'
echo pt_BR.UTF-8 UTF-8 >> /etc/locale.gen
sleep 2
echo 'Gen Local'
locale-gen
sleep 2
echo 'Install Python3'
pacman -Sy python3 --noconfirm
sleep 2
echo 'Download Grub'
pacman -Sy grub --noconfirm
echo 'Install Tools 2'
pacman -Sy xfce4 xfce4-goodies xfce4-terminal pavucontrol lightdm lightdm-gtk-greeter gvfs xarchiver thunar gnome-terminal xorg-xinit --noconfirm
sleep 2
echo 'Config xinitrc'
echo \"exec startxfce4\" > ~/.xinitrc
sleep 2
echo 'Activate lightdm'
systemctl enable lightdm
sleep 2
echo 'Activate NetworkManager'
systemctl enable NetworkManager
sleep 2