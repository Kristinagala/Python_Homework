from address import Address
from mailing import Mailing

to_address = Address("158465", "Москва", "Комсомольская", "3", "7")
from_address = Address("258963", "Санкт-Петербург", "Тамбасова", "10", "3")

box = Mailing(to_address, from_address, 1000, "РП524445")
print(box)
