from os import mkdir 
from os import rmdir 
from os import listdir
from os.path import abspath, isdir
import io
from io import open

directory_path = '..\\'
mkdir('.\\new_directory') 
rmdir('.\\new_directory') 
listdir('.\\File_handling') 

abspath('file_name') 

isdir('.\\new_directory') 