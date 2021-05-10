# About NCOVI-FETCH
NCOVI-FETCH is a command-line system information tool written in Python . NCOVI-FETCH displays information about NCOVI statistics in Vietnam(currently).
If you make some change and 
![image](https://user-images.githubusercontent.com/33241024/117637183-c5251d80-b1ab-11eb-8c0c-42b5c281f746.png)

## Windows Install 
The executable for windows is prebuild in "dist" folder. Just go ahead, change directory to this folder and run ncovi-fetch from command line or [add_the_directory_path_to_PATH_environment].

## Linux install
Unforutnally, I don't have an linux machine around, so do compiling yourself and put the executable file to $HOME/bin folder

## Compile yourself
First, install pyinstaller using one of below
 - Using pip to install Pyinstaller by: `"pip install pyinstaller"` (notice that using pip/pip3)
 - Using pip to install from my requirements.txt file: `"pip install -r requirements.txt"`  

Second, compile the code to executable using: `"pyinstaller --onefile ncovi-fetch.py"`
Finally: Make the folder to PATH environment(Windows) or copy the executable file to the bin folder (Linux)


[add_the_directory_path_to_PATH_environment]: <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>
