#!/bin/bash

if ! command -v brew &> /dev/null
then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed"
fi

brew install python
brew install python-tk

mkdir -p /tmp/.imessagex
cd /tmp/.imessagex

rm -rf build dist venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

ctk_path=$(pip show customtkinter | grep -E '^Location:' | awk '{print $2}')

pyinstaller --name 'iMessageX' \
            --icon 'rabbit.ico' \
            --windowed  \
            --noconfirm \
            --onedir  \
            --add-data="${ctk_path}/customtkinter:customtkinter/" \
            iMessageX.py

echo "${ctk_path}/customtkinter:customtkinter/"
mv dist/iMessageX.app .
rm -rf build venv dist
rm iMessageX.py
rm iMessageX.spec
rm rabbit.ico
rm requirements.txt