# nesting it is aboute puting the one into another

#Nesting 
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log_visited = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

#print(travel_log)
#print(travel_log_visited)

#Nesting a dictionary in side a list.

travel_log_visited = [
    {
        "country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total": 12
    },
    {
        "country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5
    },
]