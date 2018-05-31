"""Coins components."""

from component_objects import Component, Element


class Coins(Component):
    """Definition of coins component."""

    platinum_id = 'coinsPlatinumInput'
    gold_id = 'coinsGoldInput'
    electrum_id = 'coinsElectrumInput'
    silver_id = 'coinsSilverInput'
    copper_id = 'coinsCopperInput'
    worth_in_gold_id = 'coinsWorthInGoldLabel'
    total_weight_id = 'coinsTotalWeightLabel'

    platinum = Element(id_=platinum_id)
    gold = Element(id_=gold_id)
    electrum = Element(id_=electrum_id)
    silver = Element(id_=silver_id)
    copper = Element(id_=copper_id)
    worth_in_gold = Element(id_=worth_in_gold_id)
    total_weight = Element(id_=total_weight_id)
