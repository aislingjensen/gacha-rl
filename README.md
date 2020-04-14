### First Time Setup
install ubuntu via wsl (sorry, this is undocumented because I did it years ago. as I recall it's not hard)
install vscode
set vscode terminal to wsl

sudo apt upgrade
sudo apt install linuxbrew-wrapper

brew install pyenv
brew update
PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
brew install gcc (it's recommended and I want to be safe)
brew install pyenv (I used https://realpython.com/intro-to-pyenv/ "using the pyenv-installer)

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

pyenv install 3.8.2
pyenv global 3.8.2
exec "$SHELL" (or just spawn a new one)
python --version (should read 3.8.2)

sudo apt install mesa-common-dev \
    libsdl2-dev libsdl2-image-dev \
    libsdl2-ttf-dev libsdl2-mixer-dev


curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

poetry install
