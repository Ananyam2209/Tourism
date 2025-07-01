import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
try:
    hotels_df = pd.read_csv(r"C:\Users\Pavilion\OneDrive\Dokumen\tourism project\vast_hotels_dataset.csv")
    weather_df = pd.read_csv(r"C:\Users\Pavilion\OneDrive\Dokumen\tourism project\vast_weather_dataset.csv")
except FileNotFoundError as e:
    print("❌ File not found:", e)
    exit()

# Clean data
hotels_df["rating"] = pd.to_numeric(hotels_df["rating"], errors="coerce")
hotels_df.dropna(subset=["city", "price_per_night", "rating"], inplace=True)
weather_df.dropna(subset=["city", "month", "avg_temp"], inplace=True)

# Seaborn styling
sns.set(style="whitegrid")

# 1. Average Hotel Price per City
avg_price = hotels_df.groupby("city")["price_per_night"].mean().sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_price.values, y=avg_price.index, palette="viridis")
plt.title("Average Hotel Price per City")
plt.xlabel("Avg. Price (INR)")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# 2. Hotel Price vs Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(data=hotels_df, x="rating", y="price_per_night", hue="city", alpha=0.6)
plt.title("Hotel Price vs Rating by City")
plt.xlabel("Rating")
plt.ylabel("Price per Night (INR)")
plt.tight_layout()
plt.show()

# 3. Average Monthly Temperature (Goa)
goa_weather = weather_df[weather_df["city"].str.lower() == "goa"].copy()

# Sort by month (optional fix if month names are out of order)
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
if goa_weather["month"].isin(month_order).all():
    goa_weather["month"] = pd.Categorical(goa_weather["month"], categories=month_order, ordered=True)
    goa_weather.sort_values("month", inplace=True)

plt.figure(figsize=(10, 6))
sns.lineplot(data=goa_weather, x="month", y="avg_temp", marker="o", color="tomato")
plt.title("Average Monthly Temperature in Goa")
plt.xlabel("Month")
plt.ylabel("Avg Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Donut Chart: Hotel Distribution by City
city_counts = hotels_df["city"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(city_counts, labels=city_counts.index, autopct="%1.1f%%", startangle=140, wedgeprops=dict(width=0.3))
plt.title("Hotel Distribution by City")
plt.axis("equal")
plt.show()

# 5. Pie Chart: Rating Distribution
rating_counts = hotels_df["rating"].round(1).value_counts().sort_index()
plt.figure(figsize=(6, 6))
plt.pie(rating_counts, labels=rating_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Hotel Ratings Distribution")
plt.axis("equal")
plt.show()

# 6. Highest Hotel Rating per City
max_ratings = hotels_df.groupby("city")["rating"].max().sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(x=max_ratings.values, y=max_ratings.index, palette="coolwarm")
plt.title("Highest Hotel Rating per City")
plt.xlabel("Highest Rating")
plt.ylabel("City")
plt.xlim(0, 5)
plt.tight_layout()
plt.show()

# 7. Table Output
print("\n📊 Top 10 Hotels:")
print(hotels_df[['name', 'city', 'rating', 'price_per_night', 'amenities']].head(10))

