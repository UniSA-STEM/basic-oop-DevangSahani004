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

    def upgrade_rig(self):
        if self.__rig is None:
            print("Upgrade failed: No rig found allocated to hacker!")
            return

        for patch in self.__inventory:
            if patch.get_name() == "Hardware Patch":
                self.__rig.upgrade_rig()
                self.__inventory.remove(patch)
                print(f"Rig {self.__rig.get_name()} upgraded to level {self.__rig.get_upgrade_level()}.")
                return
        print("Upgrade failed: No Hardware Patch found in inventory.")

    def launch_data_spike(self, target_rig):
        if self.__rig is None:
            print("Launch failed: No rig equipped.")
            return

        for asset in self.__rig.get_storage():
            if asset.get_name() == "Data Spike":
                self.__rig.get_storage().remove(asset)
                target_rig.take_hits()
                self.increase_trace_level()
                print(f"{self.__name} launched a Data Spike at {target_rig.get_name()}.")
                return
        print("Launch failed: No Data Spike in rig storage.")

    def encrypt_asset(self, asset):
        for chip in self.__inventory:
            if chip.get_name() == "Security Chip":
                asset.encrypt_asset()
                self.__inventory.remove(chip)
                print(f"{asset.get_name()} has been encrypted.")
                return
        print("Encryption failed: No Security Chip available.")

    def decrypt_asset(self, asset):
        for chip in self.__inventory:
            if chip.get_name() == "Security Chip":
                asset.decrypt_asset()
                self.__inventory.remove(chip)
                print(f"{asset.get_name()} has been decrypted.")
                return
        print("Decryption failed: No Security Chip available.")

    def transfer_asset(self, asset):
        if asset.is_encrypted():
            print("Transfer failed: Asset is encrypted and cannot be transferred.")
            return
        if self.__rig:
            self.__rig.store_asset(asset)
            self.remove_from_inventory(asset)
            self.increase_trace_level()
            print(f"{asset.get_name()} transferred to rig {self.__rig.get_name()}.")
        else:
            print("Transfer failed: No rig equipped allocated to hacker.")

    def scan_inventory(self, asset_name):
        for asset in self.__inventory:
            if asset.get_name() == asset_name:
                self.__inventory.remove(asset)
                print(f"Asset {asset_name} was found and has been removed from the inventory!")
                return asset
        print(f"Asset {asset_name} does not exist in the inventory.")
        return None

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