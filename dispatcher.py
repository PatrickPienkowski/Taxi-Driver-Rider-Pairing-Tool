"""Dispatcher for the simulation"""

from typing import Optional
from driver import Driver
from rider import Rider


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.

    """
    # === Private Attributes ===
    _drivers: list
    # List of all drivers
    _riders: list
    # List of all riders

    def __init__(self) -> None:
        """Initialize a Dispatcher.

        """
        self._drivers = []
        self._riders = []

    def __str__(self) -> str:
        """Return a string representation.

        """
        return f"The available drivers are {self._drivers}"

    def request_driver(self, rider: Rider) -> Optional[Driver]:
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        """
        k = False
        for i in self._drivers:
            if i.is_idle:
                k = True
                break
        if k:
            c = self.find_driver(rider)
            return c
        else:
            self._riders.append(rider)
            return None

    def find_driver(self, rider: Rider) -> Driver:
        """get the closest driver"""
        b = None
        c = None
        for driver in self._drivers:
            if b is None and driver.is_idle:
                b = driver.get_travel_time(rider.origin)
                c = driver
            if b is not None:
                if driver.get_travel_time(rider.origin) < b \
                        and driver.is_idle:
                    b = driver.get_travel_time(rider.origin)
                    c = driver
        return c

    def request_rider(self, driver: Driver) -> Optional[Rider]:
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        """
        if driver not in self._drivers:
            self._drivers.append(driver)
        if self._riders:
            driver.is_idle = False
            return self._riders.pop(0)
        else:
            return None

    def cancel_ride(self, rider: Rider) -> None:
        """Cancel the ride for rider.

        """
        if rider in self._riders:
            self._riders.remove(rider)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={'extra-imports': ['typing', 'driver', 'rider']})
