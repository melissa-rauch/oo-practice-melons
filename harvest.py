############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
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
        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code
        print(F'Code updated to {new_code}')
        return self.code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType("Muskmelon","musk", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casa = MelonType("Casaba", "cas", 2003, "orange", False, False)
    casa.add_pairing("mint")
    all_melon_types.append(casa)
    
    cren = MelonType("Crenshaw", "cren", 1996, "green", False, False)
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yel_wa = MelonType("Yellow Watermelon", "yw", 2013, "yellow", False, False)
    yel_wa.add_pairing("ice cream")
    all_melon_types.append(yel_wa)

    print(all_melon_types)

make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f' {melon_name} pairs with')
        for pairing in melon_types:
            print(f'{self.name} pairs well with {self.pairings}.')
        print()

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



