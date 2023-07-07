from InputDevice import InputDevice


class Keyboard(InputDevice):
    keyboard_counter = 0

    def __init__(self, input_type, brand):
        Keyboard.keyboard_counter +=1
        self._id_keyboard = Keyboard.keyboard_counter
        super().__init__(input_type, brand)

    def __str__(self):
        return f'Id: {self._id_keyboard}, Brand: {self.brand}, Input Type: {self.input_type}'
