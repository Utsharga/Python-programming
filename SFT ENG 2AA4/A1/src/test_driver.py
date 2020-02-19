## @file test_driver.py
#  @author Utsharga Rozario
#  @brief Provides test samples for pos_adt.py and date_adt,py
#  @date 20/1/2020

from date_adt import *
from pos_adt import *


######Test Cases for date_adt.py#######

# @brief Tests the day method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT day method
def test_day():
  global testTot, passed
  testTot += 1
  try:
    assert date1.day() == 1
    assert date2.day() == 28
    assert date3.day() == 29
    assert date4.day() == 31
    assert date5.day() == 1
    passed += 1
    print("day test PASSED.")
  except AssertionError:
    print("day test FAILED.")

# @brief Tests the month method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT month method
def test_month():
  global testTot, passed
  testTot += 1
  try:
    assert date1.month() == 1
    assert date2.month() == 2
    assert date3.month() == 2
    assert date4.month() == 12
    assert date5.month() == 3
    passed += 1
    print("month test PASSED.")
  except AssertionError:
    print("month test FAILED.")

# @brief Tests the year method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT year method
def test_year():
  global testTot, passed
  testTot += 1
  try:
    assert date1.year() == 22
    assert date2.year() == 2222
    assert date3.year() == 2000
    assert date4.year() == 2
    assert date5.year() == 10000
    passed += 1
    print("year test PASSED.")
  except AssertionError:
    print("year test FAILED.")

# @brief Tests the next method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT next method
def test_next():
  global testTot, passed
  testTot += 1
  try:
    assert (date1.next().day() == 2 and date1.next().month() == 1 and date1.next().year() == 22)
    assert (date2.next().day() == 1 and date2.next().month() == 3 and date2.next().year() == 2222)
    assert (date3.next().day() == 1 and date3.next().month() == 3 and date3.next().year() == 2000)
    assert (date4.next().day() == 1 and date4.next().month() == 1 and date4.next().year() == 3)
    assert (date5.next().day() == 2 and date5.next().month() == 3 and date5.next().year() == 10000)
    passed += 1
    print("next test PASSED.")
  except AssertionError:
    print("next test FAILED.")

# @brief Tests the prev method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT prev method
def test_prev():
  global testTot, passed
  testTot += 1
  try:
    assert (date1.prev().day() == 31 and date1.prev().month() == 12 and date1.prev().year() == 21)
    assert (date2.prev().day() == 27 and date2.prev().month() == 2 and date2.prev().year() == 2222)
    assert (date3.prev().day() == 28 and date3.prev().month() == 2 and date3.prev().year() == 2000)
    assert (date4.prev().day() == 30 and date4.prev().month() == 12 and date4.prev().year() == 2)
    assert (date5.prev().day() == 29 and date5.prev().month() == 2 and date5.prev().year() == 10000)
    passed += 1
    print("prev test PASSED.")
  except AssertionError:
    print("prev test FAILED.")

# @brief Tests the before method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT before method
def test_before():
  global testTot, passed
  testTot += 1
  try:
    assert date1.before(DateT(1,1,23))
    assert date2.before(DateT(31,12,3000))
    assert (date3.before(DateT(29,2,2000)) == False)
    assert date4.before(DateT(12,10,213))
    assert date5.before(DateT(29,3,10000))
    passed += 1
    print("before test PASSED.")
  except AssertionError:
    print("before test FAILED.")

# @brief Tests the after method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT after method
def test_after():
  global testTot, passed
  testTot += 1
  try:
    assert date1.after(DateT(31,12,21))
    assert date2.after(DateT(4,7,2000))
    assert (date3.after(DateT(12,6,3000)) == False)
    assert date4.after(DateT(30,12,2))
    assert date5.after(DateT(1,1,1))
    passed += 1
    print("after test PASSED.")
  except AssertionError:
    print("after test FAILED.")

# @brief Tests the equal method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT equal method
def test_equal():
  global testTot, passed
  testTot += 1
  try:
    assert date1.equal(DateT(1,1,22))
    assert date2.equal(DateT(28,2,2222))
    assert date3.equal(DateT(29,2,2000))
    assert date4.equal(DateT(31,12,2))
    assert date5.equal(DateT(1,3,10000))
    passed += 1
    print("equal test PASSED.")
  except AssertionError:
    print("equal test FAILED.")

