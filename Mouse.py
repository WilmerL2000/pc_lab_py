from InputDevice import InputDevice


class Mouse(InputDevice):
    mouse_counter = 0

    def __init__(self, input_type, brand):
        Mouse.mouse_counter += 1
        self._mouse_id = Mouse.mouse_counter
        super().__init__(input_type, brand)

    def __str__(self):
        return f'Id: {self._mouse_id}, Brand: {self.brand}, Input Type: {self.input_type}'
