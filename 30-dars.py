class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        info = f"Ism: {self.ism}, Familiya: {self.familiya}"
        info += f"Passport: {self.passport}, Tugilgan yili: {self.tyil}"
        
        return info
    
    def get_age(self, yil):
        return f"Siz {yil - self.tyil} yoshdasiz"

    
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f"Ism: {self.ism}, Familiya: {self.familiya}"
        info += f"Bosqich: {self.bosqich}, ID: {self.idraqam}"
        
        return info
    
class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def get_manzil(self):
        manzil = f"Viloyat: {self.viloyat}, Tuman: {self.tuman}, "
        manzil += f"Kocha: {self.kocha}, Uy: {self.uy}"
        
        return manzil
    
inson = Shaxs("Murodjon", "Sadullaev", "FA6932585", 1997)    
talaba1_manzil = Manzil(106, "Chaman", "Bogot", "Khorezm")
talaba1 = Talaba("Murodjon", "Sadullaev", "FA6932585", 1997, 1610161, talaba1_manzil)