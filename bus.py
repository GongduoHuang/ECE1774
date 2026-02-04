class Bus:
    def __init__(self, name: str, v: float):
        self.name = str(name)
        # This triggers the setter for validation
        self.v = v

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, voltage: float):
        # Validation as per teacher's clarification notice
        if not isinstance(voltage, (float, int)):
            raise TypeError("Voltage must be a numeric value")
        elif voltage < 0.0:
            raise ValueError("Voltage must be a positive float")
        else:
            self._v = float(voltage)

    def __str__(self):
        return f"Bus(name='{self.name}', v={self.v})"