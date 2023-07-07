class Monitor:
    monitor_counter = 0

    def __init__(self, brand, height):
        Monitor.monitor_counter += 1
        self._id_monitor = Monitor.monitor_counter
        self._brand = brand
        self._height = height

    def __str__(self):
        return f'Id: {self.id_monitor}, Brand: {self.brand}, Height: {self.height}'

    @property
    def id_monitor(self):
        return self._id_monitor

    @id_monitor.setter
    def id_monitor(self, id_monitor):
        self._id_monitor = id_monitor

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height