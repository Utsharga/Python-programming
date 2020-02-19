## @file MoleculeT.py
#  @author Utsharga Rozario
#  @brief Module that creates a MoleculeT ADT
#  @date Feb 08, 2020

from Equality import *
from ChemEntity import *
from ElmSet import *


## @brief an Abstract Data Type that resemblems a molecule
class MoleculeT(ChemEntity, Equality):

    ## @brief Molecule Constructor
    #  @details Initializes a MoleculeT object with an element and number of atoms of the
    #           element
    #  @param num Number of atoms of the element in the molecule
    #  @param elm Element in the molecule
    def __init__(self, num, elm):
        self.num = num
        self.elm = elm

    ## @brief Checks if both the molecules are equal
    #  @details Checks if the current molecule and the parameter molecule are both of the
    #           same element and has the same the number of atoms
    #  @param other MoleculeT ADT
    #  @return True if the element and number of atoms of the element are the same,
    #          False otherwise
    def __eq__(self, other):
        if (self.elm == other.get_elm() and self.num == other.get_num()):
            return True
        else:
            return False

    ## @brief Checks if both the molecules are equal
    #  @details Checks if the current molecule and the parameter molecule are both of the
    #           same element and has the same the number of atoms
    #  @param other MoleculeT ADT
    #  @return True if the element and number of atoms of the element are the same,
    #          False otherwise
    def equals(self, m):
        if (self.elm == m.get_elm() and self.num == m.get_num()):
            return True
        else:
            return False

    ## @brief Gets the element in the molecule
    #  @return Element of the molecule
    def get_elm(self):
        return self.elm

    ## @brief Gets the number of atoms in the molecule
    #  @return Number of atoms in the molecule
    def get_num(self):
        return self.num

    ## @brief Gets the number of atoms of the parameter element in the molecule
    #  @param e ElementT type parameter
    #  @return The number atoms of the element in the Molecule
    def num_atoms(self, e):
        if (e == self.elm):
            return self.num
        else:
            return 0

    ## @brief Get the element in the molecule and returns an ElmSet of it
    #  @return ElmSet of the element in the molecule
    def constit_elems(self):
        return ElmSet([self.elm])
