travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}


final_travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
    "Italy": ["Rome", "Venice", "Florence"]
}

travel_log["Italy"]= ["Rome", "Venice", "Florence"]

print(travel_log == final_travel_log)

for key in travel_log:
    print(key)



print(travel_log)

for k,v in travel_log.items():
    print(f"{k}: {v}")


print(travel_log["France"])
print(travel_log["France"][1]) # accessing the second item in the list of values for key "France"

nested_list=["A","B", ["C","D"]]


print(nested_list)
print(nested_list[2][0]) # to access nested list item


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    }
}


print(travel_log)

print(travel_log["France"]["cities_visited"])      # accessing the list of cities visited in France
print(travel_log["France"]["total_visits"])
