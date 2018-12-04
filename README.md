# CSAutomator

An auto script to play game

## Compatible Environments

* Nox App Player resolution: 1280x720
* CS game version: 1.2.6

## Required Tools

* Python 2.7.9 or above
  * [Download](https://www.python.org/downloads/)

* Android SDK Platform Tools
  * Windows
    * [Download](https://developer.android.com/studio/releases/platform-tools)
    * Extract the downloaded file. For example: C:\platform-tools_r28.0.0-windows\
    * Add the platform-tool folder into environment variable: C:\platform-tools_r28.0.0-windows\platform-tools
  * Mac OS
    * Install brew (if not available) at https://brew.sh
    * Install adb via brew:
        ``` bash
        brew cask install android-platform-tools
        ```

* Tesseract
  * Windows
    * [Download](https://github.com/UB-Mannheim/tesseract/wiki)
    * Install and add the installation path into environment variable. For example: C:\Program Files (x86)\Tesseract-OCR
  * Mac OS
    * Install brew (if not available) at https://brew.sh
    * Install Tesseract via brew:
        ``` bash
        brew install tesseract
        ```

## First time set up

Install OpenCV for python:
``` bash
pip install opencv-python
```

Install enum module for python:
``` bash
pip install enum
```

Install Pillow module (PIL) for python:
``` bash
pip install Pillow
```

Install pytesseract module for python:
``` bash
pip install pytesseract
```

> Note:
>
> On Mac OS, append **sudo** at the beginning of the command to install with admin privilege, otherwise we may encounter permission deny error.

## Run

``` bash
python CSAutomator.py
```