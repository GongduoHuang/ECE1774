# vsource.py

class Vsource:
    def __init__(self, name: str, bus1: str, v: float):
        self.name = str(name)
        self.bus1 = str(bus1)
        self.v = float(v)

    def __str__(self):
        return f"Vsource(name='{self.name}', bus1='{self.bus1}', v={self.v})"


# Test section (must be runnable)
if __name__ == "__main__":
    vs1 = Vsource("V1", "A", 12.0)
    print("Vsource name:", vs1.name)
    print("Connected bus:", vs1.bus1)
    print("Source voltage:", vs1.v)
    print("As string:", vs1)
