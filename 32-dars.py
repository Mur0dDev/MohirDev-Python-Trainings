class Avto:
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        Avto.__num_avto += 1
        
    def __str__(self):
        return f"Avto: {self.make} {self.model}"

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
print(avto1)

avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", "Carolla", "Silver", 2018, 45000)
avto4 = Avto("GM", "Onix", "Qora", 2023, 15000)
avto5 = Avto("GM", "Monza", "Qizil", 2024, 19000)
avto6 = Avto("Tesla", "Model X", "Qora", 2025, 140000)