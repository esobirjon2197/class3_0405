
# 5-m
class Avtomabil:
    def __init__(self, model, tezlik):
        self.madel = model
        self.__tezlik = tezlik

    def tezlashtir(self,qiymat):
        self.__tezlik += qiymat

    def sekinlashtir(self,qiymat):
        self.__tezlik -= qiymat

    def info(self):
        print(f"Car madel: {self.madel}")
        print(f"Speed: {self.__tezlik}")

a1 = Avtomabil("BMW", 220)
a1.info()

a1.tezlashtir(100)
a1.info()

a1.sekinlashtir(20)
a1.info()



# 6-m
class Ishchi:
    def __init__(self, fullname, oylik):
        self.fullname = fullname
        self.__oylik = oylik

    def oshirish(self, qiymat):
        self.__oylik += qiymat

    def kamaytir(self, qiymat):
        self.__oylik -= qiymat

    def info(self):
        print(f"Ishchi: {self.fullname}")
        print(f"Oylik: {self.__oylik}")


i1 = Ishchi("Ali Valiyev", 3000)
i1.info()

i1.oshirish(500)
i1.info()

i1.kamaytir(200)
i1.info()
