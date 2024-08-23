import matplotlib.pyplot as plt

# Data
usage_data = {
    "5 hours +": {"Genuine": 0, "Not Genuine": 0},
    "4 hours": {"Genuine": 0, "Not Genuine": 0},
    "3 hours": {"Genuine": 0, "Not Genuine": 0},
    "2 hours": {"Genuine": 0, "Not Genuine": 0}
}

# Update the counts
responses = [
    ("3 hours", "Genuine"), ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"), ("3 hours", "Not Genuine"),
    ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"), ("4 hours", "Not Genuine"), ("5 hours +", "Genuine"),
    ("5 hours +", "Genuine"), ("4 hours", "Not Genuine"), ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"),
    ("4 hours", "Not Genuine"), ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"), ("4 hours", "Genuine"),
    ("4 hours", "Genuine"), ("5 hours +", "Not Genuine"), ("3 hours", "Genuine"), ("2 hours", "Not Genuine")
]

for time, response in responses:
    usage_data[time][response] += 1

# Prepare data for plotting
times = list(usage_data.keys())
genuine_counts = [usage_data[time]["Genuine"] for time in times]
not_genuine_counts = [usage_data[time]["Not Genuine"] for time in times]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(times, genuine_counts, label='Genuine', color='green')
plt.bar(times, not_genuine_counts, bottom=genuine_counts, label='Not Genuine', color='red')
plt.xlabel('Daily Internet Usage')
plt.ylabel('Count')
plt.title('Daily Internet Usage and Genuine Message Perception')
plt.legend()
plt.xticks(rotation=45)
plt.show()

import matplotlib.pyplot as plt

# Data
usage_data = {
   
    "5 hours +": {"Genuine": 0, "Not Genuine": 0},
    "4 hours": {"Genuine": 0, "Not Genuine": 0},
    "3 hours": {"Genuine": 0, "Not Genuine": 0},
    "2 hours": {"Genuine": 0, "Not Genuine": 0}
}

# Update the counts
responses = [
    ("3 hours", "Not Genuine"), ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"), ("3 hours", "Not Genuine"),
    ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"), ("4 hours", "Not Genuine"), ("5 hours +", "Not Genuine"),
    ("5 hours +", "Not Genuine"), ("4 hours", "Not Genuine"), ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"),
    ("4 hours", "Not Genuine"), ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"), ("4 hours", "Not Genuine"),
    ("4 hours", "Not Genuine"), ("5 hours +", "Not Genuine"), ("3 hours", "Not Genuine"), ("2 hours", "Not Genuine")
]

for time, response in responses:
    usage_data[time][response] += 1

# Prepare data for plotting
times = list(usage_data.keys())
genuine_counts = [usage_data[time]["Genuine"] for time in times]
not_genuine_counts = [usage_data[time]["Not Genuine"] for time in times]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(times, genuine_counts, label='Genuine', color='green')
plt.bar(times, not_genuine_counts, bottom=genuine_counts, label='Not Genuine', color='red')
plt.xlabel('Daily Internet Usage')
plt.ylabel('Count')
plt.title('Daily Internet Usage and Genuine Email Perception')
plt.legend()
plt.xticks(rotation=45)
plt.show()

import matplotlib.pyplot as plt

# Data
usage_data = {

    "5 hours +": {"Genuine": 0, "Not Genuine": 0},
    "4 hours": {"Genuine": 0, "Not Genuine": 0},
    "3 hours": {"Genuine": 0, "Not Genuine": 0},
    "2 hours": {"Genuine": 0, "Not Genuine": 0}
}

# Update the counts
responses = [
    ("3 hours", "Genuine"), ("5 hours +", "Genuine"), ("5 hours +", "Not Genuine"), ("3 hours", "Not Genuine"),
    ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"), ("4 hours", "Not Genuine"), ("5 hours +", "Genuine"),
    ("5 hours +", "Genuine"), ("4 hours", "Not Genuine"), ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"),
    ("4 hours", "Not Genuine"), ("5 hours +", "Not Genuine"), ("5 hours +", "Not Genuine"), ("4 hours", "Not Genuine"),
    ("4 hours", "Genuine"), ("5 hours +", "Genuine"), ("3 hours", "Not Genuine"), ("2 hours", "Not Genuine")
]

for time, response in responses:
    usage_data[time][response] += 1

# Prepare data for plotting
times = list(usage_data.keys())
genuine_counts = [usage_data[time]["Genuine"] for time in times]
not_genuine_counts = [usage_data[time]["Not Genuine"] for time in times]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(times, genuine_counts, label='Genuine', color='green')
plt.bar(times, not_genuine_counts, bottom=genuine_counts, label='Not Genuine', color='red')
plt.xlabel('Daily Internet Usage')
plt.ylabel('Count')
plt.title('Daily Internet Usage and Genuine Email Perception')
plt.legend()
plt.xticks(rotation=45)
plt.show()

import matplotlib.pyplot as plt

# Data
usage_data = {

    "5 hours +": {"Genuine": 0, "Not Genuine": 0},
    "4 hours": {"Genuine": 0, "Not Genuine": 0},
    "3 hours": {"Genuine": 0, "Not Genuine": 0},
    "2 hours": {"Genuine": 0, "Not Genuine": 0}
}

# Update the counts
responses = [
    ("3 hours", "Genuine"), ("5 hours +", "Genuine"), ("5 hours +", "Genuine"), ("3 hours", "Genuine"),
    ("5 hours +", "Genuine"), ("5 hours +", "Genuine"), ("4 hours", "Genuine"), ("5 hours +", "Genuine"),
    ("5 hours +", "Genuine"), ("4 hours", "Genuine"), ("5 hours +", "Genuine"), ("5 hours +", "Genuine"),
    ("4 hours", "Genuine"), ("5 hours +", "Genuine"), ("5 hours +", "Genuine"), ("4 hours", "Genuine"),
    ("4 hours", "Genuine"), ("5 hours +", "Not Genuine"), ("3 hours", "Genuine"), ("2 hours", "Genuine")
]

for time, response in responses:
    usage_data[time][response] += 1

# Prepare data for plotting
times = list(usage_data.keys())
genuine_counts = [usage_data[time]["Genuine"] for time in times]
not_genuine_counts = [usage_data[time]["Not Genuine"] for time in times]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(times, genuine_counts, label='Genuine', color='green')
plt.bar(times, not_genuine_counts, bottom=genuine_counts, label='Not Genuine', color='red')
plt.xlabel('Daily Internet Usage')
plt.ylabel('Count')
plt.title('Daily Internet Usage and Genuine Email Perception')
plt.legend()
plt.xticks(rotation=45)
plt.show()

