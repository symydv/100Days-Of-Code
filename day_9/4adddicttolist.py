
travel_log =[ 
    {
     "country": "france",
     "visits": 12, 
     "city": ["paris", "lille", "dijon"],
    },
    {
     "country": "germany", 
     "visits": 5,
     "city": ["berlin", "hamburg", "stuttgart"],
     },
]

def add_new_country(country_visited, times_visits, city_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visits
    new_country["city"] = city_visited
    travel_log.append(new_country)
    print(travel_log)



add_new_country("russia", 2, ["moscow", "alaska"])