class Object:
    def __init__(self, object_id, type_id, name, desc, img, floor, number):
        self._id = object_id
        self._type = type_id
        self._name = name
        self._desc = desc
        self._img = img
        self._floor = floor
        self._number = number

    # make the getter method ID
    def get_id(self):
        return self._id

    # make the setter method ID
    def set_id(self, a):
        self._id = a

    # make the delete method ID
    def del_id(self):
        del self._id
    id = property(get_id, set_id, del_id)

    # make the getter method TYPE
    def get_type(self):
        return self._type

    # make the setter method TYPE
    def set_type(self, a):
        self._type = a

    # make the delete method TYPE
    def del_type(self):
        del self._type
    type = property(get_type, set_type, del_type)

    # make the getter method NAME
    def get_name(self):
        return self._name

    # make the setter method NAME
    def set_name(self, a):
        self._name = a

    # make the delete method NAME
    def del_name(self):
        del self._name
    name = property(get_name, set_name, del_name)

    # make the getter method DESC
    def get_desc(self):
        return self._desc

    # make the setter method DESC
    def set_desc(self, a):
        self._desc = a

    # make the delete method DESC
    def del_desc(self):
        del self._desc
    desc = property(get_desc, set_desc, del_desc)

    # make the getter method IMG
    def get_img(self):
        return self._img

    # make the setter method IMG
    def set_img(self, a):
        self._img = a

    # make the delete method IMG
    def del_img(self):
        del self._img
    img = property(get_img, set_img, del_img)

    # make the getter method FLOOR
    def get_floor(self):
        return self._floor

    # make the setter method FLOOR
    def set_floor(self, a):
        self._floor = a

    # make the delete method FLOOR
    def del_floor(self):
        del self._floor
    floor = property(get_floor, set_floor, del_floor)

    # make the getter method NUMBER
    def get_number(self):
        return self._number

    # make the setter method NUMBER
    def set_number(self, a):
        self._number = a

    # make the delete method NUMBER
    def del_number(self):
        del self._number
    number = property(get_number, set_number, del_number)
