## @file ReactionT.py
#  @author Utsharga Rozario
#  @brief Module that creates a ReactionT ADT
#  @date Feb 08, 2020

import numpy as np


## @brief an Abstract Data Type that resemblems a chemical reaction
class ReactionT:

    ## @brief Reaction Constructor
    #  @details Initializes a CompoundT object with an MolecSet of MoleculeT
    #  @param l A Sequence of Compounds Representing the left side of the reaction
    #  @param r A Sequence of Compounds Representing the right side of the reaction
    #  @throws ValueError if the coefficients of the compounds are negative or
    #          the reaction is not balanced by the produced coefficients
    def __init__(self, l, r):

        self.lhs = l
        self.rhs = r

        coefs = self.__cal_coef(self.lhs, self.rhs)

        self.CoefL = coefs[0]
        self.CoefR = coefs[1]

        if not (self.__pos(self.CoefL)):
            raise ValueError
        elif not (self.__pos(self.CoefR)):
            raise ValueError
        elif not (self.__is_balanced(self.lhs, self.rhs, self.CoefL, self.CoefR)):
            raise ValueError

    ## @brief Calculates the coefficients of the right and left side of the reaction
    #  Source: https://codegolf.stackexchange.com/questions/8728/balance-chemical-equations
    #          https://www.nayuki.io/res/chemical-equation-balancer-javascript/chemical-equation-balancer.js
    #  @param lhs A Sequence of Compounds Representing the left side of the reaction
    #  @param rhs A Sequence of Compounds Representing the right side of the reaction
    #  @return A tuple containing the two lists, one for the left and one for the
    #          right hand side of the reaction, each containing the corresponding coefficients
    def __cal_coef(self, lhs, rhs):
        elmlistl = self.__make_seq(lhs)
        elmlistr = self.__make_seq(rhs)
        self.__is_list_valid(elmlistl, elmlistr)
        arr = self.__matrix(lhs, rhs, elmlistl)
        arr2 = self.__inv_matrix(arr)
        coeffs = self.__make_coeff(arr2, lhs, rhs)
        return coeffs

    ## @brief Makes a sequence of the elements in the Compound
    #  @param side A Sequence of Compounds Representing the one side of the reaction
    #  @return A sequence of elements from the Compound without any duplicates
    def __make_seq(self, side):
        elmlist = []
        elmlisttry = []
        for comp in side:
            elmlisttry = elmlisttry + comp.constit_elems().S
        for i in elmlisttry:
            if i not in elmlist:
                elmlist.append(i)
        return elmlist

    ## @brief Validates if the right side of the reaction has the same elements as the left
    #  @param elmlistl A sequence of elements representing the elements on the left side
    #  @param elmlistr A Sequence of elements representing the elements on the right side
    #  @throws ValueError If either the length of the right side elements' list and the
    #          left side elements' list do not match or one side contains a different element
    def __is_list_valid(self, elmlistl, elmlistr):
        if not (len(elmlistl) == len(elmlistr)):
            raise ValueError("Elements are different on both sides")
        for e in elmlistr:
            if not (e in elmlistr):
                raise ValueError("Elements mismatch on either of the sides")

    ## @brief Creates a square matrix representing the reaction and elements
    #  @details Creates an identity matrix utilizing numpy, it then adds the corresponding
    #           number of atoms of each element according to the elmlistl
    #  @param lhs A Sequence of Compounds Representing the left side of the reaction
    #  @param rhs A Sequence of Compounds Representing the right side of the reaction
    #  @param elmlistl A sequence of elements from the left hand side without any duplicates
    #  @return arr A square matrix representing the reaction and elements
    def __matrix(self, lhs, rhs, elmlistl):
        cols = len(lhs) + len(rhs)
        rows = len(elmlistl)
        if rows > cols:
            arr = np.identity(rows, dtype=int)
        elif rows < cols:
            arr = np.identity(cols, dtype=int)
        for i in range(len(elmlistl)):
            j = 0
            for comp in lhs:
                arr[i][j] = comp.num_atoms(elmlistl[i])
                j += 1
            for comp in rhs:
                arr[i][j] = (-1) * comp.num_atoms(elmlistl[i])
                j += 1
        return arr

    ## @brief Inverses a matrix and returns the inversed matric in whole numbers
    #  @details Uses numpy to inverse matrix and the fuction gcd to get whole numbers
    #  @param arr A square matrix representing the reaction and elements
    #  @return arr2 A matrix representing the inverse of the input matrix in whole numbers
    def __inv_matrix(self, arr):
        arr2 = np.linalg.inv(arr)
        num1 = arr2[0][0]
        num2 = arr2[0][1]
        gcd = self.__find_gcd(num1, num2)
        for i in range(len(arr2)):
            for j in range(len(arr2[0])):
                gcd = self.__find_gcd(gcd, arr2[i][j])
        arr2 = (1 / gcd) * arr2
        return arr2

    ## @brief Creates the coefficients of the compounds of both sides of the reaction
    #  @param lhs A Sequence of Compounds Representing the left side of the reaction
    #  @param rhs A Sequence of Compounds Representing the right side of the reaction
    #  @param arr A matrix representing the reaction coefficients which is the last
    #         element of each row
    #  @return arr A square matrix representing the reaction and elements
    def __make_coeff(self, arr, lhs, rhs):
        cols = len(lhs) + len(rhs)
        newlist = []
        for i in range(len(arr)):
            newlist.append(arr[i][cols - 1])
        listleft = []
        listright = []
        for i in range(len(self.lhs)):
            listleft.append(int(newlist[i]))
        for i in range(len(listleft), len(newlist)):
            listright.append(int(newlist[i]))
        return (listleft, listright)

    ## @brief Finds the greatest common denominator of the two numbers
    #  Source: https://www.geeksforgeeks.org/gcd-two-array-numbers/
    #  @param x A number mostly expected to be rational
    #  @param y A number mostly expected to be rational
    #  @return x The greatest common denominator
    def __find_gcd(self, x, y):
        while(y):
            x, y = y, x % y
        return x

    ## @brief Returns the sequence of compounds representing the left hand
    #         side of the reaction
    def get_lhs(self):
        return self.lhs

    ## @brief Returns the sequence of compounds representing the right hand
    #         side of the reaction
    def get_rhs(self):
        return self.rhs

    ## @brief Returns the sequence of coefficients representing the left hand
    #         side coefficients of the reaction
    def get_lhs_coeff(self):
        return self.CoefL

    ## @brief Returns the sequence of coefficients representing the right hand
    #         side coefficients of the reaction
    def get_rhs_coeff(self):
        return self.CoefR

    ## @brief Checks if the elements in the list are positive
    #  @param coef A sequence of coefficients representing the coefficients of
    #         one side of the reaction
    #  @return True if all the elements are positive, False otherwise
    def __pos(self, coef):
        for i in range(len(coef)):
            if coef[i] < 0:
                return False
        return True

    ## @brief Get the number of the atoms of one element in one side of the reaction
    #  @param seq A sequence of compounds representing one side of the reaction
    #  @param coef A sequence of compound coeffiecients representing one side of the reaction
    #  @param e An ElementT type data
    #  @return atoms The number of atoms of an element in one sode
    def __n_atoms(self, seq, coef, e):
        atoms = 0
        for i in range(len(seq)):
            atoms = atoms + coef[i] * seq[i].num_atoms(e)
        return atoms

    ## @brief Gets and returns a sequence of elements in one side of the reaction
    #  @param seq A sequence of compounds representing one side of the reaction
    #  @return elmlist A sequence of elements in one side of the reaction
    def __elm_in_chem_eq(self, seq):
        elmlist = []
        elmlisttry = []
        for comp in seq:
            elmlisttry = elmlisttry + comp.constit_elems().S
        for i in elmlisttry:
            if i not in elmlist:
                elmlist.append(i)
        return elmlist

    ## @brief Checks if an element is present with equal number of atoms on each side
    #  @param l A sequence of compounds representing left side of the reaction
    #  @param coefl A sequence of compound coeffiecients representing left side of the reaction
    #  @param r A sequence of compounds representing right side of the reaction
    #  @param coefr A sequence of compound coeffiecients representing right side of the reaction
    #  @return True if an element is present with equal number of atoms on each side,
    #          False otherwise
    def __is_bal_elm(self, l, r, coefl, coefr, e):
        return self.__n_atoms(l, coefl, e) == self.__n_atoms(r, coefr, e)

    ## @brief Checks if the reaction is balanced
    #  @param l A sequence of compounds representing left side of the reaction
    #  @param coefl A sequence of compound coeffiecients representing left side of the reaction
    #  @param r A sequence of compounds representing right side of the reaction
    #  @param coefr A sequence of compound coeffiecients representing right side of the reaction
    #  @return True if the reaction is balanced, False otherwise
    def __is_balanced(self, l, r, coefl, coefr):
        self.__is_list_valid(self.__elm_in_chem_eq(l), self.__elm_in_chem_eq(r))
        for e in self.__elm_in_chem_eq(l):
            if not (self.__is_bal_elm(l, r, coefl, coefr, e)):
                return False
        return True
