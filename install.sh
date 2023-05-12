#!/bin/bash

if ! command -v brew &> /dev/null
then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed"
fi

brew install python
brew install python-tk
brew install git

macos_version=$(sw_vers -productVersion)

major_version=$(echo $macos_version | awk -F '.' '{print $1}')

if [ $major_version -lt 11 ]
then
    echo "macOS version is less than 11.x. Please update your macOS. We recommend to use Big Sur version."
    exit 1
else
    echo "macOS version is 11.x or greater"
fi

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
# rm -rf .imessagex

echo "Finished!"