## @file pos_adt.py
#  @author Waseef Nayeem
#  @brief GPosT source code file, contains the implementation of the GPosT ADT used to represent geographic coordinates.
#  @date 2020-01-20

from math import degrees, radians, atan2, asin, cos, sin, sqrt


## @brief An ADT that represents geographic coordinates.
#  @details An ADT that represents geographic coordinates as well as various functions for geographic calculations,
#  such as distance between two points.
#  Some implementation assumptions that were made include constraining latitude and longitude values to valid range
#  instead of converting out of range values.
class GPosT:

    ## @brief GPosT constructor
    #  @details Constructor that builds the GPosT object from latitude and longitude values
    #  @param lat Latitude
    #  @param long Longitude
    #  @throws ValueError Error raised if latitude or longitude values are out of the valid range
    def __init__(self, lat, long):
        if lat < -90 or lat > 90:
            raise ValueError("Invalid latitude: {}".format(lat))

        if long < -180 or lat > 180:
            raise ValueError("Invalid longitude: {}".format(lat))

        self.__lat = lat
        self.__long = long

    ## @brief Getter for latitude variable
    #  @return Latitude variable
    def lat(self):
        return self.__lat

    ## @brief Getter for longitude variable
    #  @return Longitude variable
    def long(self):
        return self.__long

    ## @brief Comparison function that determines if the current position is west of the passed position object
    #  @param p GPosT object to be compared against
    #  @return True if the current position is west of passed position parameter, False otherwise
    def west_of(self, p):
        return self.__long < p.long()

    ## @brief Comparison function that determines if the current position is north of the passed position object
    #  @param p GPosT object to be compared against
    #  @return True if the current position is north of passed position parameter, False otherwise
    def north_of(self, p):
        return self.__lat > p.lat()

    ## @brief Comparison function that determines if the current position is "equal to" the passed position object.
    #  This is defined as the two positions being less than 1 km in distance from each other.
    #  @param p GPosT object to be compared against
    #  @return True if the current position is within 1 km of passed position parameter, False otherwise
    def equal(self, p):
        return self.distance(p) < 1.0

    ## @brief Function that moves the current position by a certain distance along a specified bearing.
    #  @details Mutator function that moves the current function a specified distance in km along a given bearing in degrees.
    #  Formula courtesy of https://www.movable-type.co.uk/scripts/latlong.html
    #  @param b Bearing in degrees
    #  @param d Distance in kilometres (km)
    def move(self, b, d):
        r = 6371e3
        d *= 1000
        phi1 = radians(self.__lat)
        lambda1 = radians(self.__long)
        b = radians(b)
        phi2 = asin(sin(phi1) * cos(d / r) + cos(phi1) * sin(d / r) * cos(b))
        lambda2 = lambda1 + atan2(sin(b) * sin(d / r) * cos(phi1), cos(d / r) - sin(phi1) * sin(phi2))

        self.__lat = degrees(phi2)
        self.__long = degrees(lambda2)

    ## @brief Calculates great-circle distance between two coordinates using the haversine formula.
    #  Source: https://www.movable-type.co.uk/scripts/latlong.html
    #  @param p GPosT object to calculated distance between
    #  @return Distance between the two positions (in km)
    def distance(self, p):
        r = 6371e3  # metres
        phi1 = radians(self.__lat)
        phi2 = radians(p.lat())
        delta_phi = radians(p.lat() - self.__lat)
        delta_lambda = radians(p.long() - self.__long)

        a = sin(delta_phi / 2) * sin(delta_phi / 2) + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) * sin(delta_lambda / 2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        dist = r * c
        return dist / 1000

    ## @brief Calculates time taken to travel from current position to end position and returns arrival date.
    #  @details Given an end point, starting date and speed, this function calculates the time it takes to travel from
    #  start position (current object) to end position while traveling at a specified speed. It then calculates the
    #  arrival date from the time taken and the starting date.
    #  @param p GPosT object for the end position
    #  @param d DateT object for starting date
    #  @param s Travel speed in km/day
    #  @throws ValueError Raises error if speed is negative
    #  @return DateT object for arrival date
    def arrival_date(self, p, d, s):
        if s < 0:
            raise ValueError("Speed must be positive")

        dist = self.distance(p)
        days = dist / s

        for i in range(int(days)):
            d = d.next()

        return d
