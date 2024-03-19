import pandas as pd
import re
from io import StringIO

# Load the data
with open('/mnt/data/enocean-data1.csv', 'rb') as f:
    content = f.read()
    decoded_content = content.decode('utf-8', errors='ignore')

# Initial column names
columns = ["Date Time", "Eurid", "eep/gp", "telemetry"]

# Read the data
df_new = pd.read_csv(StringIO(decoded_content), names=columns)

# 1. Replace spaces with commas in telemetry column
df_new['telemetry'] = df_new['telemetry'].str.replace(' ', ',')

# 2. Split telemetry into new columns
telemetry_columns = ['Temperature', 'Humidity', 'Illuminance', 'Acceleration Parameter', 'X-Acceleration', 'Y-Acceleration', 'Z-Acceleration', 'Open/Close Sensor', 'Signal Strength']
telemetry_df = df_new['telemetry'].str.split(',', expand=True).iloc[:, :-1]
telemetry_df.columns = telemetry_columns

# Extract only numeric values
for col in telemetry_columns:
    telemetry_df[col] = telemetry_df[col].str.extract(r'(-?\d+\.?\d*)').astype(float)

# 3. Extract only necessary columns
df_new = pd.concat([df_new, telemetry_df[['Temperature', 'Humidity', 'Illuminance', 'Signal Strength']]], axis=1)
df_new.drop(columns=['telemetry', 'Eurid', 'eep/gp'], inplace=True)

# 4. Compute hourly averages
df_new['Date Time'] = pd.to_datetime(df_new['Date Time'])
df_new.set_index('Date Time', inplace=True)
hourly_avg_new = df_new.resample('H').mean()

# 5. Compute averages for all dates by hour
hourly_avg_new['Hour'] = hourly_avg_new.index.hour
summary_new = hourly_avg_new.groupby('Hour').mean()

# 6. Save the result to CSV
summary_new.to_csv('/mnt/data/summary-8.csv')

