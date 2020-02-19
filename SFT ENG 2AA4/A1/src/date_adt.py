## @file date_adt.py
#  @author Utsharga Rozario
#  @brief Provides the DateT ADT class for representating dates
#  @date 20/1/2020

## @brief An ADT that represents a date
class DateT:

  ## @brief Date Constructor
  #  @details Initializes a DateT object with day, month and year
  #  @param d The day of the date
  #  @param m The month of the date
  #  @param y The year of the date
  #  @exception ValueError throws if the date is not a valid date
  def __init__(self, d, m, y):
    if (y < 0):
      raise ValueError("Date is not valid date")
    elif (m < 1 or m > 12):
      raise ValueError("Date is not valid date")
    elif (m == 2 and ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)) and d > 29):
      raise ValueError("Date is not valid date")
    elif (m == 2 and d > 28 and (y%4 != 0)):
      raise ValueError("Date is not valid date")
    elif ((m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d > 31):
      raise ValueError("Date is not valid date")
    elif ((m == 4 or m == 6 or m == 9 or m == 11) and d > 30):
      raise ValueError("Date is not valid date")
    self.d = d
    self.m = m
    self.y = y
  
  ## @brief Gets the day of the date
  #  @return The day of the date
  def day(self):
    return self.d

  ## @brief Gets the month of the date
  #  @return The month of the date
  def month(self):
    return self.m

  ## @brief Gets the year of the date
  #  @return The year of the date
  def year(self):
    return self.y

  ## @brief Determines if the year is a leap year or not
  #  @return True if it is leap year, False
  def __leapYear(self):
    return (((self.year() % 4) == 0 and ((self.year() % 100) != 0)) or ((self.year() % 400) == 0))
  
  ## @brief Calculates the next date in respective to current date
  #  @details Determines which date it is, if it is the last date of the month then it increments the month,
  #           and also the day to 1, also considers cases for leap year
  #  @return The next date from the current date in the DateT format
  def next(self):
    if (self.day() < 30):
      if (self.month() != 2):
        return DateT(self.day() + 1, self.month(), self.year())
      elif (self.month() == 2):
        if (self.day() < 28):
          return DateT(self.day() + 1, self.month(), self.year())
        elif (self.day() == 28 and not(self.__leapYear())):
          return DateT(1, 3, self.year())
        elif (self.day() == 28 and self.__leapYear()):
          return DateT(self.day() + 1, self.month(), self.year())
        elif (self.day() == 29 and self.__leapYear()):
          return DateT(1, 3, self.year())
    elif (self.day() == 30 and (self.month() == 4 or self.month() == 6 or self.month() == 9 or self.month() == 11)):
      return DateT(1, self.month() + 1, self.year())
    elif (self.month() == 1 or self.month() == 3 or self.month() == 5 or self.month() == 7 or self.month() == 8 or self.month() == 10):
      if (self.day() == 30):
        return DateT(31, self.month(), self.year())
      elif (self.day() == 31):
        return DateT(1, self.month() + 1, self.year())
    elif(self.month() == 12):
      if (self.day() == 30):
        return DateT(31, self.month(), self.year())
      elif (self.day() == 31):
        return DateT(1, 1, self.year() + 1)

  ## @brief Calculates the previous date in respective to current date
  #  @details Determines which date it is, if it is the first date of the month then it decrements the month,
  #           and also the day to the corresponding month's last day, also considers cases for leap year
  #  @return The previous date from the current date in the DateT format
  def prev(self):
    if (self.day() > 1):
      return DateT(self.day() - 1, self.month(), self.year())
    elif (self.day() == 1):
      if (self.month() == 1):
        return DateT(31, 12, self.year() - 1)
      elif (self.month() == 2 or self.month() == 4 or self.month() == 6 or self.month() == 8 or self.month() == 9 or self.month() == 11):
        return DateT(31, self.month() - 1, self.year())
      elif (self.month() ==3):
        if (self.__leapYear()):
          return DateT(29, 2, self.year())
        elif(self.__leapYear()):
          return DateT(28, 2, self.year())
      elif (self.month() == 5 or self.month() == 7 or self.month() == 10 or self.month() == 12):
        return DateT(30, self.month() - 1, self.year())
      
  ## @brief Determines if current date is before to the date d
  #  @param d Date in DateT format
  #  @return Returns true if current date is before the date d, false if not
  def before(self, d):
    if (d.year() > self.year()):
      return True
    elif (self.year() == d.year()):
      if (d.month() > self.month()):
        return True
      elif (self.month() == d.month()):
        if (d.day() > self.day()):
          return True
        else:
          return False
      elif (d.month() < self.month()):
        return False
    elif (d.year() < self.year()):
      return False

  ## @brief Determines if current date is after to d date
  #  @param d Date in DateT format
  #  @return Returns true if current date is after the date d, false if not
  def after(self, d):
    return not(self.before(d))

  ## @brief Compares current Date with another date 
  #  @param d Date in DateT format
  #  @return Returns true if current date is equal to the date d, false if not
  def equal(self, d):
    if(self.day() == d.day() and self.month() == d.month() and self.year() == d.year()):
      return True
    else:
      return False
        
  ## @brief Calculates the Date after n number of days
  #  @details Utilizes the next method form DateT class, performs a for loop calculate the date after n number of days
  #  @param n The number of days to be added to the current date
  #  @return Date after n number of days
  def add_days(self, n):
    added_date = DateT(self.day(), self.month(), self.year())
    for m in range(n):
      added_date = added_date.next()
    return added_date

  ## @brief Calculates the number of days between current Date and d Date
  #  @details Determines which of the dates is before and after, and performs appropriate
  #           while loop with conditions to match the date in the parameter. The while loop
  #           is executed on the basis that the next or prev method approaches the d date
  #           while incrementing a variable n, which is the days between them.  
  #  @param d Date in DateT format 
  #  @return The difference in interger between the current Date and d Date
  def days_between(self, d):
    n = 0
    d_date = DateT(self.day(), self.month(), self.year())
    if (d.year() > d_date.year()):
      while not (d.equal(d_date)):
        d_date = d_date.next()
        n = n + 1
    elif (d_date.year() == d.year()):
      if (d.month() > d_date.month()):
        while not (d.equal(d_date)):
          d_date = d_date.next()
          n = n + 1
      elif (d_date.month() == d.month()):
        if (d.day() > d_date.day()):
          n = d.day() - d_date.day()
        elif (d.day() == d_date.day()):
          n = 0
        elif (d.day() < d_date.day()):
          n = d_date.day() - d.day()
      elif (d.month() < d_date.month()):
        while not (d.equal(d_date)):
          d_date = d_date.prev()
          n = n + 1
    elif (d.year() < d_date.year()):
      while not (d.equal(d_date)):
        d_date = d_date.prev()
        n = n + 1
    
    return n
