# -----------------------------------------
# Task 4: Data Visualization (Matplotlib)
# -----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# STEP 1: LOAD DATA
# -------------------------------

file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

print("Data loaded successfully!")

# -------------------------------
# CREATE OUTPUT FOLDER
# -------------------------------

os.makedirs("outputs", exist_ok=True)


# -------------------------------
# CHART 1: TOP 10 STORIES BY SCORE
# -------------------------------

# Sort and get top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles
top10["title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure(figsize=(8, 6))
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

# Save before show
plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# -------------------------------
# CHART 2: STORIES PER CATEGORY
# -------------------------------

category_counts = df["category"].value_counts()

plt.figure(figsize=(6, 5))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()


# -------------------------------
# CHART 3: SCATTER (SCORE vs COMMENTS)
# -------------------------------

# Separate popular & non-popular
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(6, 5))

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()


# -------------------------------
# BONUS: DASHBOARD
# -------------------------------

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1
axs[0].barh(top10["title"], top10["score"])
axs[0].set_title("Top Stories")

# Chart 2
axs[1].bar(category_counts.index, category_counts.values)
axs[1].set_title("Categories")

# Chart 3
axs[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axs[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axs[2].set_title("Score vs Comments")
axs[2].legend()

# Dashboard title
plt.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.close()

print("✅ All charts saved in 'outputs/' folder")