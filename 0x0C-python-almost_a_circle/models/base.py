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
    def save_to_file(cls, list_objs):
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

    @classmethod
    def load_from_file(cls):
        """Return list instance"""
        name = cls.__name__ + ".json"
        list_inst = []
        list_dict = []

        if os.path.exists(name):
            with open(name, 'r') as my_file:
                my_str = my_file.read()
                list_dict = cls.from_json_string(my_str)
                for dict in list_dict:
                    list_inst.append(cls.create(**dictionary))
        return (list_inst)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """steralizes list_objs then save"""
        name = cls.__name__ + ".csv"
        with open(name, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                else:
                    names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, names=names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Desterializes"""
        name = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                else:
                    names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, names=names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                        for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangle using turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.shape("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sqr in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sqr.x, sqr.y)
            turt.down()
            for i in range(2):
                turt.forward(sqr.width)
                turt.left(90)
                turt.forward(sqr.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
