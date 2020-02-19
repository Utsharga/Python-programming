## @file Set.py
#  @author Utsharga Rozario
#  @brief Module that creates a Set ADT
#  @date Feb 08, 2020

from Equality import *


## @brief An abstract data type that represents a set
class Set(Equality):

    ## @brief Set Constructor
    #  @details Initializes a Set of objects
    #  @param S A List of objects
    def __init__(self, s):
        self.S = s

    ## @brief Checks if both the Sets are equal
    #  @details Checks if the current set and the parameter set are both of the same length
    #           and then if elements in both the sets are equal
    #  @param other A Set ADT
    #  @return True if the length and the elements are the same, False otherwise
    def __eq__(self, other):
        if (len(other.S) == len(self.S)):
            for e in self.S:
                if not other.member(e):
                    return False
            return True
        return False

    ## @brief Adds an object to the list
    #  @param e an element data to be added
    def add(self, e):
        self.S.append(e)

    ## @brief Removes an element from the set
    #  @details Uses the member function to determine if the element is in the list
    #           then removes the element if present
    #  @param e an element data to be removed
    #  @throw ValueError if the element is not present in the list hence cannot be removed
    def rm(self, e):
        self.S.remove(e)

    ## @brief Checks if the element in the Set
    #  @param e an element data
    #  @return True if e is present in list S
    def member(self, e):
        if e in self.S:
            return True
        return False

    ## @brief Returns the size of the list
    #  @return The length of the list
    def size(self):
        return len(self.S)

    ## @brief Checks if both the Sets are equal
    #  @details Checks if the current set and the parameter set are both of the same length
    #           and then if elements in both the sets are equal
    #  @param R A Set ADT
    #  @return True if the length and the elements are the same, False otherwise
    def equals(self, r):
        if (len(r.S) == len(self.S)):
            for e in self.S:
                if not r.member(e):
                    return False
            return True
        return False

    ## @brief Returns a sequence of elements in the set
    #  @return List of elements in the set
    def to_seq(self):
        sequence = []
        for e in self.S:
            sequence.append(e)
        return sequence

    ## @brief Set index to start of the set
    def __iter__(self):
        self.index = 0
        return self

    ## @brief Obtain value at current index and increase i value
    #  @return Value at current index
    #  @throw StopIteration Stops iterating when list out of range
    def __next__(self):
        if self.size() > self.index:
            element = self.to_seq()[self.index]
            self.index = self.index + 1
            return element
        else:
            raise StopIteration
