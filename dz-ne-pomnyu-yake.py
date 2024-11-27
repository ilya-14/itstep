class Tvarina:
    def __init__(self, imya, vid, vozrast):
        self.imya = imya
        self.vid = vid
        self.vozrast = vozrast

    def zvuk(self):
        return "Тварина видає звук"


class Sobaka(Tvarina):
    def __init__(self, imya, vozrast, poroda):
        super().__init__(imya, "Собака", vozrast)
        self.poroda = poroda

    def zvuk(self):
        return "Гав-гав!"


class Kit(Tvarina):
    def __init__(self, imya, vozrast, poroda):
        super().__init__(imya, "Кіт", vozrast)
        self.poroda = poroda

    def zvuk(self):
        return "Мяу!"


class Osoba:
    def __init__(self, imya, vіk):
        self.imya = imya
        self.vik = vіk

    def get_vik(self):
        return self.vik


class Vodiy(Osoba):
    def __init__(self, imya, vik, nomer_posvidchennya):
        super().__init__(imya, vik)
        self.nomer_posvidchennya = nomer_posvidchennya


class TransportnyyZasib:
    def __init__(self, shvydkist):
        self.shvydkist = shvydkist

    def peremishchennya(self):
        return f"Транспортний засіб рухається зі швидкістю {self.shvydkist} км/год"


class Avtomobil(TransportnyyZasib):
    def __init__(self, shvydkist, marka, model):
        super().__init__(shvydkist)
        self.marka = marka
        self.model = model

    def peremishchennya(self):
        return f"Автомобіль {self.marka} {self.model} рухається зі швидкістю {self.shvydkist} км/год"


class Samolyot(TransportnyyZasib):
    def __init__(self, shvydkist, tip):
        super().__init__(shvydkist)
        self.tip = tip

    def peremishchennya(self):
        return f"Самоліт типу {self.tip} летить зі швидкістю {self.shvydkist} км/год"


sobaka = Sobaka("Бобік", 3, "Тер'єр")
kit = Kit("Мурчик", 5, "Перс")

print(sobaka.zvuk())  # Гав-гав!
print(kit.zvuk())  # Мяу!

osoba = Osoba("Іван", 25)
vodiy = Vodiy("Олександр", 30, "AB1234567")

print(osoba.get_vik())  # 25
print(vodiy.nomer_posvidchennya)  # AB1234567

avtomobil = Avtomobil(120, "Toyota", "Corolla")
samolyot = Samolyot(900, "Boeing 747")

print(avtomobil.peremishchennya())
print(samolyot.peremishchennya())
