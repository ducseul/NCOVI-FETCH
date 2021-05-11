# About NCOVI-FETCH
NCOVI-FETCH is a command-line system information tool written in Python . NCOVI-FETCH displays information about NCOVI statistics in Vietnam(currently), summary over the world and other specific country (option).
![image](https://user-images.githubusercontent.com/33241024/117861171-5636ea00-b2bb-11eb-97b0-acb18bb5326f.png)

## How to use
![image](https://user-images.githubusercontent.com/33241024/117861270-72d32200-b2bb-11eb-91c2-cac886c121ae.png)  
Easy to use. Just type in `"ncovi-fetch"`, you will get the data about Vietnam and WorldWide summary
 - Use `ncovi-fetch -c "country name"` to get statitics of other more country. The other country can be search with `--search (-s)` parameter
![image](https://user-images.githubusercontent.com/33241024/117861667-de1cf400-b2bb-11eb-8aa7-91f47ec17a3e.png)

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
