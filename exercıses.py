# SINIFLAR bu bu zamana kadar gordugumuz en genis tanim grubu

class Person():
    #name="" buralari doldurmak pythonda zorunlu degil
    #age=""
    #gender=""
    job="developer" # buraya herkeste istisnasiz cikmasini istedigim bir deger yazabiliriz
    boy= ""           #veya bos birakabilir ve kullanicinin tercih
    #method, initializer
    def __init__(self, name, age, gender, city):
        self.name=name
        self.age=age
        self.gender=gender
        self.city=city
Talha=Person("Talha", 27, "Erkek", "Samsun")

print(Talha.name)
print(Talha.age)
print(Talha.gender)
print(Talha.city)
print(Talha.job)
Talha.boy= 182
print(Talha.boy)


class Car():
    def __init__(self, model, colour, mark):
        self.model=model
        self.colour=colour
        self.mark=mark

BMW=Car(1992, "blue", "bmw")
print("others")
print(BMW.model)
print(BMW.colour)
print(BMW.mark)

