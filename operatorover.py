class Meri:
    name = ""

    def __init__(self, name):
        self.name = name

    def __add__(self,others,bro):
        print(f"ChatGpt tm mery 1 achy dost hu. {others} tmhy slam khta ha")
        print(f"{bro} or {others} dono apas mein bhai ha")

m1 = Meri("Waleed Haider")
m1.__add__("Waleed Haider" , "Touseeq Haider")