import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Gender": ["Female", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male",
               "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female"],
    "Genuine": ["Genuine", "Not Genuine", "Not Genuine", "Not Genuine", "Not Genuine", "Not Genuine", "Not Genuine",
                "Genuine", "Genuine", "Not Genuine", "Not Genuine", "Not Genuine", "Not Genuine", "Not Genuine",
                "Not Genuine", "Genuine", "Genuine", "Not Genuine", "Genuine", "Not Genuine"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Count occurrences of each combination
counts = df.groupby(["Gender", "Genuine"]).size().unstack()

# Plot
colors = {"Genuine": "green", "Not Genuine": "red"}
ax = counts.plot(kind="bar", stacked=True, color=colors.values())
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.title("Genuine Messages by Gender", fontsize=14)
plt.legend(title="Genuine?", labels=colors.keys(), fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

import matplotlib.pyplot as plt

# Data
gender = ['Female', 'Male']
genuine_responses = [0, 0]  # Count of 'Genuine' responses for each gender
not_genuine_responses = [5, 15]  # Count of 'Not Genuine' responses for each gender

# Plot
bar_width = 0.35
index = range(len(gender))

plt.bar(index, genuine_responses, bar_width, label='Genuine', color='green')
plt.bar(index, not_genuine_responses, bar_width, label='Not Genuine', color='red', bottom=genuine_responses)

# Title and labels
plt.title('Responses to "Do you think the above Email is genuine?" by Gender')
plt.xlabel('Gender')
plt.ylabel('Count of responses')
plt.xticks(index, gender)

# Legend
plt.legend()

# Show plot
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the provided data
data = {
    "Gender": ["Female", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male",
               "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female"],
    "Response": ["Genuine", "Genuine", "Not Genuine", "Not Genuine", "Not Genuine", "Not Genuine", 
                 "Not Genuine", "Genuine", "Genuine", "Not Genuine", "Not Genuine", "Not Genuine", 
                 "Not Genuine", "Not Genuine", "Not Genuine", "Not Genuine", "Genuine", "Genuine", 
                 "Not Genuine", "Not Genuine"]
}

df = pd.DataFrame(data)

# Count occurrences of each combination of gender and response
counts = df.groupby(['Gender', 'Response']).size().unstack()

# Plot stacked bar chart
counts.plot(kind='bar', stacked=True, color=['green', 'red'])
plt.title('Responses by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.yticks(range(0, 15, 2))  # Set y-axis range from 0 to 14, increment by 2
plt.legend(title='Response')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Gender": ["Female", "Male", "Male", "Female", "Male", "Male", "Female", "Male", "Male", "Male",
               "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female"],
    "Genuine_Email": ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
                      "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Map 'Yes' to Genuine and 'No' to Not Genuine
df['Genuine_Email'] = df['Genuine_Email'].map({'Yes': 'Genuine', 'No': 'Not Genuine'})

# Group by Gender and Genuine_Email, and count occurrences
grouped = df.groupby(['Gender', 'Genuine_Email']).size().unstack(fill_value=0)

# Plot stacked bar chart
colors = {'Genuine': 'green', 'Not Genuine': 'red'}
grouped.plot(kind='bar', stacked=True, color=[colors[col] for col in grouped.columns])

# Add labels and title
plt.title('Stacked Bar Chart of Gender vs Genuine Email')
plt.xlabel('Gender')
plt.ylabel('Count')

# Show plot
plt.show()
