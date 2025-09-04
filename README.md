# Solar-
# 🔋 Solar System Design Calculator

This repository contains Python scripts that assist engineers in preliminary solar PV system sizing.  
It automates the calculation of **battery capacity, inverter sizing, and solar panel requirements** using user-provided load and environmental parameters.  

---

## 📂 Repository Structure
- **`Solar_Calc.py`** → Core module containing the `SolarCalc` class and methods for system sizing.  
- **`solar.py`** → Entry script (interactive), imports `SolarCalc` and prompts for design parameters.  

---

## ⚡ Engineering Features
- **Battery Bank Sizing**
  - Computes required **energy storage (kWh)**.  
  - Converts to **ampere-hours (Ah)** given system DC bus voltage.  
  - Incorporates **Depth of Discharge (DoD)** for realistic battery sizing.  
  - Rounds to the nearest **market-available capacity**.  

- **Inverter Sizing**
  - Converts load (kW) to apparent power (kVA) using **power factor = 0.8**.  
  - Selects the nearest available rating from a **standardized inverter list** (0.8 – 500 kVA).  

- **Solar Array Sizing**
  - Determines current demand during sunlight hours.  
  - Accounts for **module tolerance** (e.g., 95%).  
  - Calculates the minimum **number of PV modules** required.  

---

## ▶️ Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/Austin-2005-ai/Solar-.git
   cd Solar-
Run the main script:

bash
Copy code
python solar.py
Provide the required inputs:

Load demand (kW)

Hours of daily operation

Average daily sun hours

System DC bus voltage (12 / 24 / 48 V)

Module rated current (A)

Panel tolerance (%)

Battery depth of discharge (%)

Optional: inverter rating (kVA)

📊 Example Output
yaml
Copy code
--- Solar Design Results ---
You need a battery bank with a capacity of 877.19 Ah or 21.05 kWh
The inverter size you provided does not exist. Should I calculate the nearest inverter for you?
Yes or No: yes
You need exactly 9 solar panels

Summary:
- Battery Bank: 21.05 kWh
- Inverter Size: 3.5 kVA
- Solar Panels: 9
🧮 Assumptions
Power factor (PF): 0.8 (residential/industrial loads).

Battery DoD: Adjustable (default = 75%).

System voltage levels: 12 V, 24 V, 48 V DC bus.

Tolerance factor: Accounts for panel rating deviations.

Standard inverter ratings are predefined to reflect market availability.

🔧 Requirements
Python 3.8+

Standard library only (math).

📜 License
Open-source under MIT License. Suitable for academic, industrial, and personal use.

✍️ Designed for engineers and system integrators to accelerate feasibility studies and preliminary designs.
