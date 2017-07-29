apt-get update
apt-get upgrade

apt-get install -y git zsh
apt-get install -y wget stow
apt-get install -y python3.4-venv
apt-get install -y unzip
apt-get install -y tig

# Oh-my-zsh
git clone git://github.com/robbyrussell/oh-my-zsh.git /home/vagrant/.oh-my-zsh
cp /home/vagrant/.oh-my-zsh/templates/zshrc.zsh-template /home/vagrant/.zshrc
chsh -s /usr/bin/zsh vagrant

# Vundle
git clone git://github.com/VundleVim/Vundle.vim.git /home/vagrant/.vim/bundle/Vundle.vim

