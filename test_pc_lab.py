from Computer import Computer
from Keyboard import Keyboard
from Monitor import Monitor
from Mouse import Mouse
from Order import Order

keyboard1 = Keyboard('USB', 'HP')
mouse1 = Mouse('USB', 'HP')
monitor1 = Monitor('HP', 15)
computer1 = Computer('HP', monitor1, keyboard1, mouse1)

keyboard2 = Keyboard('Bluetooth', 'Acer')
mouse2 = Mouse('Bluetooth', 'Acer')
monitor2 = Monitor('Acer', 27)
computer2 = Computer('Acer', monitor2, keyboard2, mouse2)

computers1 = [computer1, computer2]
order1 = Order(computers1)
print(order1)

keyboard3 = Keyboard('USB', 'Dell')
mouse3 = Mouse('USB', 'Dell')
monitor3 = Monitor('Dell', 15)
computer3 = Computer('Dell', monitor3, keyboard3, mouse3)

keyboard4 = Keyboard('Bluetooth', 'MSI')
mouse4 = Mouse('Bluetooth', 'MSI')
monitor4 = Monitor('MSI', 27)
computer4 = Computer('MSI', monitor4, keyboard4, mouse4)

computers2 = [computer3, computer4]
order2 = Order(computers2)
print(order2)