import os

description = input("Description :- ")

os.system("git add .")
os.system("git status")
command = "git commit -m '" + description + "'"
os.system(command)
os.system("git push")