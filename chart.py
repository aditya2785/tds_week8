import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Force seaborn theme
sns.set_theme(style="white")

np.random.seed(42)

data = {
    "Website Visits": np.random.randint(50, 200, 100),
    "App Usage Time": np.random.randint(20, 120, 100),
    "Email Click Rate": np.random.uniform(1, 10, 100),
    "Purchase Frequency": np.random.randint(1, 15, 100),
    "Customer Support Calls": np.random.randint(0, 5, 100)
}

df = pd.DataFrame(data)
corr = df.corr()

plt.figure(figsize=(8, 8))

# EXPLICIT seaborn heatmap
ax = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=1,
    square=True,
    cbar=True
)

plt.title("Customer Engagement Correlation Matrix", fontsize=16)

# EXACT 512x512 export
plt.savefig("chart.png", dpi=64)
plt.close()
