# Nvidia Driver installation

Sometimes you will have a hard time installing the nvidia driver. Its usually because the driver gets blacklisted and doesnt automatically loads when system boots. If you know and can manually loan the driver, go ahead and do it, if not, these instructions can be helpful.

Check the current driver thats used.
```
dkms status
```

Removing all the mess
```
sudo apt-get purge nvidia*  
sudo apt remove nvidia-*  
sudo apt autoremove  
```

Reinstall the nvidia driver
```
sudo dkms install nvidia/470.74 -k $(uname -r) #uname gives the kernel version. 470.74 can be replace with the version you need
sudo update-initramfs -u #Updates the bootloader file and hopefully whitelist nvidia driver
sudo reboot
```

If Still stuck, go ahead and disable secure boot on BIOS. Had to do that on Euler.

Also give a try installing an HWE,
https://ubuntu.pkgs.org/20.04/ubuntu-updates-restricted-amd64/linux-modules-nvidia-470-generic-hwe-20.04_5.11.0-38.42~20.04.1_amd64.deb.html

## Ref

https://forums.developer.nvidia.com/t/nvidia-smi-has-failed-because-it-couldn-t-communicate-with-the-nvidia-driver-after-updating-ubuntu-20-04/170985/6

https://askubuntu.com/questions/1105090/cant-change-to-nvidia-proprietary-driver-ubuntu-18-04