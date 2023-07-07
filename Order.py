class Order:

    order_counter = 0
    order_list = []

    def __init__(self, computers):
        Order.order_counter += 1
        self._id_order = Order.order_counter
        self._computers = computers

    def __str__(self):
        computers_str = ''
        for computer in self._computers:
            computers_str += computer.__str__()

        return f'''
            Order: {self._id_order}
            Computers: {computers_str}
        '''


    def add_computer_to_order(self, computer):
        self._computers.append(computer)
