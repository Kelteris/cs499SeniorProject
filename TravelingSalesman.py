import csv
from random import shuffle

class Chromosome(object):
    #will later take in the parameter that is a city from google maps
    def __init__(self):
        pass

    def mutations(self):
        pass

    def fitness(self):
        pass

class Tsp(object):
    # will hold lots of chromosomes which will represent an order of citys
    def __init__(self):
        pass

class City(object):

    def __init__(self, name, latitude, longitude, miles_to_la,
                 miles_to_lv, miles_to_nyc, miles_to_slc,
                 miles_to_miami, miles_to_dallas, id_number):
        self.name = name
        self.latitude = latitude
        self.longitute  = longitude
        self.miles_to_la = miles_to_la
        self.miles_to_lv = miles_to_lv
        self.miles_to_nyc = miles_to_nyc
        self.miles_to_slc = miles_to_slc
        self.miles_to_miami = miles_to_miami
        self.miles_to_dallas = miles_to_dallas
        self.id_number = id_number

    def make_dictionary_of_distances(self):

        distances = {'miles_to_la' : self.miles_to_la,
                     'miles_to_lv': self.miles_to_lv,
                     'miles_to_nyc': self.miles_to_nyc,
                     'miles_to_slc': self.miles_to_slc,
                     'miles_to_miami': self.miles_to_miami,
                     'miles_to_dallas': self.miles_to_dallas}

        return distances

la = City("la", 34.02, 118.4, 0, 228, 2481, 579, 2339, 1240, 1)
lv = City("lv", 36.23, 115.3, 228, 0, 2233, 362, 2181, 1071, 2)
nyc = City("nyc", 40.66, 73.94, 2451, 2233, 0, 1972, 1089, 1373, 3)
slc = City("slc", 40.78, 111.9, 579, 362, 1972, 0, 1089, 1000, 4)
miami = City("miami", 25.78, 80.21, 2339, 2181, 1089, 2089, 0, 1111, 5)
dallas = City("dallas", 32.79, 96.77, 1240, 1071, 1373, 1000, 1111, 0, 6)


#milwaukee = City("Milwaukee", 43.06, 87.97)
#lincoln = City("Lincoln", 40.81, 96.68)
#boston = City("Boston", 42.33, 71.02)
#with open('cd.csv') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        print(row['start_city'], row['end_city'], row['distance'])

cities = [la, lv, nyc, slc, miami, dallas]
shuffle(cities)
print (cities[0].name, cities[1].name, cities[2].name, cities[3].name, cities[4].name, cities[5].name)
total_miles = 0
for i in range(len(cities)):
    print(i)
    print(cities[i].name)
    dictionary = cities[i].make_dictionary_of_distances()
    print (dictionary)
    if (i < (len(cities) - 1)):
        next_city = "miles_to_" + cities[i + 1].name
        total_miles += dictionary[next_city]
        print (next_city)
        print (total_miles)
        #if (cities[i].miles)
        #print (cities[i].miles_to_ + cities[i + 1].name)
    else:
        next_city = "miles_to_" + cities[0].name
        total_miles += dictionary[next_city]
        print(next_city)
        print(total_miles)