# Given two lists - one with city names, and one with country names, print pairs with country-city. You can assume that the lists are of the same length.
# For example, given:
# cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
# countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']
# Expected output is:
# New York - USA
# Kyiv - Ukraine
# Paris-France
# …..
# And so on

cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']

for city in cities:
    continue
for i, county in enumerate(countries):
    print(f"{county} - {cities[i]}")