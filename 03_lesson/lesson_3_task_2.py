from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "Galaxy S", "+79516665544")
phone2 = Smartphone("Apple", "iPhone 11", "+79000000000")
phone3 = Smartphone("Хiaomi", "Redmi 10", "+79111111111")
phone4 = Smartphone("Huawei", "P30 Pro", "+79598742536")
phone5 = Smartphone("Honor", "X9m", "+79312569874")


catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

phone1.sayName()
phone2.sayName()
phone3.sayName()
phone4.sayName()
phone5.sayName()
