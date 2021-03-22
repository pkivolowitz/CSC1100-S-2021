# Installation instructions for Windows

## Python

It is required that Python 3.7 be installed as no wheel file for Python 3.8 is available at the time of this writing. Repeat, the Python version **must** be 3.7.X.

### Installation

Link to the Python installation file is [here](https://www.python.org/ftp/python/3.7.5/python-3.7.5-amd64.exe).

0. Click "Run"
1. Click on "Add Python 3.7 to PATH"
2. Click on "Install Now"
3. Click on "Yes"
4. Click on "Disable path length limit"
5. Click on "Yes"
6. Click on "Close"

### Confirmation

1. Press Windows Key
2. Type "cmd" and enter. This is your "command prompt" - we will use it alot.
3. Type `python --version`
4. You should see `Python 3.7.5` or another numeric value indicating a different version. The first two digits must be "3.7".

## Python modules first time setup

1. Enter command prompt if not already in it (see above if unsure how)
2. Type `python -m pip install --upgrade pip setuptools wheel` and hit enter. Alert instructor if the last line printed does not include "Successfully".
3. Type `pip install PyPl` and hit enter. Alert instructor if the last line doe snot include "Successfully"
4. Use this [link](https://files.pythonhosted.org/packages/55/89/5a66a6be1720b823111d603abc975803a403f294e77fc8862fdafea4e005/scipy-1.3.2-cp37-cp37m-win_amd64.whl) save the file to your Downloads folder. Wait for the download to finish. **NOTE** Notice the 37 repeated in this file name? It corresponds to having installed Python 3.7.X. If this is not the case, the following will not work and you should alert the instructor.
5. Back in the command prompt type `pip install Downloads\scipy-1.3.2-cp37-cp37m-win_amd64.whl` and hit enter. Alert the instructor if the last line does not include "Successfully".
6. Use this [link](https://files.pythonhosted.org/packages/cb/5a/abd74bd5ce791e2ab0b6fd88b144c42dbc88b3b1d963147417d0e163684b/scikit_image-0.16.2-cp37-cp37m-win_amd64.whl) save the file to your Downloads folder. Wait for the download to finish. **NOTE** Notice the 37 repeated in this file name? It corresponds to having installed Python 3.7.X. If this is not the case, the following will not work and you should alert the instructor.
7. Back in the command prompt type `pip install Downloads\scikit_image-0.16.2-cp37-cp37m-win_amd64.whl` and hit enter. Alert the instructor if the last line does not include "Successfully".
8. Type `pip install mutagen matplotlib` and hit enter. Alert the instructor if the last line does not include "Successfully".

### Install Visual Studio Code

1. In your web browser search for Visual Studio Code Download
2. Click on the first link making sure it leads to a Microsoft website.
3. Click on the download button for Windows (64 bit)
4. Install

