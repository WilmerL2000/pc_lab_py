class InputDevice:

    def __init__(self, input_type, brand):
        self._input_type = input_type
        self._brand = brand

    def __str__(self):
        return f''

    @property
    def input_type(self):
        return self._input_type

    @input_type.setter
    def input_type(self,input_type):
        self._input_type = input_type

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand
