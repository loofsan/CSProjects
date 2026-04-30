##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab Assignment 10 - Metaclass Usage Application
#  Application: Interpolating camelCase into snake_case
#  Description: This is a dict subclass that automatically 
#       interpolates camelCase names into snake_case keys.  
#       It uses the inflection module and it is able to 
#       convert strings between various "string cases". 
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lalab10.py
#  Date: 04/20/25



from typing import Any
import inflection

class CaseInterpolationDict(dict):
    def __setitem__(self, key: str, value: Any):
        super().__setitem__(key, value)
        super().__setitem__(inflection.underscore(key), value)

class CaseInterpolatedMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases):
        return CaseInterpolationDict()

class User(metaclass=CaseInterpolatedMeta):
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName

    def getDisplayName(self):
        return f"{self.firstName} {self.lastName}"

    def greetUser(self):
        return f"Hello {self.getDisplayName()}!"
