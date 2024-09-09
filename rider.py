"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
WAITING: A constant used for the waiting rider status.
CANCELLED: A constant used for the cancelled rider status.
SATISFIED: A constant used for the satisfied rider status
"""

from location import Location

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:

    """A rider for a ride-sharing service.
    === Attributes ===
    patience: The patience of the rider
    destination: destination of the rider
    identifier: An identifier for the person doing the activity.
    id: an indentifier

    origin The original location of the rider.
    """

    #
    id: str
    patience: int
    origin: Location
    destination: Location
    status: str

    def __init__(self, identifier: str, patience: int, origin: Location,
                 destination: Location) -> None:
        """Initialize a Rider.

        """
        self.id = identifier
        self.patience = patience
        self.origin = origin
        self.destination = destination
        self.status = WAITING

    def cancel(self) -> None:
        """ sets status of rider to cancel
        """
        self.status = CANCELLED

    def waiting(self) -> None:
        """ sets status of rider to waiting
        """
        self.status = WAITING

    def satisfied(self) -> None:
        """ sets status of rider to satisfied
        """
        self.status = SATISFIED


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={'extra-imports': ['location']})
