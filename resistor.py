# resistor.py
class Resistor:
    def __init__(self, name: str, bus1: str, bus2: str, r: float):
        self.name = str(name)
        self.bus1 = str(bus1)
        self.bus2 = str(bus2)
        self.r = float(r)
        self.g = self.calc_g()

    def calc_g(self) -> float:
        if self.r <= 0:
            raise ValueError("Resistance must be > 0")
        return 1.0 / self.r

# load.py
class Load:
    def __init__(self, name: str, bus1: str, p: float, v_nom: float):
        self.name = str(name)
        self.bus1 = str(bus1)
        self.p = float(p)
        self.v_nom = float(v_nom)
        self.g = self.calc_g()

    def calc_g(self) -> float:
        if self.v_nom <= 0:
            raise ValueError("Nominal voltage must be > 0")
        return self.p / (self.v_nom ** 2)

# vsource.py
class Vsource:
    def __init__(self, name: str, bus1: str, v: float):
        self.name = str(name)
        self.bus1 = str(bus1)
        self.v = float(v)