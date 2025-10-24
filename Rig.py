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
    """
    Rig represents the computer that is utilised by hackers to perform their magic in the simulation.
    A rig can only be acquired by hacker when a CryptoToken is available to them.
    Every rig is determined with a name, damage level, current state, upgrade level and assets.
    Has capability to generate assets upon initialisation.
    """
    def __init__(self, name):

        # upon instantiation, the rig is given pre-defined data through private visibility
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage = [Asset("Data Spike", "Used for battles"), Asset("Data Spike", "Used for battles"), Asset("Removable Drive", "Used for extraction")]
        self.__upgrade_level = 0

    # which are further retrieved from these getter methods.
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

    # repair rig provides capability to ensure if the rig has damage or not
    # upon validating its damage, it can repair itself through the use of a CryptoToken.
    # in return, it will reset rig damage and update its condition status.
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

    # capability to upgrade the rig's stability when taking hits.
    # An upgrade is performed upon validating that the inventory has a hardware patch.
    def upgrade_rig(self):
        for asset in self.__storage:
            if asset.get_name() == "Hardware Patch":
                self.__storage.remove(asset)
                self.__upgrade_level += 1
                print(f"{self.__name} upgraded to {self.__upgrade_level} level. Amazing!")
                return
        print(f"Upgrade failed. No Hardware Patch was found in {self.__name}'s storage.")

    # when in simulation, the rig takes hit through this function.
    # if damage level of this rig goes beyond its threshold, it will return a broken state for its condition.
    def take_hits(self):
        self.__damage += 1
        hits_threshold = max(1, 2 - self.__upgrade_level)

        if self.__damage >= hits_threshold:
            self.__broken = True
            print(f"The rig, {self.__name}, has broke. Repairs are required!.")
        else:
            print(f"The rig, {self.__name}, took a hit. It currently has {self.__damage} damages.")

    # using random, this function has a set of 5 options.
    # When instantiated, the rig will generate and keep it within its storage.
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

    # this function allows the rig to store passed in asset to its storage.
    # it will not store if its encrypted.
    def store_asset(self, asset):
        if asset.is_encrypted():
            print("Failed to store asset. Asset is encrypted.")
            return
        self.__storage.append(asset)
        print(f"The asset {asset.get_name()} has been stored.")

    # rig has the capability to release an asset stored within its storage if not encrypted.
    # however, if the asset is encrypted, this function will not work.
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


    # a string conversion method that will return a formatted string that is visually appealing.
    # provides informative data neatly such as rig's name, condition and stored assets.
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