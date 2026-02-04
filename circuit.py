from bus import Bus
from resistor import Resistor
from load import Load
from vsource import Vsource

class Circuit:
    def __init__(self, name: str):
        # Attributes, Milestone 3
        self.name = str(name)
        self.buses = {}          # Dict[str, Bus]
        self.resistors = {}      # Dict[str, Resistor]
        self.loads = {}          # Dict[str, Load]
        self.vsource = None      # Vsource object
        self.i = 0.0             # Current attribute named 'i'

    # Methods， Milestone 3
    def add_bus(self, bus_name: str):
        if bus_name not in self.buses:
            self.buses[bus_name] = Bus(bus_name, 0.0)

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        self.add_bus(bus1)
        self.add_bus(bus2)
        self.resistors[name] = Resistor(name, bus1, bus2, r)

    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        self.add_bus(bus1)
        self.loads[name] = Load(name, bus1, p, v)

    def add_vsource_element(self, name: str, bus1: str, v: float):
        self.add_bus(bus1)
        self.vsource = Vsource(name, bus1, v)
        self.buses[bus1].v = v

    def set_i(self, i: float):
        self.i = float(i)

    def print_nodal_voltage(self):
        print("--- Nodal Voltages ---")
        for name in sorted(self.buses):
            print(f"bus {name} voltage = {self.buses[name].v:.1f} V")

    def print_circuit_current(self):
        print(f"Circuit current = {self.i:.1f} A")