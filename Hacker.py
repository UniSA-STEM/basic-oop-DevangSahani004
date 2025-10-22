"""
File: Hacker.py
Description: Represents hacker as an object, which can obtain a rig and perform data spikes.
Author: Devang Sahani
ID: 110411585
Username: sahdy004
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# imports
from Asset import Asset

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = [Asset("CryptoToken", "Required to acquire or repair damaged rigs.")]
        self.__rig = None
        self.__trace_level = 0

    def get_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_trace_level(self):
        return self.__trace_level

    def set_rig(self, rig):
        self.__rig = rig

    def increase_trace_level(self):
        self.__trace_level += 1

    def reset_trace_level(self):
        self.__trace_level = 0

    def add_to_inventory(self, asset):
        self.__inventory.append(asset)

    def remove_from_inventory(self, asset):
        self.__inventory.remove(asset)

    def acquire_rig(self, rig):
        for asset in self.__inventory:
            if asset.get_name() == "CryptoToken":
                self.__inventory.remove(asset)
                self.__rig = rig
                print(f"Hacker {self.__name} has acquired rig {rig.get_name()} and is now activated!")
                return
        print("Acquisition failed: No CryptoToken in inventory.")

    def launch_data_spike(self, target_rig):
        pass

    def __str__(self):
        if self.__rig:
            rig_name =  self.__rig.get_name()
        else:
            rig_name = "Rig not found!"

        inventory_list = []
        for asset in self.__inventory:
            inventory_list.append(str(asset))

        if inventory_list:
            inventory_text = "\n".join(inventory_list)
        else:
            inventory_text = "No Inventory Found!"

        return (
        f"\n|---------------- Hacker Details ----------------|\n"
        f"Hacker Name: {self.__name}\n"
        f"Rig: {rig_name}\n"
        f"Trace Level: {self.__trace_level}\n"
        f"Inventory: {inventory_text}\n"
        f"|------------------------------------------------|\n"
        )