import random
import time

class SensorDataGenerator:
    def __init__(self):
        self.emergency = False  # وضعیت اضطراری
        self.emergency_start_time = None  

    def start_emergency(self):
        """شروع حالت اضطراری (مثلاً آتش‌سوزی)"""
        self.emergency = True
        self.emergency_start_time = time.time()
        print("🚨 حالت اضطراری فعال شد!")

    def stop_emergency(self):
        """پایان حالت اضطراری"""
        self.emergency = False
        print("✅ حالت اضطراری متوقف شد!")

    def generate_me4_so2_data(self):
        """تولید داده‌های سنسور ME4-SO2"""
        so2 = round(random.uniform(10, 200), 1) if self.emergency else round(random.uniform(0, 20), 1)  # SO2 در ppm
        temp = round(random.uniform(-20, 50), 1)  # دما °C
        hum = round(random.uniform(15, 90), 1)  # رطوبت %

        return {
            "so2": so2,  # غلظت SO2 (ppm)
            "temp": temp,  # دما (°C)
            "hum": hum  # رطوبت (%)
        }

    def generate_ze40_tvoc_data(self):
        """تولید داده‌های سنسور ZE40-TVOC"""
        tvoc = round(random.uniform(3, 10), 1) if self.emergency else round(random.uniform(0, 5), 1)  # TVOC در ppm
        temp = round(random.uniform(0, 50), 1)  
        hum = round(random.uniform(15, 90), 1)

        return {
            "tvoc": tvoc,  # غلظت TVOC (ppm)
            "temp": temp,  # دما (°C)
            "hum": hum  # رطوبت (%)
        }

    def generate_zphs01b_data(self):
        """تولید داده‌های سنسور ZPHS01B"""
        if self.emergency:
            pm25 = random.randint(500, 1000)  # ذرات معلق PM2.5 (µg/m³)
            co2 = random.randint(2000, 5000)  # غلظت CO2 (ppm)
            tvoc = random.randint(2, 3)  # کیفیت TVOC (درجه)
            temp = round(random.uniform(30, 65), 1)  
            hum = round(random.uniform(50, 100), 1)
            ch2o = round(random.uniform(1, 6.250), 3)  # فرمالدهید (mg/m³)
            co = round(random.uniform(100, 500), 1)  # مونوکسیدکربن (ppm)
            o3 = round(random.uniform(5, 10), 2)  # اوزون (ppm)
            no2 = round(random.uniform(5, 10), 2)  # دی‌اکسید نیتروژن (ppm)
        else:
            pm25 = random.randint(0, 1000)
            co2 = random.randint(0, 5000)
            tvoc = random.randint(0, 3)
            temp = round(random.uniform(-20, 65), 1)
            hum = round(random.uniform(0, 100), 1)
            ch2o = round(random.uniform(0, 6.250), 3)
            co = round(random.uniform(0, 500), 1)
            o3 = round(random.uniform(0, 10), 2)
            no2 = round(random.uniform(0.1, 10), 2)

        return {
            "pm25": pm25,  # PM2.5 (µg/m³)
            "co2": co2,  # CO2 (ppm)
            "tvoc": tvoc,  # TVOC (درجه)
            "temp": temp,  # دما (°C)
            "hum": hum,  # رطوبت (%)
            "ch2o": ch2o,  # فرمالدهید (mg/m³)
            "co": co,  # مونوکسیدکربن (ppm)
            "o3": o3,  # اوزون (ppm)
            "no2": no2  # دی‌اکسید نیتروژن (ppm)
        }

# استفاده از کلاس
sensor = SensorDataGenerator()

# حالت عادی
print("📊 داده‌های سنسور (عادی):")
for _ in range(5):
    print(sensor.generate_me4_so2_data())
    print(sensor.generate_ze40_tvoc_data())
    print(sensor.generate_zphs01b_data())
    time.sleep(1)

# حالت اضطراری
sensor.start_emergency()
for _ in range(5):
    print("🚨", sensor.generate_me4_so2_data())
    print("🚨", sensor.generate_ze40_tvoc_data())
    print("🚨", sensor.generate_zphs01b_data())
    time.sleep(1)

# بازگشت به حالت عادی
sensor.stop_emergency()
print("📊 داده‌های سنسور (پس از اضطراری):")
for _ in range(5):
    print(sensor.generate_me4_so2_data())
    print(sensor.generate_ze40_tvoc_data())
    print(sensor.generate_zphs01b_data())
    time.sleep(1)
