
# Installing Python on MacOS

## Terminal

You will be using the MacOS terminal a great deal. It would be best if you glued the terminal to your dock. Use Spotlight Search and enter "terminal" without the quotes. Then, right click on the terminal icon in the dock and select Options → Keep in Dock.

Here is a very brief first taste of using the terminal.

### cd

When you enter the terminal, you are "in" your home directory. Navigating directories will be a critical skill when using the terminal. The "cd" command changes the directory you are "in".

| command | meaning |
| --- | --- |
| `cd` |  cd by itself moves you back to your home directory |
| `cd dir_name` | attempts to change the directory you are "in" to the named directory. |
| `cd ..` | moves you up one directory level |

### pwd

The pwd command "prints the working directory" - i.e. it will print the full path of the directory you are "in" right now.

### ls

The ls command prints a "list" of the current directory OR another file system entity if you specify one.

| command | meaning |
| --- | --- |
| `ls`  | lists the contents of the current directory |
| `ls dir_name`  | lists the contents of the indicated directory |

### ls -l

It is possible to modify the operation of various commands using "command line options". The -l (dash el) option to ls causes it to print its "long" listing - details about the contents such as dates and sizes.

### mkdir

You will need to create new folders / directories. This is done with mkdir.

| command | meaning |
| --- | --- |
| `mkdir new_dir_name`  | attempts to create the indicated directory |

### python

Once Python is installed, you can run a Python program like so:

```python program_name``` or

```python program_name arg1 arg2 ... argn```

## Install brew

### Get / install brew

Copy the following, paste it into the terminal and hit enter.

```text
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

You'll need to hit enter to "Continue".

Then you'll need to enter your password. Note that this is being entered in the Terminal - your characters will *not* be echoed back to you so it will look like you are not typing anything. This is normal.

At this point a very *large* amount of data will be downloaded - this first installation will take a very long time. I have a top end MBP and a fast WiFi. For me, this step took only two minutes. For you it may take a long time especially because everyone else is hammering the WiFi at the same time.

`homebrew` or just `brew` is the Mac's "missing package manager". A package manager is software that makes installing other software easier. Unlike everything you've been sold, sometimes the Mac does NOT make things easier. Kool Aid, a childhood treat best left in childhood.

### Add brew to `path`

Commands that can be run from the terminal can live in many different directories for reasons of organization, for example. To specify where the terminal should look for commands, its maintains a `path`. The path is a list of directories the terminal will examine looking for the program you've asked it to run. The path is a list of directories separated by semicolons. 

The directories to Python must be added to your path.

Upon entering the terminal (recall, you are in your home directory), type the following **EXACTLY**. Any deviation will end in tears. Except that Apple hates all Professors and recently renamed the file you need to edit (and changed the Terminal in *many* ways for absolutely no friggin' reason. 

For some of you, the file you need is `.profile`. For others (including those with the latest Macs) the file you need to edit is `.zprofile`. Just because.

To determine which file name you should use, type:

```ls -l .profile```

If you see this: `ls: .profile: No such file or directory`, use `.zprofile`. 

If you see anything like this: `-rw-r--r--  1 yourname  staff  55 Dec 17 14:52 .profile` then continue using `.profile` where I list `.zprofile`.

```vi .zprofile```

Opens the editor `vi`. It is possible this file may be empty. That's OK. Keep right on going.

```G```

Goes to the bottom of the file.

```A```

Enters append mode. If you are not at the beginning of a line, hit enter to start a new line.

Copy this next line and paste it into the terminal.

```export PATH="/usr/local/opt/python/libexec/bin:$PATH"```

Add a new line.

Enter `ESC` - this is not a word, rather a key on your keyboard typically at the top left. Hitting escape leaves the append mode.

```:wq```

Writes the changes to `.zprofile` and exits `vi`.

Type `exit` and hit enter. The current Terminal will exit - they window may stay around - you can close it. We can change this behavior in Terminal's preferences. 

Reenter the Terminal and check to make sure your changes stuck. Type `echo $PATH`. You should get output that lists Python in the first entry. For example:

```text
/usr/local/opt/python/libexec/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

