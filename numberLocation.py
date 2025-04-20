import phonenumbers


import folium

from myNumber import number

from phonenumbers import geocoder

key = 'f642070a3be04ee9a7a9c164bc09fa17'


samNumber = phonenumbers.parse(number)

yourLocation =geocoder.description_for_number(samNumber , "en")

print(yourLocation)

##get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))


from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

result = geocoder.geocode(query)
print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print("Latitude is : ", lat)
print("Longitude is : ",lng)

myMap = folium.Map(location=[lat,lng],zoom_start = 9)

folium.Marker([lat,lng],popup = yourLocation).add_to(myMap)

##save map in html file

myMap.save("MapLocation.html")

