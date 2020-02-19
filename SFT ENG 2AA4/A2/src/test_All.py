## @file test_All.py
#  @author Utsharga Rozario
#  @brief Tests implementation of python files Set, MoleculeT, CompoundT and ReactionT.
#  @date Feb 8, 2020
#  @details Written to test chemical reaction balancing
#           Avoids interacting with state variables to enforce information hiding.

import pytest

from ChemTypes import ElementT
from Set import *
from MoleculeT import *
from CompoundT import *
from ReactionT import *


## @brief Tests methods from Set.py
class TestSet:

    def setup_method(self, method):
        self.set1 = Set([1, 2, 3, 4, 5])
        self.set2 = Set([])

    def test_add(self):
        self.set1.add(6)
        assert self.set1.member(6)
        self.set1.add("32")
        assert self.set1.member("32")

    def test_rm(self):
        self.set1.rm(5)
        assert not self.set1.member(5)

        with pytest.raises(ValueError):
            self.set1.rm(7)

    def test_member(self):
        assert self.set1.member(2)
        assert not self.set1.member(8)

    def test_size(self):
        assert self.set1.size() == 5
        assert self.set2.size() == 0

    def test_equals(self):
        assert self.set1.equals(Set([1, 2, 3, 4, 5]))
        assert not self.set1.equals(Set([1, 2, 3, 4]))

    def test___eq__(self):
        assert self.set1 == Set([1, 2, 3, 4, 5])
        assert not self.set1 == Set([1, 2, 3, 4])

    def test_to_seq(self):
        assert self.set1.to_seq() == [1, 2, 3, 4, 5]


## @brief Tests methods from MoleculeT.py
class TestMoleculeT:

    def setup_method(self, method):
        self.molec1 = MoleculeT(5, ElementT.H)

    def test_get_elm(self):
        assert self.molec1.get_elm() == ElementT.H

    def test_get_num(self):
        assert self.molec1.get_num() == 5

    def test_equals(self):
        assert self.molec1.equals(MoleculeT(5, ElementT.H))
        assert not self.molec1.equals(MoleculeT(4, ElementT.H))
        assert not self.molec1.equals(MoleculeT(5, ElementT.O))

    def test___eq__(self):
        assert self.molec1 == MoleculeT(5, ElementT.H)
        assert not self.molec1 == MoleculeT(4, ElementT.H)
        assert not self.molec1 == MoleculeT(5, ElementT.O)

    def test_num_atoms(self):
        assert self.molec1.num_atoms(ElementT.H) == 5
        assert self.molec1.num_atoms(ElementT.O) == 0

    def test_constit_elms(self):
        assert self.molec1.constit_elems() == ElmSet([ElementT.H])


## @brief Tests methods from CompoundT.py
class TestCompoundT:

    def setup_method(self, method):
        self.m1 = MoleculeT(3, ElementT.C)
        self.m2 = MoleculeT(8, ElementT.H)
        self.m3 = MoleculeT(3, ElementT.O)
        self.m4 = MoleculeT(1, ElementT.Mg)
        self.m5 = MoleculeT(1, ElementT.Og)
        self.m6 = MoleculeT(17, ElementT.O)
        self.compound1 = CompoundT(MolecSet([self.m1, self.m2, self.m3]))
        self.compound2 = CompoundT(MolecSet([self.m4, self.m3, self.m5]))
        self.compound3 = CompoundT(MolecSet([self.m4]))
        self.compound4 = CompoundT(MolecSet([self.m3, self.m4, self.m6]))
        self.elmset1 = ElmSet([ElementT.C, ElementT.H, ElementT.O])
        self.elmset2 = ElmSet([ElementT.Mg, ElementT.O, ElementT.Og])
        self.elmset3 = ElmSet([ElementT.Mg])

    def test_get_molec_set(self):
        assert self.compound1.get_molec_set() == MolecSet([self.m1, self.m2, self.m3])
        assert self.compound2.get_molec_set() == MolecSet([self.m4, self.m3, self.m5])
        assert self.compound3.get_molec_set() == MolecSet([self.m4])

    def test___eq__(self):
        assert self.compound1 == CompoundT(MolecSet([self.m1, self.m2, self.m3]))
        assert self.compound2 == CompoundT(MolecSet([self.m4, self.m3, self.m5]))
        assert self.compound3 == CompoundT(MolecSet([self.m4]))
        assert not self.compound2 == CompoundT(MolecSet([self.m4, self.m3, self.m6]))
    
    def test_equals(self):
        assert self.compound1.equals(CompoundT(MolecSet([self.m1, self.m2, self.m3])))
        assert self.compound2.equals(CompoundT(MolecSet([self.m4, self.m3, self.m5])))
        assert self.compound3.equals(CompoundT(MolecSet([self.m4])))
        assert not self.compound2.equals(CompoundT(MolecSet([self.m4, self.m3, self.m6])))

    def test_num_atoms(self):
        assert self.compound1.num_atoms(ElementT.H) == 8
        assert self.compound2.num_atoms(ElementT.Ag) == 0
        assert self.compound4.num_atoms(ElementT.O) == 20

    def test_constit_elms(self):
        assert self.compound1.constit_elems() == self.elmset1
        assert self.compound2.constit_elems() == self.elmset2
        assert self.compound3.constit_elems() == self.elmset3


## @brief Tests methods from ReactionT.py
class TestReactionT:

    def setup_method(self, method):
        self.m1 = MoleculeT(1, ElementT.Na)
        self.m2 = MoleculeT(1, ElementT.Cl)
        self.m3 = MoleculeT(1, ElementT.S)
        self.m4 = MoleculeT(2, ElementT.O)
        self.m5 = MoleculeT(2, ElementT.H)
        self.m6 = MoleculeT(1, ElementT.O)
        self.m7 = MoleculeT(2, ElementT.Na)
        self.m10 = MoleculeT(4, ElementT.O)
        self.m11 = MoleculeT(1, ElementT.H)
        self.compound1 = CompoundT(MolecSet([self.m1, self.m2]))
        self.compound2 = CompoundT(MolecSet([self.m3, self.m4]))
        self.compound3 = CompoundT(MolecSet([self.m5, self.m6]))
        self.compound4 = CompoundT(MolecSet([self.m4]))
        self.compound5 = CompoundT(MolecSet([self.m7, self.m3, self.m10]))
        self.compound6 = CompoundT(MolecSet([self.m11, self.m2]))
        self.lhs = [self.compound1, self.compound2, self.compound3, self.compound4]
        self.rhs = [self.compound5, self.compound6]
        self.lhs2 = [CompoundT(MolecSet([self.m5])), CompoundT(MolecSet([self.m4]))]
        self.rhs2 = [CompoundT(MolecSet([self.m5, self.m6]))]
        self.list = [self.compound1, self.compound2, self.compound3, self.compound4]
        self.reaction = ReactionT(self.lhs, self.rhs)
        self.reaction2 = ReactionT(self.lhs2, self.rhs2)

    def test_get_lhs(self):
        assert self.reaction.get_lhs() == self.list
        assert self.reaction2.get_lhs() == self.lhs2

    def test_get_rhs(self):
        assert self.reaction.get_rhs() == [self.compound5, self.compound6]
        assert self.reaction2.get_rhs() == self.rhs2

    def test_get_lhs_coeff(self):
        assert self.reaction.get_lhs_coeff() == [4, 2, 2, 1]
        assert self.reaction2.get_lhs_coeff() == [2, 1]

    def test_get_rhs_coeff(self):
        assert self.reaction.get_rhs_coeff() == [2, 4]
        assert self.reaction2.get_rhs_coeff() == [2]
