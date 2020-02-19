## @file CompoundT.py
#  @author Utsharga Rozario
#  @brief Module that creates a CompoundT ADT
#  @date Feb 08, 2020

from Set import *
from ChemEntity import *
from ElmSet import *
from MolecSet import *
from MoleculeT import *


## @brief an Abstract Data Type that resemblems a compound
class CompoundT(ChemEntity, Equality):

    ## @brief Molecule Constructor
    #  @details Initializes a CompoundT object with an MolecSet of MoleculeT
    #  @param M Element in the molecule
    def __init__(self, m):
        self.C = m

    ## @brief Checks if both the compound are equal
    #  @details Checks if the current compound and the parameter compound have the same
    #           number of molecules and the same element of molecules
    #  @param other CompoundT ADT
    #  @return True if the Molecule and number of atoms of the element are the same,
    #          False otherwise
    def __eq__(self, other):
        if (self.C.equals(other.get_molec_set())):
            return True
        else:
            return False

    ## @brief Get the elements in compound and returns an ElmSet of it
    #  @return ElmSet of the elements in the compound
    def constit_elems(self):
        listelm = []
        for m in self.C.S:
            listelm.append(m.get_elm())
        return ElmSet(listelm)

    ## @brief Gets the molecule set of the compound
    #  @return The molecule set of the compound
    def get_molec_set(self):
        return self.C

    ## @brief Checks if both the compound are equal
    #  @details Checks if the current compound and the parameter compound have the same
    #           number of molecules and the same element of molecules
    #  @param other CompoundT ADT
    #  @return True if the Molecule and number of atoms of the element are the same,
    #          False otherwise
    def equals(self, d):
        if (self.C.equals(d.get_molec_set())):
            return True
        else:
            return False

    ## @brief Gets the number of atoms of the parameter element in the compound
    #  @param e ElementT type parameter
    #  @return The number atoms of the element in the Compound
    def num_atoms(self, e):
        atoms = 0
        for mol in self.C.S:
            atoms += mol.num_atoms(e)
        return atoms
