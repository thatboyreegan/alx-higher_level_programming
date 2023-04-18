#!/usr/bin/python3
"""Defines a class Base"""

import json
import csv
import sys
import turtle


class Base:
    """class called Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a new instance

        Args:
            id ( optional): id of the base. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serializes to a json string

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            json str: json representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation to a file

        Args:
            list_objs (list): lsit of instances
        """
        filename = cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            with open(filename, "w") as f:
                f.write("[]")
        else:
            dictionarie_s = [cls.to_dictionary(obj) for obj in list_objs]
            with open(filename, "w") as f:
                f.write(cls.to_json_string(dictionarie_s))

    @staticmethod
    def from_json_string(json_string):
        """
        returns a list of json string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of inctances
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []

        dict_s = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in dict_s]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in CSV format
        Args:
            list_objs (list): list of objects to serialize
        """
        a_list = [cls.to_dictionary(obj) for obj in list_objs]
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            format = ["id", "width", "height", "x", "y"]
        else:
            format = ["id", "size", "x", "y"]

        with open(filename, "w") as csv_file:
            obj_instance = csv.DictWriter(csv_file, fieldnames=format)
            obj_instance.writeheader()
            obj_instance.writerows(a_list)

    @classmethod
    def load_from_file_csv(cls):
        """
        desializes in CSV format
        """
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r") as csv_file:
                read = csv.DictReader(csv_file)

                for dict in read:
                    for key, value in dict.items():
                        try:
                            dict[key] = int(value)
                        except ValueError:
                            sys.exit("{} must be an intger.\
                                Line on csv file: {}".format(key,
                                                             read.line_num))
                    dict_s = []
                    dict_s.append(dict)
                return [cls.create(**dict) for dict_h in dict_s]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws all the rectangles and squares
        """
        t = turtle.Turtle()
