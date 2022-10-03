#!/usr/bin/python3
"""
Module square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size - sets width and height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Prints [Square] (<id>) <x>/<y> - <size>"""
        return "[{}] ({}) {}/{} - {}".format(
               self.__class__.__name__, self.id, self.x, self.y,
               self.size)

    def update(self, *args, **kwargs):
        """assign argument to each attribute"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dictt = {}
        dictt["id"] = self.id
        dictt["size"] = self.size
        dictt["x"] = self.x
        dictt["y"] = self.y
        return dictt
