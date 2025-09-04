import math

class SolarCalc:
    """Automates the process of calculating key parameters in solar panel design."""
    
    def __init__(self, load, hours_of_use, hours_of_exposure, sys_Voltage, curr_per_panel, tolerance=95, DoD=75, inverter_rating=0):
        """Initialize names and attributes."""
        self.sys_Voltage = sys_Voltage
        self.curr_per_panel = curr_per_panel
        self.load = load
        self.hours_of_use = hours_of_use
        self.hours_of_exposure = hours_of_exposure
        self.inverter_rating = inverter_rating
        self.tolerance = tolerance
        self.DoD = DoD
        self.standard_inverters = [5, 7.5, 10, 15, 20, 25, 30, 50, 100, 250, 500]  # Market-standard kVA ratings
    

    def battery_bank_capacity(self):
        """Calculate required battery capacity (in Ah and kWh), rounded to nearest market size."""
        # Energy consumption (kWh)
        energy_consumed = self.load * self.hours_of_use

        # Adjust for depth of discharge
        adjusted_energy = energy_consumed / (self.DoD / 100)

        # Convert to Ah
        battery_capacity_Ah = (adjusted_energy * 1000) / self.sys_Voltage

        # Market-standard battery sizes (in kWh)
        standard_batteries = [1, 2.5, 5, 10, 15, 20, 25, 30, 50, 100]

        # Find the nearest size >= required
        nearest_batt_kWh = next((b for b in standard_batteries if b >= adjusted_energy), standard_batteries[-1])

        print(f"You need a battery bank with a capacity of {battery_capacity_Ah:.2f} Ah or {nearest_batt_kWh:.2f} kWh (rounded up)")
        return nearest_batt_kWh
    

    def calc_inverter_rating(self):
        """Find the nearest standard inverter rating based on the load."""
        load_kva = self.load / 0.8  # Convert kW to kVA (PF = 0.8)
        for inverter in self.standard_inverters:
            if inverter >= load_kva:
                return inverter
        return self.standard_inverters[-1]  # if load > all standard sizes
    

    def number_of_solar_panels(self):
        """Calculate the number of solar panels needed."""
        if self.inverter_rating not in self.standard_inverters:
            print('The inverter size you provided does not exist. Should I calculate the nearest inverter for you?')
            answer = input("Yes or No: ")
            if answer.upper() == 'YES':
                self.inverter_rating = self.calc_inverter_rating()
            else:
                return
        
        # Get required battery capacity
        adjusted_energy = self.battery_bank_capacity()

        # Convert energy to current needed during sunlight
        current_needed = adjusted_energy * 1000 / (self.sys_Voltage * self.hours_of_exposure)

        # Apply panel tolerance
        current_per_panel = self.curr_per_panel * (self.tolerance / 100)

        # Calculate number of panels
        number_of_panels = math.ceil(current_needed / current_per_panel)

        print(f'You need exactly {number_of_panels} solar panels')
        return number_of_panels
    

    def design(self):
        """Run full solar system design and return a summary."""
        batt_kWh, batt_Ah = self.battery_bank_capacity()
        inverter = self.calc_inverter_rating()
        panels = self.number_of_solar_panels()
        return {
            "Battery_kWh": batt_kWh,
            "Battery_Ah": batt_Ah,
            "Inverter_kVA": inverter,
            "Panels": panels
        }