"""
File: Asset.py
Description: Represents Hacker's Assets as an object, which stores asset data such as name, description etc.
Author: Devang Sahani
ID: 110411585
Username: sahdy004
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_name(self):
        return self.__name

    def get_asset_description(self):
        return self.__description

    def is_encrypted(self):
        return self.__encrypted

    def encrypt_asset(self):
        self.__encrypted = True

    def decrypt_asset(self):
        self.__encrypted = False

    def __str__(self):
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"