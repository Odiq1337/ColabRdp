import os

class RDP(object):
    def __init__(self, u, p):
        self.username = u
        self.password = p
        self.buatUser()
        self.tambahUser()
        self.aturkataSandi()
        self.installCRD()
        self.install_Desktop_environment()
        self.installGoogleChorme()
        self.installOtherTools()
        self.finish()


    def buatUser(self):
        os.system("sudo useradd -m %s" % (self.username))


    def tambahUser(self):
        os.system("sudo adduser %s" % (self.username))


    def aturkataSandi(self):
        os.system("echo '%s:%s' | sudo chpasswd" % (self.username, self.password))


    def installCRD(self):
        os.system("wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb")
        os.system("sudo dpkg --install chrome-remote-desktop_current_amd64.deb")
        os.system("sudo apt install --assume-yes --fix-broken")


    def install_Desktop_environment(self):
        os.system("DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base")
        os.system("sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'")
        os.system("sudo apt install --assume-yes xscreensaver")
        os.system("sudo systemctl disable lightdm.service")


    def installGoogleChorme(self):
        os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        os.system("sudo dpkg --install google-chrome-stable_current_amd64.deb")
        os.system("sudo apt install --assume-yes --fix-broken")


    def installOtherTools(self):
        os.system("apt install nautilus nano -y")
        os.system("sudo apt install nautilus nano -y")


    def finish(self):
        os.system("sudo adduser %s chrome-remote-desktop" % (self.username))
        code = input("Code: ")
        os.system('su - %s -c """%s"""' % (self.username, code))


if __name__ == "__main__":
    username = input("User: ")
    password = input("Pswd: ")
    RDP(username, password)
