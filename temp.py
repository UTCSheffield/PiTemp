from envirophat import weather

import time
while True:
    print(weather.temperature())
    time.sleep(15)
