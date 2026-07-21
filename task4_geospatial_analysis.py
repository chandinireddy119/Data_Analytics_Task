import pandas as pd
import folium

print("=" * 60)
print("GEOSPATIAL DATA ANALYSIS")
print("=" * 60)

# Read dataset
df = pd.read_csv("geospatial_sales.csv")

print("\nOriginal Dataset\n")
print(df)

print("\nDataset Information\n")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nTotal Sales by City")
print(df.groupby("City")["Sales"].sum())

# Create map centered on India
map_india = folium.Map(
    location=[22.9734, 78.6569],
    zoom_start=5
)

# Add markers
for index, row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['City']}<br>Sales: ₹{row['Sales']}",
        tooltip=row["City"]
    ).add_to(map_india)

# Save map
map_india.save("geospatial_analysis_map.html")

print("\nInteractive map created successfully.")
print("Output File: geospatial_analysis_map.html")
print("\nTask 4 Completed Successfully!")