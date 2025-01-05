
# Nesting a list in a dictionary
travel_log = {
    "france": ["paris", "lille", "dijon"],
    "germany": ["berlin", "hamburg", "stuttgart"],
}


#nesting a dictionary in a dictionary
travel_log = {
    "france": {"city1":"paris", "city2":"lille", "city3":"dijon",},
    "germany": {"cities_visited": ["berlin", "hamburg", "stuttgart"], "total_visits": 5}
}



#nestiing  dict in a list
travel_log =[ 
    {
     "country": "france", 
     "city": ["paris", "lille", "dijon"],
    },
    {
     "country": "germany", 
     "city": ["berlin", "hamburg", "stuttgart"],
     },
]
