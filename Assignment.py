import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Load log file
with open("calgary_access_log.txt") as file:
    lines = file.readlines()

# Define regex pattern for log lines
pattern = re.compile(r'(\S+) - - \[(.*?)\] "(.*?) (.*?) (.*?)" (\d{3}) (\d+|-)')

# Extract data
data = []
for line in lines:
    match = pattern.match(line)
    if match:
        host, datetime_str, method, resource, protocol, status, bytes_sent = match.groups()
        data.append({
            'host': host,
            'datetime': datetime.strptime(datetime_str, "%d/%b/%Y:%H:%M:%S %z"),
            'method': method,
            'resource': resource,
            'protocol': protocol,
            'status': int(status),
            'bytes_sent': int(bytes_sent) if bytes_sent != '-' else 0
        })

# Convert to DataFrame
df = pd.DataFrame(data)

#--> Top 10 Most Requested Resources <--#
print("\n#Top 10 Requested Resources:")
print(df['resource'].value_counts().head(10))

#--> Distribution of Status Codes <--#
print("\n#Distribution of Status Codes#")
print(df['status'].value_counts())

#--> Total Data Transferred (in KB or MB) <--#
print("\n#Total Data Transferred (in KB or MB)#")
print(df['bytes_sent'].sum() / 1024)  # in KB

#--> Error Requests (like 404) <--#
print("\n#Error Requests (like 404)#")
print(df[df['status'] >= 400]['resource'].value_counts())

sns.countplot(data=df, x='status')
plt.title("Status Code Distribution")
plt.show()