#!/usr/bin/python3


class Base:
    """main base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json of list"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to _file(cls, list_objs):
        """Save json"""
        name = cls.__name__ + ".json"
        with open(name, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_dicts = [opn.todictionary() for opn in list_objs]

    @staticmethod
    def from_json_string(json_string):
        """json string list"""
        if json_string is None or json_string == "[]":
            return[]
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return instance"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == 'Rectangle':
            dmy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dmy = cls(1)

        dmy.update(**dictionary)
        return (dmy)
