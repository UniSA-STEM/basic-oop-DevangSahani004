"""
File: Asset.py
Description: Represents Hacker's Assets as an object, which stores asset data such as name, description etc.
Author: Devang Sahani
ID: 110411585
Username: sahdy004
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    """Represents a digital asset with a name, description, and encryption status."""
    # constructor initialises asset details through private attributes
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    # use of getters to retrieve name and asset description for private visibility
    def get_name(self):
        return self.__name

    def get_asset_description(self):
        return self.__description

    # ensures encryption of assets in hacker.py
    def is_encrypted(self):
        return self.__encrypted

    # used as setter to set status of assets with encryption and decryption
    def encrypt_asset(self):
        self.__encrypted = True

    def decrypt_asset(self):
        self.__encrypted = False

    # string conversion method to display encryption or not on output to user
    def __str__(self):
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"