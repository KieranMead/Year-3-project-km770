import matplotlib.pyplot as plt

# Provided data
age_range = ['18-25', '35-50', '50+']
yes_counts = [3, 2, 0]  # Number of "Yes" responses for each age range
no_counts = [11, 2, 1]  # Number of "No" responses for each age range

# Plotting the bar chart
bar_width = 0.35
index = range(len(age_range))

plt.bar(index, yes_counts, bar_width, label='Genuine', color='Green')
plt.bar(index, no_counts, bar_width, label='Not Genuine', color='Red', bottom=yes_counts)  # Stacking on top of 'Yes' counts

plt.xlabel('Age Range')
plt.ylabel('Count')
plt.title('Genuine/Not genuine Responses by Age Range')
plt.xticks(index, age_range)
plt.legend()

plt.show()


import matplotlib.pyplot as plt

# Provided data
age_range = ['18-25', '35-50', '50+']
yes_counts = [0, 0, 0]
no_counts = [0, 0, 0]

# Fill in counts based on the provided data
yes_counts[0] = 0  # No 'Yes' responses for age range '18-25'
yes_counts[1] = 0  # No 'Yes' responses for age range '35-50'
yes_counts[2] = 0  # No 'Yes' responses for age range '50+'

no_counts[0] = 15  # Total 'No' responses for age range '18-25'
no_counts[1] = 4   # Total 'No' responses for age range '35-50'
no_counts[2] = 1   # Total 'No' responses for age range '50+'

# Plotting the bar chart
bar_width = 0.35
index = range(len(age_range))
plt.bar(index, yes_counts, bar_width, label='Genuine', color='Green')
plt.bar(index, no_counts, bar_width, label='Not genuine', color='red')

plt.xlabel('Age Range')
plt.ylabel('Count')
plt.title('Genuine/Not genuine Responses by Age Range')
plt.xticks(index, age_range)
plt.legend()

plt.show()




# Data
responses = ["Yes", "Yes", "No", "No", "No", "No", "No", "Yes", "Yes", "No", "No", "No", "No", "No", "No", "No", "Yes", "Yes", "No", "No"]
ages = ["18-25", "18-25", "18-25", "35-50", "18-25", "18-25", "18-25", "18-25", "18-25", "18-25", "18-25", "18-25", "18-25", "18-25", "18-25", "18-25", "35-50", "50+", "35-50", "35-50"]

# Count responses for each age group
response_counts = {}
for age, response in zip(ages, responses):
    if age not in response_counts:
        response_counts[age] = {"Yes": 0, "No": 0}
    response_counts[age][response] += 1

# Extract age groups and their corresponding counts
age_groups = list(response_counts.keys())
yes_counts = [response_counts[age]["Yes"] for age in age_groups]
no_counts = [response_counts[age]["No"] for age in age_groups]

# Plot
bar_width = 0.35
index = range(len(age_groups))
plt.bar(index, yes_counts, bar_width, label='Genuine', color='green')
plt.bar(index, no_counts, bar_width, bottom=yes_counts, label='Not genuine', color='tab:red')

plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Genuine/Not genuine responses by age range')
plt.xticks(index, age_groups)
plt.legend()
plt.show()

import matplotlib.pyplot as plt

# Data
age_groups = ['18-25', '35-50', '50+']
yes_counts = [4, 2, 1]
no_counts = [10, 2, 0]

# Plot
bar_width = 0.35
index = range(len(age_groups))

plt.bar(index, yes_counts, bar_width, label='Genuine', color='green')
plt.bar(index, no_counts, bar_width, bottom=yes_counts, label='Not genuine', color='red')

plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Genuine/not genuine by age range')
plt.xticks(index, age_groups)
plt.legend()

plt.show()





