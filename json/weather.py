# import required modules 
import requests, json 

# Enter your API key here 
#api_key = "Your_API_Key"
api_key = "bd90de086e09bf23d749d5f2243c3b06"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"


# Provide city name 
city_name = input("Enter city name : ") 
  
# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
data = response.json() 

# Let's take a look at what our data looks like:
print(data["main"])