travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities":["paris", "lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Humburg", "Stuttgart"]
},
]
#DO NOT change the code above.

#TODO: write the function that will allow new country
# to be added to the trave_log.

def add_new_country(country_visited, time_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited

    travel_log.append(new_country)

#DO NOT chnage the code below.
add_new_country("Russia", 2, ["Mosco", "Saint Petersbu"])
print(travel_log)