### Install Python

Note that any time `brew` is executed it may choose to update its database. Doing so can take a long time. You'll know it is still working by looking at the title bar of the terminal window. It will change frequently.

```brew install python```

Installing anything can take a long time. 

### Verify Python is installed

To be safe, exit the current Terminal and enter the Terminal again.

Enter:

```python3 --version```

A version of Python, if found, will tell you about itself. I myself did the above on December 17, 2019 and got this:

```text
Python 3.7.3
```

### python3 versus python

It is very likely you will need to explicitly execute `python3` rather than `python`. Same for `pip` - likely must use `pip3`.


### Verify `pip` is installed

Enter `pip3 --version` into the Terminal and hit enter. You should see a version string that refers to Python 3.7 (or later) such as this:

```text
pip 19.0.3 from /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
```

`pip` is the Python package manager. Why have one package manager when you can have 50?

### Python modules first time setup

1. Paste `python3 -m pip install --upgrade pip setuptools wheel` and hit enter. Alert instructor if the last line printed does not include "Successfully".

2. `pip3 install PyPl` and hit enter. Alert instructor if the last line doe snot include "Successfully"

3. Use this [link](https://files.pythonhosted.org/packages/6b/d1/71d3e9cd5e57ff34bd506f815ac0deeaaa655825f41f6fbfbaf8a69886e2/scipy-1.4.0-cp37-cp37m-macosx_10_6_intel.whl). Save the file to your Downloads folder. Wait for the download to finish. **NOTE** Notice the 37 repeated in this file name? It corresponds to having installed Python 3.7.X. If this is not the case, the following will not work and you should alert the instructor. 

4. Back in the command prompt paste `pip3 install Downloads/scipy-1.4.0-cp37-cp37m-macosx_10_6_intel.whl` and hit enter. Alert the instructor if the last line does not include "Successfully".

5. Use this [link](https://files.pythonhosted.org/packages/f7/c5/d2625858ffcc0b5a86557200224be9f1f22a71e5234563d218b6153fb635/scikit_image-0.16.2-cp37-cp37m-macosx_10_6_intel.whl) and  save the file to your Downloads folder. Wait for the download to finish. **NOTE** Notice the 37 repeated in this file name? It corresponds to having installed Python 3.7.X. If this is not the case, the following will not work and you should alert the instructor.

6. Back in the command prompt paste `pip3 install Downloads/scikit_image-0.16.2-cp37-cp37m-macosx_10_6_intel.whl` and hit enter. Alert the instructor if the last line does not include "Successfully".

7. Paste `pip3 install mutagen matplotlib` and hit enter. Alert the instructor if the last line does not include "Successfully".

### Install Visual Studio Code

Use this [link](https://code.visualstudio.com/docs/?dv=osx). You will be downloading the Visual Studio Code package for MacOS.

When you try to open it in Catalina it will fail. Why? Because Steve Jobs.

If this happens:

1. go to Preferences --> Security and Privacy.
2. At the bottom of the dialogue, unlock the settings by clicking on the padlock and enter your password.
3. Click on "Allow apps downloaded from: App Store and identified developers."
4. Run the Visual Studio Code install again. This time you will have the change to "Open".
5. After verifying that you can run Visual Studio Code, you need to move it from your Downloads directory to your Applications folder. In the Finder, right click on Visual Studio Code and select "Copy Visual Studio Code".
6. Click on Applications, and paste. You should hear a stupid 1980's sound.
7. Use Spotlight Search now, to confirm your Visual Studio Code is in the right place. Run Visual Studio Code.
8. Assuming it is now running, right click on its Dock icon. Select Options --> Keep in Dock.

The following is optional - it will allow you to launch VSCode from the Terminal.

Inside VSCode type `↑+⌘+P`.

In the text box, type `shell` you should see `Shell Command: Install 'code' command in PATH`.

Select it.

You should see a dialog at the bottom of the screen which says `Shell command 'code' successfully installed in PATH'.


