## @file Equality.py
#  @author Utsharga Rozairo
#  @brief Module that creates an Equality ADT and inherits ABC
#  @date Feb 08, 2020

from abc import ABC, abstractmethod


## @brief An abstract data type for the equality symbol
class Equality(ABC):

    ## @brief An abstract method that defines if the parameter and the self are equal
    #  @param other A parameter of the same type as self, and is used for the comparison
    @abstractmethod
    def __eq__(self, other):
        pass