# @brief Tests the add_days method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT add_days method
def test_add_days():
  global testTot, passed
  testTot += 1
  try:
    assert (date1.add_days(31).day() == 1 and date1.add_days(31).month() == 2 and date1.add_days(31).year() == 22)
    assert (date2.add_days(365).day() == 28 and date2.add_days(365).month() == 2 and date2.add_days(365).year() == 2223)
    assert (date3.add_days(307).day() == 1 and date3.add_days(307).month() == 1 and date3.add_days(307).year() == 2001)
    assert (date4.add_days(90000).day() == 30 and date4.add_days(90000).month() == 5 and date4.add_days(90000).year() == 249)
    assert (date5.add_days(70).day() == 10 and date5.add_days(70).month() == 5 and date5.add_days(70).year() == 10000)
    passed += 1
    print("add_days test PASSED.")
  except AssertionError:
    print("add_days test FAILED.")

# @brief Tests the days_between method of the DateT class
# @details Checks for equality between actual and expected values for
#          the DateT days_between method
def test_days_between():
  global testTot, passed
  testTot += 1
  try:
    assert date1.days_between(DateT(1,3,22)) == 59
    assert date2.days_between(DateT(31,12,3000)) == 284465
    assert date3.days_between(DateT(1,3,2000)) == 1
    assert date4.days_between(DateT(31,12,3)) == 365
    assert date5.days_between(DateT(1,3,10000)) == 0
    passed += 1
    print("days_between test PASSED.")
  except AssertionError:
    print("days_between test FAILED.")


testTot = 0
passed = 0

date1 = DateT(1,1,22)
date2 = DateT(28,2,2222)
date3 = DateT(29,2,2000)
date4 = DateT(31,12,2)
date5 = DateT(1,3,10000)

print("Test Cases for date_adt.py:")
test_day()
test_month()
test_year()
test_next()
test_prev()
test_before()
test_after()
test_equal()
test_add_days()
test_days_between()

print (passed, "of", testTot, "date_adt.py tests passed.")

######Test Cases for pos_adt.py#######

# for testing floating point equality after arithmetic
def isClose(a, b):
    return (abs(a - b) <= 0.1*(abs(a)))

# @brief Tests the lat method of the GPosT class
# @details Checks for equality between actual and expected values for
#          the GPosT lat method
def test_lat():
  global testTotPos, passedPos
  testTotPos += 1
  try:
    assert pos1.lat() == -90.00
    assert pos2.lat() == 90.00
    assert pos3.lat() == 0.00
    assert pos4.lat() == -53.1236739687
    assert pos5.lat() == 45
    passedPos += 1
    print("lat test PASSED.")
  except AssertionError:
    print("lat test FAILED.")

# @brief Tests the long method of the GPosT class
# @details Checks for equality between actual and expected values for
#          the GPosT l ongmethod
def test_long():
  global testTotPos, passedPos
  testTotPos += 1
  try:
    assert pos1.long() == -180.00
    assert pos2.long() == 180.00
    assert pos3.long() == 0.00
    assert pos4.long() == 31.5463673564
    assert pos5.long() == -87
    passedPos += 1
    print("long test PASSED.")
  except AssertionError:
    print("long test FAILED.")

# @brief Tests the west_of method of the GPosT class
# @details Checks for equality between actual and expected values for
#          the GPosT west_of method
def test_west_of():
  global testTotPos, passedPos
  testTotPos += 1
  try:
    assert (pos1.west_of(GPosT(-90.00, -179.9999999999)) == True)
    assert (pos2.west_of(GPosT(90.00, 179.9999999999)) == False)
    assert (pos3.west_of(GPosT(0.0000000001, 32.0000000001)) == True)
    assert (pos4.west_of(GPosT(67.70497335, 29.904735907450)) == False)
    assert (pos5.west_of(GPosT(90.00, -180.00)) == False)
    passedPos += 1
    print("west_of test PASSED.")
  except AssertionError:
    print("west_of test FAILED.")

# @brief Tests the north_of method of the GPosT class
# @details Checks for equality between actual and expected values for
#          the GPosT north_of method
def test_north_of():
  global testTotPos, passedPos
  testTotPos += 1
  try:
    assert (pos1.north_of(GPosT(-89.9999999999, -180.00)) == False)
    assert (pos2.north_of(GPosT(89.9999999999, 180.00)) == True)
    assert (pos3.north_of(GPosT(32.0000000001, 0.0000000001)) == False)
    assert (pos4.north_of(GPosT(-67.097060756709, 29.904735907450)) == True)
    assert (pos5.north_of(GPosT(-90.00, -180.00)) == True)
    passedPos += 1
    print("north_of test PASSED.")
  except AssertionError:
    print("north_of test FAILED.")

