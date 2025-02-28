import random

class SensorDataGenerator:
    def __init__(self):
        pass

    def generate_me4_so2_data(self):
        """
        Generate random data for ME4-SO2 sensor.
        """
        so2_concentration = round(random.uniform(0, 20), 1)  # SO2 concentration in ppm
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
        tvoc_concentration = round(random.uniform(0, 5), 1)  # TVOC concentration in ppm
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

# Generate random data for ME4-SO2 sensor
me4_so2_data = sensor_generator.generate_me4_so2_data()
print("ME4-SO2 Sensor Data:", me4_so2_data)

# Generate random data for ZE40-TVOC sensor
ze40_tvoc_data = sensor_generator.generate_ze40_tvoc_data()
print("ZE40-TVOC Sensor Data:", ze40_tvoc_data)

# Generate random data for ZPHS01B sensor
zphs01b_data = sensor_generator.generate_zphs01b_data()
print("ZPHS01B Sensor Data:", zphs01b_data)
