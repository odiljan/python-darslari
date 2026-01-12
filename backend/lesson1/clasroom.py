# python -m venv venv  

# cop asoslari
  # a = 6
  # def add():
  #  pass
  # print(type(a))
  # print(type{add()})
  
class Car:
    brand = "GM"

    def __init__(self, year, price, color):
        self.year = year
        self.price = price
        self.color = color
        self.is_engine_out = False

    def __str__(self):
        return f"{self.year}-yilgi mashina"

    def __repr__(self):
        return f"Car(year={self.year}, price={self.price}, color='{self.color}')"


obj1 = Car(year=2025, price=10000, color="oq")
obj2 = Car(year=2022, price=8000, color="qizil")
obj3 = Car(year=2000, price=1000, color="qora")

print(obj2.price)
print(obj2.color)
print(obj1)          # __str__
print(repr(obj3))    # __repr__
