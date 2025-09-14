import folium

# Preloaded coordinates for Caffenio branches in Ciudad Obregón
caffenio_locations = [
    ("Caffenio – Central Obr", 27.48273, -109.93074),
    ("Caffenio – Industrial", 27.48511, -109.91926),
    ("Caffenio – Mayo", 27.49307, -109.93922),
    ("Caffenio – Santa Anita", 27.49150, -109.94690),
    ("Caffenio – Guerrero", 27.48774, -109.93005),
    ("Caffenio – Norte", 27.50990, -109.93142),
    ("Caffenio – Fairplay", 27.47294, -109.91833),
    ("Caffenio – Constitución", 27.45921, -109.91545),
    ("Caffenio – Miguel Alemán", 27.48200, -109.93090),
    ("Caffenio – Nainarí", 27.48670, -109.94020),
    ("Caffenio – Bella Vista", 27.49430, -109.93380),
    ("Caffenio – Calle 200", 27.47490, -109.93320),
    ("Caffenio – Plaza 5", 27.45450, -109.91010)
]

# Center map roughly on Ciudad Obregón
m = folium.Map(location=[27.486, -109.939], zoom_start=13)

# Add markers for each location
for name, lat, lon in caffenio_locations:
    folium.Marker(
        location=[lat, lon],
        popup=name,
        icon=folium.Icon(color='brown', icon='coffee', prefix='fa')
    ).add_to(m)

# Save map
m.save("ciudad_obregon_caffenio_map.html")
print("Map created: ciudad_obregon_caffenio_map.html")
