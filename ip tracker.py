import requests
import folium

res=requests.get('https://ipinfo.io/') #getting requests from the url
data=res.json() #converting the res file into json
#print(data) # shows what this data will print
location=data['loc'].split(',')
lat=float(location[0])
log=float(location[1])
#the location format is loc[ latitude, longtitude]. So we created 2 separated
#variables to capture thoses values

# folium is a base map framework which can create coordinates and show datas related to the locations

#featureGroup
fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('Brazil-states.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[lat,log],popup="this is my location"))

map=folium.Map(location=[lat,log],zoom_start=7)

map.add_child(fg)
map.save("location.html")