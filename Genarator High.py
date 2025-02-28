import random
import time

class SensorDataGenerator:
    def __init__(self):
        self.emergency = False  # Flag to indicate if an emergency is happening
        self.emergency_start_time = None

    def start_emergency(self):
        """
        Simulate the start of an emergency (e.g., fire or explosion).
        """
        self.emergency = True
        self.emergency_start_time = time.time()
        print("Emergency started! Sensor data will increase rapidly.")

    def stop_emergency(self):
        """
        Stop the emergency simulation.
        """
        self.emergency = False
        print("Emergency stopped. Sensor data returning to normal.")

    def generate_me4_so2_data(self):
        """
        Generate random data for ME4-SO2 sensor.
        """
        if self.emergency:
            # Simulate a rapid increase in SO2 concentration during an emergency
            so2_concentration = round(random.uniform(10, 200), 1)  # SO2 concentration in ppm (higher range)
        else:
            so2_concentration = round(random.uniform(0, 20), 1)  # Normal SO2 concentration in ppm

        temperature = round(random.uniform(-20, 50), 1)  # Temperature in Celsius
        humidity = round(random.uniform(15, 90), 1)  # Humidity in %

        return {
            "SO2 Concentration (ppm)": so2_concentration,
            "Temperature (°C)": temperature,
            "Humidity (%)": humidity
        }

    def generate_ze40_tvoc_data(self):
        """
        Generate random data for ZE40-TVOC sensor.
        """
        if self.emergency:
            # Simulate a rapid increase in TVOC concentration during an emergency
            tvoc_concentration = round(random.uniform(3, 10), 1)  # TVOC concentration in ppm (higher range)
        else:
            tvoc_concentration = round(random.uniform(0, 5), 1)  # Normal TVOC concentration in ppm

        temperature = round(random.uniform(0, 50), 1)  # Temperature in Celsius
        humidity = round(random.uniform(15, 90), 1)  # Humidity in %

        return {
            "TVOC Concentration (ppm)": tvoc_concentration,
            "Temperature (°C)": temperature,
            "Humidity (%)": humidity
        }

    def generate_zphs01b_data(self):
        """
        Generate random data for ZPHS01B sensor.
        """
        if self.emergency:
            # Simulate a rapid increase in sensor readings during an emergency
            pm25 = random.randint(500, 1000)  # PM2.5 concentration in µg/m³ (higher range)
            co2 = random.randint(2000, 5000)  # CO2 concentration in ppm (higher range)
            tvoc = random.randint(2, 3)  # TVOC grade (higher range)
            temperature = round(random.uniform(30, 65), 1)  # Temperature in Celsius (higher range)
            humidity = round(random.uniform(50, 100), 1)  # Humidity in % (higher range)
            ch2o = round(random.uniform(1, 6.250), 3)  # Formaldehyde concentration in mg/m³ (higher range)
            co = round(random.uniform(100, 500), 1)  # CO concentration in ppm (higher range)
            o3 = round(random.uniform(5, 10), 2)  # Ozone concentration in ppm (higher range)
            no2 = round(random.uniform(5, 10), 2)  # NO2 concentration in ppm (higher range)
        else:
            # Normal sensor readings
            pm25 = random.randint(0, 1000)  # PM2.5 concentration in µg/m³
            co2 = random.randint(0, 5000)  # CO2 concentration in ppm
            tvoc = random.randint(0, 3)  # TVOC grade (0-3)
            temperature = round(random.uniform(-20, 65), 1)  # Temperature in Celsius
            humidity = round(random.uniform(0, 100), 1)  # Humidity in %
            ch2o = round(random.uniform(0, 6.250), 3)  # Formaldehyde concentration in mg/m³
            co = round(random.uniform(0, 500), 1)  # CO concentration in ppm
            o3 = round(random.uniform(0, 10), 2)  # Ozone concentration in ppm
            no2 = round(random.uniform(0.1, 10), 2)  # NO2 concentration in ppm

        return {
            "PM2.5 (µg/m³)": pm25,
            "CO2 (ppm)": co2,
            "TVOC (grade)": tvoc,
            "Temperature (°C)": temperature,
            "Humidity (%)": humidity,
            "CH2O (mg/m³)": ch2o,
            "CO (ppm)": co,
            "O3 (ppm)": o3,
            "NO2 (ppm)": no2
        }

# Example usage:
sensor_generator = SensorDataGenerator()

# Simulate normal conditions
print("Normal Sensor Data:")
for _ in range(5):
    print("ME4-SO2 Sensor Data:", sensor_generator.generate_me4_so2_data())
    print("ZE40-TVOC Sensor Data:", sensor_generator.generate_ze40_tvoc_data())
    print("ZPHS01B Sensor Data:", sensor_generator.generate_zphs01b_data())
    time.sleep(1)  # Simulate a 1-second delay between readings

# Simulate an emergency (e.g., fire or explosion)
sensor_generator.start_emergency()
for _ in range(5):
    print("ME4-SO2 Sensor Data (Emergency):", sensor_generator.generate_me4_so2_data())
    print("ZE40-TVOC Sensor Data (Emergency):", sensor_generator.generate_ze40_tvoc_data())
    print("ZPHS01B Sensor Data (Emergency):", sensor_generator.generate_zphs01b_data())
    time.sleep(1)  # Simulate a 1-second delay between readings

# Stop the emergency
sensor_generator.stop_emergency()

# Simulate normal conditions again
print("Normal Sensor Data (After Emergency):")
for _ in range(5):
    print("ME4-SO2 Sensor Data:", sensor_generator.generate_me4_so2_data())
    print("ZE40-TVOC Sensor Data:", sensor_generator.generate_ze40_tvoc_data())
    print("ZPHS01B Sensor Data:", sensor_generator.generate_zphs01b_data())
    time.sleep(1)  # Simulate a 1-second delay between readings
