#!/usr/bin/env python3
"""
The Mystical Dragon - Mastering Mixins
"""


class SwimMixin:
    """
    SwimMixin
    """

    def swim(self):
        """
        swim method
        """
        print("The creature swims!")


class FlyMixin:
    """
    FlyMixin
    """

    def fly(self):
        """
        fly method
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    subclass Dragon
    """

    def roar(self):
        """
        method roar
        """
        print("The dragon roars!")


"""
draco = Dragon()

draco.swim()
draco.fly()
draco.roar()
"""
