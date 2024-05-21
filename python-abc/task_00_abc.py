#!/usr/bin/env python3
"""
Nameless Module
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    abstract class Animal
    """

    @abstractmethod
    def sound(self):
        """
        abstract method sound
        """
        pass


class Dog(Animal):
    """
    subclass Dog
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    subclass Cat
    """

    def sound(self):
        return "Meow"
