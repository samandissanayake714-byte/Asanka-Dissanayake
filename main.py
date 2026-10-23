import time
import pandas as pd
from datetime import datetime

data_list = []

print("Aviator data collection started...")

try:
    while True:
        current_multiplier = "2.00x"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       
        print(f"[{timestamp}] Data collected: {current_multiplier}")
       
        data_list.append({"Time": timestamp, "Multiplier": current_multiplier})
        df = pd.DataFrame(data_list)
        df.to_csv("aviator_data.csv", index=False)
       
        time.sleep(10)

except KeyboardInterrupt:
    print("\nProgram stopped.") 
