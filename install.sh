#!/bin/bash

if ! command -v brew &> /dev/null
then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed"
fi

brew install python@3.10
brew install python-tk@3.10

rm -rf /Applications/iMessageX.app

mkdir -p /tmp/.imessagex
cd /tmp/.imessagex
git clone https://github.com/Tuan-VuAnh/iMessageX.git

cd iMessageX
rm -rf build dist venv
python3 -m venv venv
source venv/bin/activate
pip install wheel
pip install -r requirements.txt

ctk_path=$(pip show customtkinter | grep -E '^Location:' | awk '{print $2}')

pyinstaller --name 'iMessageX' \
            --icon 'rabbit.ico' \
            --windowed  \
            --noconfirm \
            --onedir  \
            --add-data="${ctk_path}/customtkinter:customtkinter/" \
            iMessageX.py


mv dist/iMessageX.app /Applications

cd /tmp
rm -rf .imessagex