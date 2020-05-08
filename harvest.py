############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.pairings = []
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings = self.pairings.append(pairings)
        return self.pairings

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = self.new_code
        return self.code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
# code, first_harvest, color, is_seedless, is_bestseller, 
#                  name)
    # Fill in the rest
    "Muskmelon" = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    "Casaba" = MelonType("cas", 2003, "orange", False, False, "Casaba")
    "Crenshaw" = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    "Yellow Watermelon" = MelonType("yw", 2013, "yellow", False, False, "Yellow Watermelon")
    for melon in MelonType:
        all_melon_types.append(melon)
    print(all_melon_types)

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        melon = self.name.upper()
        print(f'{self.name} pairs well with {self.pairings}.')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