# @brief Tests the equal method of the GPosT class
# @details Checks for equality between actual and expected values for
#          the GPosT equal method
def test_equal_pos():
  global testTotPos, passedPos
  testTotPos += 1
  try:
    assert pos1.equal(GPosT(-89.9999999999, -179.9999999999)) == True
    assert pos2.equal(GPosT(90.00, 180.00)) == True
    assert pos3.equal(GPosT(0.00, 32.9098678598)) == False
    assert pos4.equal(GPosT(-53.12367370058, 31.55383614889)) == True
    assert pos5.equal(GPosT(45.00645172973, -86.99111585795)) == False
    passedPos += 1
    print("equal test PASSED.")
  except AssertionError:
    print("equal test FAILED.")

# @brief Tests the move method of the GPosT class
# @details Checks for equality between actual and expected values for
#          the GPosT move method
def test_move():
  global testTotPos, passedPos
  testTotPos += 1
  pos1m = GPosT(pos1.lat(), pos1.long())
  pos2m = GPosT(pos2.lat(), pos2.long())
  pos3m = GPosT(pos3.lat(), pos3.long())
  pos4m = GPosT(pos4.lat(), pos4.long())
  pos5m = GPosT(pos5.lat(), pos5.long())
  pos1m.move(90.00, 100000)
  pos2m.move(360,100)
  pos3m.move(45,3564)
  pos4m.move(-79,10000)
  pos5m.move(0,0)
  try:
    assert (isClose(pos1m.lat(), 89.3216) and isClose(pos1m.long(), -90.0000))
    assert (isClose(pos2m.lat(), 89.1007) and isClose(pos2m.long(), 90.0000))
    assert (isClose(pos3m.lat(), 22.0399) and isClose(pos3m.long(), 023.8808))
    assert (isClose(pos4m.lat(), 06.3018) and isClose(pos4m.long(),  -049.4131))
    assert (isClose(pos5m.lat(), 45.00) and isClose(pos5m.long(),  -087.00))
    passedPos += 1
    print("move test PASSED.")
  except AssertionError:
    print("move test FAILED.")

# @brief Tests the distance method of the GPosT class
# @details Checks for equality between actual and expected values for
#          the GPosT distance method
def test_distance():
  global testTotPos, passedPos
  testTotPos += 1
  try:
    assert isClose(pos1.distance(GPosT(90,180)),20020)
    assert isClose(pos2.distance(GPosT(-56.4639764,-76.4875)), 16290)
    assert isClose(pos3.distance(GPosT(87.9467, 80.7486)), 9971)
    assert isClose(pos4.distance(GPosT(90, -180)), 15910)
    assert isClose(pos5.distance(GPosT(45.01, -87)), 1.112)
    passedPos += 1
    print("distance test PASSED.")
  except AssertionError:
    print("distance test FAILED.")
    
# @brief Tests the arrival_date method of the GPosT class
# @details Checks for equality between actual and expected values for
#          the GPosT arrival_date method
def test_arrival_date():
  global testTotPos, passedPos
  testTotPos += 1
  date1 = pos1.arrival_date(GPosT(90,180), DateT(1,1,2000), 54.5)
  date2 = pos2.arrival_date(GPosT(-56.4639764,-76.4875), DateT(1,2,2000), 212.59123)
  date3 = pos3.arrival_date(GPosT(87.9467, 80.7486), DateT(1,2,2000), 9970.84535815507)
  date4 = pos4.arrival_date(GPosT(90, -180), DateT(1,2,2000), 16000)
  date5 = pos5.arrival_date(GPosT(45.01, -87), DateT(1,2,2000), 0.0371)
  try:
    assert date1.day() == 2 and date1.month() == 1 and date1.year() == 2001
    assert date2.day() == 17 and date2.month() == 4 and date2.year() == 2000
    assert date3.day() == 1 and date3.month() == 2 and date3.year() == 2000
    assert date4.day() == 1 and date4.month() == 2 and date4.year() == 2000
    assert date5.day() == 1 and date5.month() == 3 and date5.year() == 2000
    passedPos += 1
    print("arrival_date test PASSED.")
  except AssertionError:
    print("arrival_date test FAILED.")

pos1 = GPosT(-90.00, -180.00)
pos2 = GPosT(90.00, 180.00)
pos3 = GPosT(0.00, 0.00)
pos4 = GPosT(-53.1236739687, 31.5463673564)
pos5 = GPosT(45.00, -87.00)

testTotPos = 0
passedPos = 0

print("Test Cases for pos_adt.py:")

test_lat()
test_long()
test_west_of()
test_north_of()
test_equal_pos()
test_move()
test_distance()
test_arrival_date()

print ( passedPos, "of", testTotPos, "pos_adt.py tests passed.")
  
