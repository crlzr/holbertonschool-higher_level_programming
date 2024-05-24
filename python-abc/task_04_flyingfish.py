#!/usr/bin/env python3
"""
Multiple inheritance
"""


class Fish:
    """
    class Fish
    """
    def swim(self):
        """
        method swim
        """
        print("The fish is swimming!")

    def habitat(self):
        """
        method habitat
        """
        print("The fish lives in the water")


class Bird:
    """
    class Bird
    """
    def fly(self):
        """
        method fly
        """
        print("The bird is flying")

    def habitat(self):
        """
        method habitat
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    subclass inheriting from Fish and Bird
    """
    def fly(self):
        """
        overwritten fly method
        """
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        """
        overwritten habitat method
        """
        print("The flying fish lives both in water and the sky!")

    def __init__(self):
        """
         Constructor for flying fish
        """
        pass
