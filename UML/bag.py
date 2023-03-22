"""This module implements a Bag and a GrabBag"""
import random


class Bag:
    """
    Een ongesorteerde en ongeordende collectie van items,
        waaraan items toegevoegd kunnen worden,
        waarin duplicaten zijn toegestaan,
        waaruit items verwijderd kunnen worden,
        waaruit een willekeurig item opgevraagd kan worden. Het wordt dan NIET verwijderd.
    """

    def __init__(self):
        """constructor"""
        self.items = []

    def get_item(self):
        """geeft een willekeurig item uit de interne lijst terug
            output: willekeurig item uit self.items
        """
        random.seed()
        i = random.randint(0, len(self.items) - 1)
        return self.items[i]

    def add_item(self, item):
        """voegt een item toe aan de interne lijst
            input: toe te voegen item
        """
        self.items.append(item)

    def remove_item(self, item):
        """verwijdert een item uit de interne lijst"""
        if item in self.items:
            self.items.remove(item)


class GrabBag(Bag):
    """Een soort Bag waar opgevraagde items ALTIJD uit verwijderd worden"""

    def get_item(self):
        """geeft een willekeurig item uit de interne lijst terug en verwijdert
           dit uit de interne collectie
           output: willekeurig item uit self.items
        """
        item = super().get_item()
        super().remove_item(item)
        return item


class MaxBag(Bag):
    """een bag waarvan je makkelijk de grootste aanwezige waarde kunt bepalen (in O(1))"""

    def __init__(self):
        """constructor. Add a field for the maximal value"""
        self.max = None
        super().__init__()

    def get_max_value(self):
        """return the maximal value in the Bag"""
        return self.max

    def add_item(self, item):
        """if the added item > max, we should change max as well!"""
        if not self.max or self.max < item:
            self.max = item
        super().add_item(item)
