#!/usr/bin/python3
"""base module: This module contains the Base class definition."""
import json
import csv


class Base:
    """Definition for the Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance attributes during instanciation.

        Args:
            id: assumed to be an int or None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json string representation of list_objs into a file."""
        filename = cls.__name__ + '.json'
        dictlist = []
        if list_objs is not None and len(list_objs) > 0:
            dictlist = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(dictlist))

    @staticmethod
    def from_json_string(json_string):
        """Return a python object from a json string."""
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creat an instance of a class from a dictionary of its attribute."""
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances of a class from a file containing
        a json string representation of instances of that class.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                dictlist = cls.from_json_string(file.read())
        except IOError:
            return []
        return [cls.create(**dicto) for dicto in dictlist]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV serialization of a list of objects to a file.
        """
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        """
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in dico.items())
                              for dico in list_dicts]
                return [cls.create(**dico) for dico in list_dicts]
        except IOError:
            return []
