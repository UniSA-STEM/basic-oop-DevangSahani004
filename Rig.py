"""
File: Rig.py
Description: Represents the hacker's workstation. This is the driver to all the magic it performs.
Author: Devang Sahani
ID: 110411585
Username: sahdy004
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Asset import Asset


class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage = [Asset("Data Spike", "Used for battles"), Asset("Data Spike", "Used for battles"), Asset("Removable Drive", "Used for extraction")]
        self.__upgrade_level = 0


    def get_name(self):
        return self.__name

    def get_storage(self):
        return self.__storage

    def get_upgrade_level(self):
        return self.__upgrade_level

    def get_damage(self):
        return self.__damage

    def is_broken(self):
        return self.__broken

    def repair_rig(self):
        if self.__damage == 0:
            print(f"The rig, {self.__name}, has no damage. No repair is required!")
            return

        for asset in self.__storage:
            if asset.get_name() == "CryptoToken":
                self.__storage.remove(asset)
                self.__damage = 0
                self.__broken = False
                print(f"The rig, {self.__name}, has been repaired using a CryptoToken.")
                return

        print(f"Rig repair failed! No CryptoToken was found in {self.__name}'s storage.")

    def upgrade_rig(self):
        for asset in self.__storage:
            if asset.get_name() == "Hardware Patch":
                self.__storage.remove(asset)
                self.__upgrade_level += 1
                print(f"{self.__name} upgraded to {self.__upgrade_level} level. Amazing!")
                return
        print(f"Upgrade failed. No Hardware Patch was found in {self.__name}'s storage.")

    def take_hits(self):
        self.__damage += 1
        hits_threshold = max(1, 2 - self.__upgrade_level)

        if self.__damage >= hits_threshold:
            self.__broken = True
            print(f"The rig, {self.__name}, has broke. Repairs are required!.")
        else:
            print(f"The rig, {self.__name}, took a hit. It currently has {self.__damage} damages.")

    def generate_asset(self):
        asset_options = [
            Asset("CryptoToken", "Required to acquire or repair damaged rigs."),
            Asset("Data Spike", "Used for battles."),
            Asset("Removable Drive", "Used for extraction."),
            Asset("Security Chip", "Used to encrypt or decrypt assets in the rig."),
            Asset("Hardware Patch", "Used for upgrade rigs."),
        ]

        random_asset = random.choice(asset_options)
        self.__storage.append(random_asset)
        print(f"Rig {self.__name} randomly generated a asset, {random_asset.get_name()}.")

    def store_asset(self, asset):
        if asset.is_encrypted():
            print("Failed to store asset. Asset is encrypted.")
            return
        self.__storage.append(asset)
        print(f"The asset {asset.get_name()} has been stored.")

    def release_asset(self, asset):
        if asset.is_encrypted():
            print(f"Failed to release asset {asset.get_name()}. Asset is encrypted.")
            return None
        if asset in self.__storage:
            self.__storage.remove(asset)
            print(f"The asset {asset.get_name()} has been released from {self.__name}.")
            return asset
        print(f"Asset {asset.get_name()} was not found in {self.__name}'s storage.")
        return None

    def __str__(self):
        if self.__broken:
            condition = "Broken"
        elif self.__damage == 0:
            condition = "Pristine"
        else:
            condition = "Damaged!"


        stored_assets = []
        for asset in self.__storage:
            stored_assets.append(asset.get_name())

        if stored_assets:
            assets = ", ".join(stored_assets)
        else:
            assets = "None assets stored!"


        return(
            f"\n|---------------- Rig Details ----------------|\n"
            f"Rig Name: {self.__name}\n"
            f"Condition: {condition} (Level {self.__upgrade_level})\n"
            f"Stored Assets: {assets}\n"
            f"|--------------------------------------------|\n"
        )