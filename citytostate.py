city_to_state_dict = {"East Rancho Dominguez": "California",
                      "Clinton": "Mississippi",
                      "Nanuet": "New York",
                      "Sand Springs": "Oklahoma",
                      "Middle River": "Maryland",
                      "Carbondale": "Illinois",
                      "Boise": "Idaho",
                      "Las Vegas": "Nevada",
                      "Denver": "Colorado",
                      "Hagerstown": "Maryland",
                      "Venice": "Florida",
                      "Moreno Valley": "California",
                      "Mamaroneck": "New York",
                      "Bartow": "Florida",
                      "Bensonhurst": "New York"}

city = raw_input("Enter your City ")
state = raw_input("Enter your State ")
for key, value in city_to_state_dict.iteritems():
  if value==city or key==state:
    print key, value