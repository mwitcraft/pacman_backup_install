# Opens the installed applications file and downloads any missing
# or out of date apps
import os

# Opens the list of installed applications
file = open("Installed_Applications.txt", "r")

command = ""
# Installs the applications, if needed
for line in file:
    # 'yes' automatically chooses 'y' when prompted
    command = "yes | sudo pacman -S --needed " + line
    os.system(command);
    command = ""
