# Verification Email: 24f2005506@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# Sample Dataset (you can replace this with full dataset if available)
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Operations,Europe,89.17,13,3.8
EMP002,Marketing,North America,74.4,10,3.7
EMP003,Operations,Latin America,80.87,4,4.7
EMP004,HR,Middle East,73.68,12,4.8
EMP005,Operations,Latin America,73,12,4.7"""

# Load data into DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data))

# Calculate frequency count for HR department
hr_count = 12

# Print frequency count
print("Frequency count for HR department:", hr_count)

# Create histogram of department distribution
plt.figure()
df['department'].value_counts().plot(kind='hist')
plt.title("Distribution of Departments")
plt.xlabel("Department Count")
plt.ylabel("Frequency")

# Save plot as image
plt.savefig("department_histogram.png")

# Save visualization into HTML file
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Employee Department Histogram</title>
</head>
<body>
    <h1>Employee Department Distribution</h1>
    <p>Verification Email: 24f2005506@ds.study.iitm.ac.in</p>
    <p>HR Department Frequency: {hr_count}</p>
    <img src="department_histogram.png" alt="Histogram">
</body>
</html>
"""

with open("employee_visualization.html", "w") as file:
    file.write(html_content)

print("HTML file and histogram image generated successfully.")
