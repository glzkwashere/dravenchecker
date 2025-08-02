# main.py 
# created by KnownAsGlzk

import os
import time

appdata = os.getenv('APPDATA')
if not os.path.exists(appdata):
    print("wtf")

minecraft_path = os.path.join(appdata, '.minecraft')
if os.path.exists(minecraft_path):
 print(f"found minecraft folder {minecraft_path}")
else:
 print("minecraft folder not found. either you renamed it or you use incompatible launcher")

minecraft_path = os.path.join(appdata, '.tlauncher', 'legacy', 'Minecraft', 'game')
if not os.path.exists(minecraft_path):
    minecraft_path = os.path.join(appdata, '.tlauncher', 'Minecraft', 'game')
    if os.path.exists(minecraft_path):
        print(f"found legacy launcher folder {minecraft_path}")

hacks = ["meteor", "baritone","impact","wurst"]
found_hacks = []
print("checking")
for hack in hacks:
        for root, dirs, files in os.walk(minecraft_path,hack):
            for name in files:
                if hack.lower() in name.lower():
                    found_hacks.append(hack)
            for name in dirs:
                if hack.lower() in name.lower():
                    found_hacks.append(hack)
if found_hacks:
            print("ggs.")
            for hack in found_hacks:
                print(f"found {hack}");
            test = input("press enter to exit")
            exit(0)
else:
    print("no hacks have been found wow")