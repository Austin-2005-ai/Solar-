from Solar_Calc import SolarCalc

# Collect inputs from the user
load = float(input('What is the load the solar is expected to carry (in kW)? '))
time_of_use = float(input('How many hours will the system run daily? '))
time_of_exposure = float(input('How many hours of sunlight are available daily? '))
sys_voltage = float(input('What is the system voltage (e.g., 12, 24, 48)? '))
curr_per_panel = float(input('How much current (in Amps) can each solar panel supply? '))

# Optional inputs with defaults
tolerance = input('Panel tolerance in % [default = 95]: ')
tolerance = float(tolerance) if tolerance.strip() else 95

DoD = input('Battery depth of discharge in % [default = 75]: ')
DoD = float(DoD) if DoD.strip() else 75

inverter_size = input('Enter inverter size (kVA) [leave blank to auto-select]: ')
inverter_size = float(inverter_size) if inverter_size.strip() else 0

# Create SolarCalc instance
system = SolarCalc(load, time_of_use, time_of_exposure, sys_voltage, curr_per_panel, tolerance, DoD, inverter_size)

# Run calculations
print("\n--- Solar Design Results ---")
battery = system.battery_bank_capacity()
inverter = system.calc_inverter_rating()
panels = system.number_of_solar_panels()

print(f"\nSummary:\n- Battery Bank: {battery:.2f} kWh\n- Inverter Size: {inverter} kVA\n- Solar Panels: {panels}")