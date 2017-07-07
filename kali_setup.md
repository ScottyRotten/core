#Kali Setup Notes

#change theme in solarized
apt-get install terminator

#Install Hack font for terminal http://sourcefoundry.org/hack/
#Change font to hack in terminator profile
apt-get install fonts-hack-ttf

#Install Ultimate Vim Config https://github.com/amix/vimrc
git clone https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh

#Install ZSH with gentoo theme
#edit ~/.zshrc theme to "gentoo"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

