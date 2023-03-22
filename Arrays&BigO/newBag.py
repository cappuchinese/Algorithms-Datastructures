"""
#TODO 30-03-22 lisah: programme description
"""

__author__ = "Lisa Hu"
__date__ = 03.2022

# IMPORTS
import random


class Bag:
    """
    An unsorted and unordered collection of items:
        Items can be added;
        Items can be duplicates;
        Items can be removed;
        Items can be called randomly WITHOUT removing them.
    """
    def __init__(self):
        """
        Constructor
        """
        self.items = []

    def get_item(self):
        """
        Returns random item from internal list
        """
        random.seed()
        i = random.randint(0, len(self.items) - 1)
        return self.items[i]

    def add_item(self, item):
        """
        Add an item to the internal list
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Remove the item from the internal list
        """
        if item in self.items:
            self.items.remove(item)


class GrabBag(Bag):
    """
    A Bag that ALWAYS deletes the returned item
    """
    def get_item(self):
        """
        Get a random item from the internal list and delete this from the collection
        """
        item = super().get_item()
        super().remove_item(item)
        return item


class MaxBag(Bag):
    """

    """