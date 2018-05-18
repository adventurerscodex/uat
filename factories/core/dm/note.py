"""Note factory."""

import factory


class Note:
    """Definition of Note model."""

    def __init__(
        self,
        note,
    ):
        """Initialize Note instance."""
        self.note = note


class NoteFactory(factory.Factory):
    """Definition of Note factory."""

    class Meta:
        """Bind model to factory."""

        model = Note

    note = factory.Faker(
        'text',
        max_nb_chars=15
    )
