import csv
import unicodecsv
import json
import requests
import pandas as pd

# Dada la información de un restaurante, obtener datos de Yelp.
def obtenerInformaciónRestaurante(term, latitude, longitude, pais):
    query = {'term':term, 'latitude':latitude, 'longitude':longitude}
    my_headers = {'Authorization' : 'Bearer .................................'}
    response = requests.get('https://api.yelp.com/v3/businesses/search', headers=my_headers, params=query)
    path = r'datasets/' + pais + '_yelp.json' 
    with open(path, 'w') as outfile:
        outfile.write(response.text)
    return response

# Dado un país, obtener sus nombres de restaurantes, latitudes y longitudes.
def procesarPais(p): 
    rows = []
    path = r'datasets/' + p + '.csv' 
    pais = open(path, encoding='Latin1')
    csvreader = csv.reader(pais)
    header = next(csvreader)
    headers = header[0].split(";")
    
    term = []
    lat = []
    lon = []
    rows = []

    for row in csvreader:
        restaurante = row[0].split(";")
        if(len(restaurante) > 7):
            if(restaurante[0] != "" and restaurante[5] != "" and restaurante[6] != ""):
                term.append(restaurante[0])
                lat.append(restaurante[5])
                lon.append(restaurante[6])
        
    pais.close()
    return (term, lat, lon, p)

def generarCsvPais(p):
    headers = ["name", "price", "review_count", "rating", "delivery", "pickup", "address", "city", "zip_code", "country", "state"]
    term, latitud, longitud, pais = procesarPais(p)
    stringCsv = []
    for i in range(len(term)):
        restauranteProcesado = obtenerInformaciónRestaurante(term[i], latitud[i], longitud[i], pais)
        print("Country: ", p, ". Index executed (i): ", i)
        if("businesses" in restauranteProcesado.json()):
            if(len(restauranteProcesado.json()["businesses"]) > 0):
                
                    price = ""
                    name = ""
                    reviewCount = 0
                    rating = 0.0
                    delivery = 0
                    pickup = 0
                    city = ""
                    zipCode = ""
                    country = ""
                    state = ""
                    
                    if("transactions" in restauranteProcesado.json()["businesses"][0]):
                        if("delivery" in restauranteProcesado.json()["businesses"][0]["transactions"]):
                            delivery = 1
                            
                        if("pickup" in restauranteProcesado.json()["businesses"][0]["transactions"]):
                            pickup = 1
                            
                    if("location" in restauranteProcesado.json()["businesses"][0]):                           
                        if("city" in restauranteProcesado.json()["businesses"][0]["location"]):
                            city = restauranteProcesado.json()["businesses"][0]["location"]["city"]
                            
                        if("zip_code" in restauranteProcesado.json()["businesses"][0]["location"]):
                            zipCode = restauranteProcesado.json()["businesses"][0]["location"]["zip_code"]
                            
                        if("country" in restauranteProcesado.json()["businesses"][0]["location"]):
                            country = restauranteProcesado.json()["businesses"][0]["location"]["country"]
                            
                        if("state" in restauranteProcesado.json()["businesses"][0]["location"]):
                            state = restauranteProcesado.json()["businesses"][0]["location"]["state"]
                            
                    if("price" in restauranteProcesado.json()["businesses"][0]):
                        price = restauranteProcesado.json()["businesses"][0]["price"]
                    
                    if("name" in restauranteProcesado.json()["businesses"][0]):
                        name = restauranteProcesado.json()["businesses"][0]["name"]
                    
                    if("review_count" in restauranteProcesado.json()["businesses"][0]):
                        reviewCount = restauranteProcesado.json()["businesses"][0]["review_count"]
                        
                    if("rating" in restauranteProcesado.json()["businesses"][0]):
                        rating = restauranteProcesado.json()["businesses"][0]["rating"]
                        
                    separator = ";"
                    string = name
                    string += separator
                    string += price
                    string += separator
                    string += str(reviewCount)
                    string += separator
                    string += str(rating)
                    string += separator
                    string += str(delivery)
                    string += separator
                    string += str(pickup)
                    string += separator
                    string += city
                    string += separator
                    string += zipCode
                    string += separator
                    string += country
                    string += separator
                    string += state
                    string += separator
                    
                    stringCsv.append(string)
    print(stringCsv)
    return stringCsv

paises = ["Alemania", 
          "Austria", 
          "Belgica", 
          "China", 
          "Corea", 
          "Dinamarca", 
          "Estados_Unidos", 
          "Francia", 
          "Grecia", 
          "Hong_Kong", 
          "Irlanda",
          "Italia",
          "Japon",
          "Paises_Bajos",
          "Portugal",
          "Reino_Unido",
          "Rusia",
          "Singapur",
          "Spain",
          "Suecia",
          "Suiza",
          "Tailandia"]

headers = "name;price;review_count;rating;delivery;pickup;city;zip_code;country:state"
data = []
count = 0

for p in paises:
    count += 1
    print("Counter: ", count)
    data += generarCsvPais(p)
    
with open(r'datasets/countries_yelp.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

def crearFicheroJsonDesdeResponse(response):
    with open(r'datasets/json_data.json', 'w') as outfile:
        outfile.write(response)

def crearFicheroJsonDesdeFicheroCsv(data):
    data = json.load(open(r'datasets/test.json'))
    df = pd.DataFrame(data["businesses"])
    df.to_csv (r'datasets/testparser.csv', index = None)        

data = json.load(open(r'datasets/test.json'))
crearFicheroJsonDesdeFicheroCsv(data)    