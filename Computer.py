class Computer:

    computer_counter = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.computer_counter += 1
        self._id_computer = Computer.computer_counter
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    def __str__(self):
        return f'''
                {self.name} : {self.id_computer }
                Monitor: {self.monitor}
                Keyboard: {self.keyboard}
                Mouse: {self.mouse}
        '''

    @property
    def id_computer(self):
        return self._id_computer

    @property
    def name(self):
        return self._name

    @property
    def monitor(self):
        return self._monitor

    @property
    def keyboard(self):
        return self._keyboard

    @property
    def mouse(self):
        return self._mouse