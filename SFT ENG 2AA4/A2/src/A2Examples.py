from ChemTypes import ElementT
import numpy as np
from Set import *
from ElmSet import *
from MolecSet import *
from MoleculeT import *
from CompoundT import *
from ReactionT import *

# Chem Type Examples
e1 = ElementT.H
e2 = ElementT.He

# Set Examples - with integers
S = Set([1, -6, 4, 0, 12])

S.add(5)

S.rm(4)

print(S.member(5))
print(S.member(4))
print(S.size())

R = Set([12, -6, 0, 1, 5])

print(S.equals(R))
print(S == R)

print(str(R.to_seq()))

for i in R:
    print(i)

# ElmSet Examples
E = ElmSet([ElementT.H, ElementT.O])
E.add(ElementT.C)
print(E == ElmSet([ElementT.H, ElementT.C, ElementT.O]))

# MoleculeT Examples
M1 = MoleculeT(2, ElementT.H)
M2 = MoleculeT(7, ElementT.O)
M3 = MoleculeT(2, ElementT.H)
print(M1.num_atoms(ElementT.C)) #0
print(M1.constit_elems() == ElmSet([ElementT.H])) #True
print(M1.equals(M2)) #False
print(M1 == M2) #False
print(M1 == M3) #True

# CompoundT Examples
C1 = CompoundT(MolecSet([M1, M2]))
C2 = CompoundT(MolecSet([M1, M2]))
print(C1.num_atoms(ElementT.O)) #2
e = C1.constit_elems()
print(e.equals(ElmSet([ElementT.H, ElementT.O])))
print(C1.equals(CompoundT(MolecSet([M1]))))
print(C1.equals(C2))
print(C1 == C2)

elmListL = []

C3 = [CompoundT(MolecSet([MoleculeT(2, ElementT.H)])), CompoundT(MolecSet([MoleculeT(2, ElementT.O)]))]
C4 = [CompoundT(MolecSet([MoleculeT(1, ElementT.H), MoleculeT(1, ElementT.O)]))]

for comp in C3:
    elmListL = elmListL + comp.constit_elems().S

elmListB = []

for i in elmListL:
    if i not in elmListB:
        elmListB.append(i)

for i in range(len(elmListB)):
    print (elmListB[i])

cols = len(C3) + len(C4)
rows = len(elmListB)
if rows > cols:
    arr = np.identity(rows, dtype = int) 
elif rows < cols:
    arr = np.identity(cols, dtype = int) 

for i in range(len(elmListB)):
    #creating a list of lists
    j = 0
    for comp in C3:
        arr[i][j] = comp.num_atoms(elmListB[i])
        j += 1

    for comp in C4:
        arr[i][j] = (-1)*comp.num_atoms(elmListB[i])
        j += 1

arr2 = np.linalg.inv(arr)


print (arr)

print (arr2)

def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x

num1 = arr2[0][0] 
num2 = arr2[0][1] 
gcd = find_gcd(num1, num2) 

for i in range(len(arr2)):
    for j in range(len(arr2[0])): 
        gcd = find_gcd(gcd, arr2[i][j])

arr2 = (1/gcd)*arr2

print (arr2)

print (gcd)

newList = []

for i in range(len(arr2)):
    newList.append(arr2[i][cols-1])

print (newList)

listLeft = []
listRight = []

for i in range(len(C3)):
    listLeft.append(int(newList[i]))

print (listLeft)

for i in range(len(listLeft), len(newList)):
    listRight.append(int(newList[i]))

print (listRight)

r = ReactionT(C3, C4)

print(r.get_lhs_coeff())

print(r.get_rhs_coeff())

m1 = MoleculeT(1, ElementT.Na)
m2 = MoleculeT(1, ElementT.Cl)
m3 = MoleculeT(1, ElementT.S)
m4 = MoleculeT(2, ElementT.O)
m5 = MoleculeT(2, ElementT.H)
m6 = MoleculeT(1, ElementT.O)
m7 = MoleculeT(2, ElementT.Na)
m10 = MoleculeT(4, ElementT.O)
m11 = MoleculeT(1, ElementT.H)
compound1 = CompoundT(MolecSet([m1, m2]))
compound2 = CompoundT(MolecSet([m3, m4]))
compound3 = CompoundT(MolecSet([m5, m6]))
compound4 = CompoundT(MolecSet([m4]))
compound5 = CompoundT(MolecSet([m7, m3, m10]))
compound6 = CompoundT(MolecSet([m11, m2]))
lhs = [compound1, compound2, compound3, compound4]
rhs = [compound5, compound6]
reaction = ReactionT(lhs, rhs)