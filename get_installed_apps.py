# Simple script to get all of the installed applications 
# and store in a text file
import os

os.system("pacman -Qqe > appsv1.txt")
