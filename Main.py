"""
File: main.py
Description: Represents a key to running the program using Hacker, Asset & Rig.py as a library. Contains all test cases.
Author: Devang Sahani
ID: 110411585
Username: sahdy004
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig
from Asset import Asset


hacker = Hacker("NoTrailz")
print(hacker)

rig = Rig("SilentKilla")
hacker.acquire_rig(rig)
print(hacker)

rig.generate_asset()
rig.generate_asset()
print(rig)

locate_asset = None
hacker.get_inventory().append(Asset("Security Chip", "Used for encryption"))

for asset in rig.get_storage():
    if asset.get_name() == "Removable Drive":
        locate_asset = asset

if locate_asset is not None:
    hacker.encrypt_asset(locate_asset)
else:
    print("Removable Drive is not in rig storage. Try again!")

locate_asset = None
hacker.get_inventory().append(Asset("Security Chip", "Used for encryption"))

for asset in rig.get_storage():
    if asset.get_name() == "Removable Drive":
        locate_asset = asset

if locate_asset is not None:
    hacker.decrypt_asset(locate_asset)
else:
    print("Removable Drive is not in rig storage. Try again!")

rig.take_hits()
rig.take_hits()
print(rig)

hacker.get_inventory().append(Asset("CryptoToken", "Used for repair"))
rig.repair_rig()
print(rig)