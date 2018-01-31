"""Coins components."""

from modules.element import Element, Component


class Coins(Component):
    """Definition of coins component."""

    platinum = Element(id_='coinsPlatinumInput')
    gold = Element(id_='coinsGoldInput')
    electrum = Element(id_='coinsElectrumInput')
    silver = Element(id_='coinsSilverInput')
    copper = Element(id_='coinsCopperInput')
