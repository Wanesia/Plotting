import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Load the data from the CSV file
data = pd.read_csv('data/speed_data_data.csv')

# Filter the data to include only rows with important data
filtered_data = data.dropna(subset=['attr', 'sinc', 'intel', 'fun', 'amb', 'shar', 'gender', 'age'], how='any')

# Count occurrences
age_counts = filtered_data['age'].value_counts().sort_index()
gender_counts = filtered_data['gender'].value_counts().sort_index()
gender_counts.index = ['Women' if x == 0 else 'Men' for x in gender_counts.index]

gender_counts = gender_counts.reindex(['Women', 'Men'])

# Calculate the average ratings for each attribute
avg_values_women = filtered_data[filtered_data['gender'] == 0][['attr', 'sinc', 'intel', 'fun', 'amb', 'shar']].mean()
avg_values_men = filtered_data[filtered_data['gender'] == 1][['attr', 'sinc', 'intel', 'fun', 'amb', 'shar']].mean()

# Mapping to display full names of attributes
attribute_mapping = {
    'attr': 'Attractiveness',
    'sinc': 'Sincerity',
    'intel': 'Intelligence',
    'fun': 'Fun',
    'amb': 'Ambition',
    'shar': 'Shared Interests'
}

# Extract attribute names and their full versions
attributes = avg_values_women.index.tolist()
full_attributes = [attribute_mapping[attr] for attr in attributes]

# Average values for women and men
values_women = avg_values_women.values.tolist()
values_men = avg_values_men.values.tolist()

bar_width = 0.35

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

# Age distribution as line graph
ax1 = plt.subplot(gs[0, 0])
ax1.plot(age_counts.index, age_counts.values, color='lightgreen', marker='o')
ax1.set_xlabel('Age')
ax1.set_ylabel('Count')
ax1.set_title('Distribution of Age')

# Gender distribution as a pie chart
ax2 = plt.subplot(gs[0, 1])
ax2.pie(gender_counts, labels=gender_counts.index, colors=['pink', '#6666ff'], autopct='%1.1f%%', startangle=140)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.set_title('Distribution of Gender')

# Average attributes
ax3 = plt.subplot(gs[1, :])
ax3.bar([x - bar_width/2 for x in range(len(attributes))], values_women, width=bar_width, label='Women', color='pink')
ax3.bar([x + bar_width/2 for x in range(len(attributes))], values_men, width=bar_width, label='Men', color='#6666ff')
ax3.set_xlabel('Attribute')
ax3.set_ylabel('Average Rating')
ax3.set_title('Average Attributes Ratings by Gender')
ax3.set_xticks(range(len(full_attributes)))
ax3.set_xticklabels(full_attributes)
ax3.legend()

plt.tight_layout()
plt.show()
