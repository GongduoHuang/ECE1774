# load.py

class Load:
    def __init__(self, name: str, bus1: str, p: float, v_nom: float):
        self.name = str(name)
        self.bus1 = str(bus1)
        self.p = float(p)        # active power (W)
        self.v_nom = float(v_nom)
        self.g = self.calc_g()   # equivalent conductance (S)

    def calc_g(self) -> float:
        if self.v_nom <= 0:
            raise ValueError("Nominal voltage must be > 0.")
        return self.p / (self.v_nom ** 2)

    def __str__(self):
        return (
            f"Load(name='{self.name}', bus1='{self.bus1}', "
            f"p={self.p}, v_nom={self.v_nom}, g={self.g})"
        )


# Test section (must be runnable)
if __name__ == "__main__":
    load1 = Load("Load1", "B", p=50.0, v_nom=10.0)
    print("Load name:", load1.name)
    print("bus1:", load1.bus1)
    print("p (W):", load1.p)
    print("v_nom (V):", load1.v_nom)
    print("g (siemens):", load1.g)
    print("As string:", load1)
