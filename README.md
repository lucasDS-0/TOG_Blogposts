# TOG Blogposts
This is a (WIP) web scraper to read SIU's (GOAT's) blogposts for each chapter.

This is based on info in the [TOG Wiki](https://towerofgod.fandom.com/wiki/Tower_of_God_Wiki), up to 2022/03/12.

## Script usage

On a command console run the script by typing 
```Python
python3 main.py --volume X --chapter Y
```
where `--volume` and `--chapter` are self-explanatory optional parameters.

## Installation

A setup file is available so the script can be installed and used anywhere.
For this purpose, run the following command
```Shell
pip install -e /path/to/script/folder
```
after that, just run 
```Shell
togblog --volume X --chapter Y
```