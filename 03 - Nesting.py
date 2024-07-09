#Nesting the List inside the dictionary
travel_log = {
    "Jhapa" : ["Damak", "Birtamode","Surunga","Kakarbhitta"],
    "Kathmandu" : ["Bhaktapur","Lalitpur","Kathmandu"]
}
#Nesting list inside a dictionary and dictionaryinside a dictionary
travel_detail = {
    "Jhapa" :{"Places Visited" : ["Damak", "Birtamode","Surunga","Kakarbhitta"], "Number of times": 20},
    "Kathmandu" :{"Places visited": ["Bhaktapur","Lalitpur","Kathmandu"], "specific temples": ["Pashupatinath", "Swyambunath","Krishna Temple"]}
}
#Nesting a dictionary inside a list
travel = [
    {"District": "Jhapa", "Places Visited" : ["Damak", "Birtamode","Surunga","Kakarbhitta"], "Number of times": 20},
    {"District" : "Kathmandu", "Places visited": ["Bhaktapur","Lalitpur","Kathmandu"], "specific temples": ["Pashupatinath", "Swyambunath","Krishna Temple"] }
]