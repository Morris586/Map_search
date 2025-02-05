import folium 
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

location_name = input("Enter a location: ")

geolocator = Nominatim(user_agent='geoapi')
location = geolocator.geocode(location_name)

if location:

    latitude = location.latitude
    longitude = location.longitude
    clcoding = folium.Map(location= [latitude, longitude], zoom_start=15)

    marker= folium.Marker([latitude, longitude], popup=location_name)
    marker.add_to(clcoding)

    clcoding.save("map.html")
    print("Map saved as map.html. Open it in a browser to view.")
else:
    print("Location not found. Try again?")