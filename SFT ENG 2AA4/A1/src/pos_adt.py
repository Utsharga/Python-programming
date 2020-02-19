## @file pos_adt.py
#  @author Utsharga Rozario
#  @brief Provides the GPosT ADT for representating global position in degrees
#  @date 13/01/2020

from math import *
from date_adt import *

## @brief An ADT that represents a global position coordinates in degrees
class GPosT:

    ## @brief Date Constructor
    #  @details Initializes a GPosT object with phi (latitude in degrees) and lamda (longitude in degrees)
    #  @param phi The latitude in degrees
    #  @param lamda The longitude in degrees
    #  @exception ValueError throws if the the latitude or longitude is out of range
    def __init__(self, phi, lamda):
        if (phi < -90 or phi > 90):
            raise ValueError("Latitude is out of range")
        elif (lamda < -180 or lamda > 180):
            raise ValueError("Longitude is out of range")
        self.phi = phi
        self.lamda = lamda

    ## @brief Gets the latitude of the position
    #  @return The latitude of the position
    def lat(self):
        return self.phi

    ## @brief Gets the longitude of the position
    #  @return The longitude of the position
    def long(self):
        return self.lamda

    ## @brief Determines whether the parameter position is west of current position
    #  @param p Position of another global position of type GPosT
    #  @return Returns True if the current position is west of the parameter position, False if otherwise
    def west_of(self, p):
        if (p.long() > self.long()):
            return True
        else:
            return False

    ## @brief Determines whether the parameter position is north of current position
    #  @param p Position of another global position of type GPosT
    #  @return True if the curent position is north of the parameter position, false if otherwise
    def north_of(self, p):
        if (p.lat() < self.lat()):
            return True
        else:
            return False

    ## @brief Determines whether the parameter position is equal to the current position
    #  @details The method calculates whether the parameter position is equal to or less than 1km
    #           from current position which is then considered equal to the position
    #  @param p Position of another global position of type GPosT
    #  @return True if the parameter position is equal to the current position, false if otherwise
    def equal(self, p):
        if (self.long() == p.long() and self.lat() == p.lat()):
            return True
        elif (self.distance(p) < 1):
            return True
        else:
            return False
    
    ## @brief Translates the current global position in accordance to the provided parameters
    #  @param b The bearing at which to move the current posistion
    #  @param d The distance to move the current position
    def move(self, b, d):
        R = 6371
        delta = d/R
        phi1 = self.lat() * (pi/180)
        lamda1 = self.long() * (pi/180)
        b_rad = b * (pi/180)
        phi2 = asin(sin(phi1)*cos(delta) + cos(phi1)*sin(delta)*cos(b_rad))
        lamda2 = lamda1 +  atan2( (sin(b_rad)*sin(delta)*cos(phi1)), (cos(delta) - sin(phi1)*sin(phi2)))
        self.phi = phi2 * (180/pi)
        self.lamda = lamda2 * (180/pi)

    ## @brief Calculates the distance between current position and parameter position
    #  @param p Position of another global position of type GPosT
    #  @return Returns distance between two points
    def distance(self, p):
        R = 6371
        phi1 = self.lat() * (pi/180)
        phi2 = p.lat() * (pi/180)
        delphi = (self.lat() - p.lat()) * (pi/180)
        dellamda = (self.long() - p.long()) * (pi/180)

        a = sin(delphi/2)*sin(delphi/2) + cos(phi1)*cos(phi2)*sin(dellamda/2)*sin(dellamda/2)
        c = 2*atan2(sqrt(a), sqrt(1-a))
        d = R*c

        return d

    ## @brief Calculates the date of arrival from
    #  @details Calculates the distance between the parameter position and current position,
    #           Calculates time in days required to reach parameter position using linear velocity formula (t = d/s),
    #           Determines arrival date by by adding number of days to current date using add_days method
    #  @param p Position of another global position of type GPosT
    #  @param d Current date of type DateT
    #  @param s Speed of someone moving from current position in km/day
    #  @return Returns distance between two points
    def arrival_date(self, p, d, s):
        dis = self.distance(p)
        time = ceil(dis/s) 
        a_date = d.add_days(time - 1)

        return a_date
