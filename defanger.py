# Defanger - Python 3 - Malcolm Krolick

from tkinter.filedialog import Open


with open("sites.txt", 'r') as f:
    new_sites = []
    sites = f.read().splitlines()
    for site in sites:
        new_sites.append(site.replace(".", "[.]").replace("http", "hXXp"))

with open("defanged_sites.txt", 'a') as f:
    f.write("-----------------------------------------------------------------------------------------\n")
    for site in new_sites:
        f.write(site + "\n")    
