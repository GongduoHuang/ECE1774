from circuit import Circuit
from solution import Solution


def main():
    # 1. Define the circuit
    ckt = Circuit("Simple DC Circuit")

    # a. Add buses
    ckt.add_bus("A")
    ckt.add_bus("B")

    # b. Voltage source
    ckt.add_vsource_element("Va", "A", 100.0)

    # c. Resistor
    ckt.add_resistor_element("Rab", "A", "B", 5.0)

    # d. Load
    ckt.add_load_element("Lb", "B", 2000.0, 100.0)

    # 2. Create solution and simulate
    sol = Solution(ckt)
    sol.do_power_flow()

    # 3. Display results
    ckt.print_nodal_voltage()
    ckt.print_circuit_current()


if __name__ == "__main__":
    main()