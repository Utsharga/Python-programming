## @file ChemEntity.py
#  @author Utsharga Rozario
#  @brief Module that creates a MoleculeT ADT
#  @date Feb 08, 2020

from abc import ABC, abstractmethod
from ChemTypes import *
from ElmSet import *


## @brief an Abstract Data Type that resemblems a chemical entity
class ChemEntity(ABC):

    ## @brief Gets the number of atoms of the parameter element in the molecule
    #  @param e ElementT type parameter
    #  @return The number atoms of the element in a chemical entity
    @abstractmethod
    def num_atoms(self, e):
        pass

    ## @brief Get the element in the molecule and returns an ElmSet of it
    #  @return ElmSet of the elements in a chemical entity
    @abstractmethod
    def constit_elems(self):
        pass
