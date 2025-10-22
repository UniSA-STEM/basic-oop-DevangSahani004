"""
File: Rig.py
Description: Represents the hacker's workstation. This is the driver to all the magic it performs.
Author: Devang Sahani
ID: 110411585
Username: sahdy004
This is my own work as defined by the University's Academic Misconduct Policy.
"""
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
        pass

    def upgrade_rig(self):
        pass

    def take_hits(self):
        pass

    def generate_asset(self):
        pass

    def store_asset(self):
        pass

    def release_asset(self):
        pass

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