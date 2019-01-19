import os

file = open("Installed_Applications.txt", "r")

command = ""
for line in file:
    command = "yes | sudo pacman -S --needed " + line
    # print(command)
    os.system(command);
    command = ""
