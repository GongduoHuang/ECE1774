class Solution:
    def __init__(self, circuit):
        # Attribute as per Milestone 4 section 1.a
        self.circuit = circuit

    def do_power_flow(self):
        """
        Solves the circuit using conductance values.
        Specific for a series circuit with one resistor and one load.
        """
        ckt = self.circuit

        # Accessing components from dictionaries
        resistor = list(ckt.resistors.values())[0]
        load = list(ckt.loads.values())[0]
        va = ckt.vsource.v

        # Calculate conductance values
        g_r = resistor.calc_g()
        g_load = load.calc_g()

        # Step 1: Calculate total current
        # I = Va * (Gr * Gload) / (Gr + Gload)
        current = va * (g_r * g_load) / (g_r + g_load)
        ckt.set_i(current)

        # Step 2: Determine voltage at bus B
        # Vb = Va - I * R
        vb = va - (current * resistor.r)

        # Update bus B voltage in the circuit object
        bus_b_name = resistor.bus2
        ckt.buses[bus_b_name].v = vb