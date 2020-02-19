## @file date_adt.py
#  @author Waseef Nayeem
#  @brief DateT source code file, contains the implementation of the DateT ADT used to represent Gregorian calendar dates.
#  @date 2020-01-20


## @brief An ADT that represents a date on the Gregorian calendar.
#  @details An ADT that represents a date on the Gregorian calendar.
#  It also implements various functions related to date calculations
#  Some implementation assumptions that were made include not supporting BCE years. I also chose to include
#  parameter validity checking even though it was not explicitly required.
class DateT:

    ## @brief DateT constructor
    #  @details Constructor that builds the DateT object from day, month and year parameters
    #  @param d Day
    #  @param m Month
    #  @param y Year
    #  @throws ValueError Error raised if specified day, month or year are invalid
    def __init__(self, d, m, y):
        self.days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

        if y < 0:
            raise ValueError('Invalid year: {}'.format(y))

        if m < 1 or m > 12:
            raise ValueError('Invalid month: {}'.format(m))

        if d < 1 or d > 28 and self.days_in_month[m - 1] == 28:
            if not (d == 29 and ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))):
                raise ValueError('Invalid day {} for month {} of year {}'.format(d, m, y))
        elif d < 1 or d > self.days_in_month[m - 1]:
            raise ValueError('Invalid day {} for month {} of year {}'.format(d, m, y))

        self.__d = d
        self.__m = m
        self.__y = y

    ## @brief Getter for day variable
    #  @return Day variable
    def day(self):
        return self.__d

    ## @brief Getter for month variable
    #  @return Month variable
    def month(self):
        return self.__m

    ## @brief Getter for year variable
    #  @return Year variable
    def year(self):
        return self.__y

    ## @brief Returns a DateADT object that is one day ahead of current object
    #  @return DateADT object one day after current
    def next(self):
        next_d = self.__d + 1
        next_m = self.__m
        next_y = self.__y

        if self.__d == 28 and self.days_in_month[self.__m - 1] == 28:
            if not ((self.__y % 4 == 0 and self.__y % 100 != 0) or (self.__y % 400 == 0)):
                next_d = 1
                next_m = self.__m + 1
        elif self.__d == 29 and self.days_in_month[self.__m - 1] == 28:
            next_d = 1
            next_m = self.__m + 1
        elif self.__d == 30 and self.days_in_month[self.__m - 1] == 30:
            next_d = 1
            next_m = self.__m + 1
        elif self.__d == 31 and self.days_in_month[self.__m - 1] == 31:
            next_d = 1
            next_m = self.__m + 1
            if self.__m == 12:
                next_m = 1
                next_y = self.__y + 1

        return DateT(next_d, next_m, next_y)

    ## @brief Returns a DateADT object that is one day behind the current object
    #  @return DateADT object one day before current
    def prev(self):
        prev_d = self.__d - 1
        prev_m = self.__m
        prev_y = self.__y

        if self.__d == 1 and self.days_in_month[self.__m - 2] == 28:
            prev_m = self.__m - 1
            if (self.__y % 4 == 0 and self.__y % 100 != 0) or (self.__y % 400 == 0):
                prev_d = 29
            else:
                prev_d = 28
        elif self.__d == 1 and self.days_in_month[self.__m - 2] == 30:
            prev_d = 30
            prev_m = self.__m - 1
        elif self.__d == 1 and self.days_in_month[self.__m - 2] == 31:
            prev_d = 31
            prev_m = self.__m - 1
            if self.__m == 1:
                prev_m = 12
                prev_y = self.__y - 1

        return DateT(prev_d, prev_m, prev_y)

    ## @brief Comparison function that determines if the current object is before the passed date object
    #  @param date DateT object to be compared against
    #  @return True if the current date is before date parameter, False otherwise
    def before(self, date):
        if self.__y < date.year():
            return True
        elif self.__y == date.year() and self.__m < date.month():
            return True
        elif self.__y == date.year() and self.__m == date.month() and self.__d < date.day():
            return True

        return False

    ## @brief Comparison function that determines if the current object is after the date parameter
    #  @param date DateT object to be compared against
    #  @return True if the current date is after date parameter, False otherwise
    def after(self, date):
        if self.__y > date.year():
            return True
        elif self.__y == date.year() and self.__m > date.month():
            return True
        elif self.__y == date.year() and self.__m == date.month() and self.__d > date.day():
            return True

        return False

    ## @brief Comparison function that determines if the current object is same date as the passed parameter
    #  @param date DateT object to be compared against
    #  @return True if the current date is identical to the date parameter, False otherwise
    def equal(self, date):
        return date.day() == self.__d and date.month() == self.__m and date.year() == self.__y

    ## @brief Function that returns a DateT object N number of days after the current date object
    #  @param n Number of days to add to current date object
    #  @throws ValueError Raises error if n is negative
    #  @return DateADT object N days later
    def add_days(self, n):
        if n < 0:
            raise ValueError("Cannot add negative number of days")

        new_day = DateT(self.__d, self.__m, self.__y)

        for i in range(n):
            new_day = new_day.next()

        return new_day

    ## @brief Calculates the number of days between the current date object and a given date object parameter
    #  @param date Date object used to calculate days between current date object
    #  @return Integer value representing the number of days between the two dates
    def days_between(self, date):
        counter = 0

        before_date = self if self.before(date) else date
        after_date = self if self.after(date) else date

        while not after_date.equal(before_date):
            before_date = before_date.next()
            counter += 1

        return counter
