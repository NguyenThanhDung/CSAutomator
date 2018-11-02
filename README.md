# CSAutomator

An auto script to play game

## Compatible Environments

* Nox App Player resolution: 1280x720
* CS game version: 1.2.5 1.0.70280

## Required Tools

* Python 2.7.9 or above
  * [Download](https://www.python.org/downloads/)

* Android SDK Platform Tools
  * [Download](https://developer.android.com/studio/releases/platform-tools)
  * Extract the downloaded file. For example: C:\platform-tools_r28.0.0-windows\
  * Add the platform-tool folder into environment variable: C:\platform-tools_r28.0.0-windows\platform-tools

* Tesseract
  * [Download](https://github.com/UB-Mannheim/tesseract/wiki)
  * Install and add the installation path into environment variable. For example: C:\Program Files (x86)\Tesseract-OCR

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

## Run

``` bash
python CSAutomator.py
```