# slesinger-lab-projects
batch plotter for now, more to follow  
this readme will serve as the batch plotter protocol for Gauri (hi gauri!!)  
i will make improvements as time passes, and upload them here  


## Python Setup
To run this project, you will need Python 3.14  
Go to https://www.python.org/downloads/, select version 3.14, and follow the instructions  
IMPORTANT: When installing, make sure to let the installer install pip and add it to your path  

## Installing VSCode
You can technically run python programs through the terminal, but its a bit of a pain  
We can get around this by installing VSCode, which allows you to run any programs you have through its own terminal (shows up as a little play button on the upper right hand of the screen  
Go to https://code.visualstudio.com/ and follow the instructions


## Installing Libraries
To get started, you need to install a number of libraries:  
*pyabf  
*matplotlib  
*numpy  


To install them, go to the command line and write:  
*python -m pip install pyabf matplotlib numpy  

## Creating Input and Output Folders
After installing dependencies, the plotter is _almost_ ready to go, it just needs two things on your end:  
The plotter needs an _input folder_, which contains the actual recording files, and an _output folder_, where completed plots will be deposited  
These folders can just live on your desktop, and you can name them whatever you want

## Feeding Folder Paths to the Plotter
After creating your input and output folders, you need to pass the locations of those folders to the plotter  
This happens in 2 lines: Line **74** (input) and line **86** (output)  
Right click on your designated **input** folder on your desktop (or wherever you put it), and select "copy as path"  
Go to line 74 of the program and replace the text surrounding the hashtags (INCLUDING THE HASHTAGS DO NOT LEAVE THEM IN) with your path  
Type a single lowercase letter "r" in front of the path  
The finished result will look something like **r"C:\Users\joego\Desktop\batchPlotterInput"**  
Repeat with your designated **output** folder on line 86  









