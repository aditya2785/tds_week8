import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
sns.set_context("talk")

np.random.seed(42)

data = {
    "Website Visits": np.random.randint(50, 200, 100),
    "App Usage Time": np.random.randint(20, 120, 100),
    "Email Click Rate": np.random.uniform(1, 10, 100),
    "Purchase Frequency": np.random.randint(1, 15, 100),
    "Customer Support Calls": np.random.randint(0, 5, 100)
}

df = pd.DataFrame(data)
corr_matrix = df.corr()

# CRITICAL SETTINGS FOR 512x512
plt.figure(figsize=(8, 8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    square=True
)

plt.title("Customer Engagement Correlation Matrix", fontsize=16, fontweight="bold")

# IMPORTANT: No bbox_inches
plt.savefig("chart.png", dpi=64)
plt.close()
