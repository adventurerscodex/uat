"""Encounter Factories."""

import factory

from factories.fixtures import random_wordlist


"""EncounterAddEditModal Factory."""


class EncounterAddEditModal:
    """EncounterAddEditModal model."""

    def __init__(
        self,
        encounter_name,
        location
    ):
        """Initialize EncounterAddEditModal instance."""
        self.encounter_name = encounter_name
        self.location = location


class EncounterAddEditModalFactory(factory.Factory):
    """Definition of EncounterAddEditModal factory."""

    class Meta:
        """Bind model to factory."""

        model = EncounterAddEditModal

    encounter_name = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='EncounterName_')
    )

    location = factory.Faker(
        'word',
        ext_word_list=random_wordlist(max_length=40, prefix='Location_')
    )
