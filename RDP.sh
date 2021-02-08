sudo useradd -m odiq
sudo adduser odiq
echo 'odiq:youme' | sudo chpasswd

wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
sudo dpkg --install chrome-remote-desktop_current_amd64.deb
sudo apt install --assume-yes --fix-broken

DEBIAN_FRONTEND=noninteractive
apt install --assume-yes xfce4 desktop-base
sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'
sudo apt install --assume-yes xscreensaver
sudo systemctl disable lightdm.service

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg --install google-chrome-stable_current_amd64.deb
sudo apt install --assume-yes --fix-broken


apt install nautilus nano -y
sudo apt install nautilus nano -y



sudo adduser odiq chrome-remote-desktop
read -p "Code " code;
su - odiq -c """${code}"""

