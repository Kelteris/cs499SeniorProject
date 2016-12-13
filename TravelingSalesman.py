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

class generation(object):
    # will hold lots of chromosomes which will represent an order of citys
    def __init__(self):
        pass

class City(object):

    def __init__(self, name, latitude, longitude, miles_to_la,
                 miles_to_lv, miles_to_nyc, miles_to_slc,
                 miles_to_miami, miles_to_dallas, miles_to_milwaukee,
                 miles_to_boston, miles_to_lincoln, miles_to_seattle,
                 miles_to_portland, miles_to_atlanta, miles_to_tucson,
                 miles_to_pittsburgh, id_number):

        self.name = name
        self.latitude = latitude
        self.longitute  = longitude
        self.miles_to_la = miles_to_la
        self.miles_to_lv = miles_to_lv
        self.miles_to_nyc = miles_to_nyc
        self.miles_to_slc = miles_to_slc
        self.miles_to_miami = miles_to_miami
        self.miles_to_dallas = miles_to_dallas
        self.miles_to_milwaukee = miles_to_milwaukee
        self.miles_to_boston = miles_to_boston
        self.miles_to_lincoln = miles_to_lincoln
        self.miles_to_seattle = miles_to_seattle
        self.miles_to_portland = miles_to_portland
        self.miles_to_atlanta = miles_to_atlanta
        self.miles_to_tucson = miles_to_tucson
        self.miles_to_pittsburgh = miles_to_pittsburgh
        self.id_number = id_number

    def make_dictionary_of_distances(self):

        distances = {'miles_to_la' : self.miles_to_la,
                     'miles_to_lv': self.miles_to_lv,
                     'miles_to_nyc': self.miles_to_nyc,
                     'miles_to_slc': self.miles_to_slc,
                     'miles_to_miami': self.miles_to_miami,
                     'miles_to_dallas': self.miles_to_dallas,
                     'miles_to_milwaukee': self.miles_to_milwaukee,
                     'miles_to_boston' : self.miles_to_boston,
                     'miles_to_lincoln' : self.miles_to_lincoln,
                     'miles_to_seattle' : self.miles_to_seattle,
                     'miles_to_portland' : self.miles_to_portland,
                     'miles_to_atlanta' : self.miles_to_atlanta,
                     'miles_to_tucson' : self.miles_to_tucson,
                     'miles_to_pittsburgh' : self.miles_to_pittsburgh}

        return distances





def main():

    #list of 6 cities
    #la = City("la", 34.02, 118.4, 0, 228, 2481, 579, 2339, 1240, 1)
    #lv = City("lv", 36.23, 115.3, 228, 0, 2233, 362, 2181, 1071, 2)
    #nyc = City("nyc", 40.66, 73.94, 2451, 2233, 0, 1972, 1089, 1373, 3)
    #slc = City("slc", 40.78, 111.9, 579, 362, 1972, 0, 2089, 1000, 4)
    #miami = City("miami", 25.78, 80.21, 2339, 2181, 1089, 2089, 0, 1111, 5)
    #dallas = City("dallas", 32.79, 96.77, 1240, 1071, 1373, 1000, 1111, 0, 6)

    #set of 8
    #la = City("la", 34.02, 118.4, 0, 228, 2481, 579, 2339, 1240, 1744, 2597, 1)
    #lv = City("lv", 36.23, 115.3, 228, 0, 2233, 362, 2181, 1071, 1521, 2375, 2)
    #nyc = City("nyc", 40.66, 73.94, 2451, 2233, 0, 1972, 1089, 1373, 734, 190, 3)
    #slc = City("slc", 40.78, 111.9, 579, 362, 1972, 0, 2089, 1000, 1242, 2099, 4)
    #miami = City("miami", 25.78, 80.21, 2339, 2181, 1089, 2089, 0, 1111, 1268, 1256, 5)
    #dallas = City("dallas", 32.79, 96.77, 1240, 1071, 1373, 1000, 1111, 0, 857, 1552, 6)
    #milwaukee = City("milwaukee", 43.06, 87.97, 1744, 1521, 734, 1242, 1268, 857, 0, 858, 7)
    #boston = City("boston", 42.33, 71.02, 2597, 2375, 190, 2099, 1256, 1552, 858, 0, 8)

    # set of 14 cities
    la = City("la", 34.02, 118.4, 0, 228, 2481, 579, 2339, 1240, 1744, 2597, 1269, 959, 825, 1937, 440, 2137, 1)
    lv = City("lv", 36.23, 115.3, 228, 0, 2233, 362, 2181, 1071, 1521, 2375, 1047, 871, 755, 1746, 362, 1920, 2)
    nyc = City("nyc", 40.66, 73.94, 2451, 2233, 0, 1972, 1089, 1373, 734, 190, 1187, 2048, 2446, 746, 2123, 316, 3)
    slc = City("slc", 40.78, 111.9, 579, 362, 1972, 0, 2089, 1000, 1242, 2099, 796, 701, 636, 1583, 591, 1668, 4)
    miami = City("miami", 25.78, 80.21, 2339, 2181, 1089, 2089, 0, 1111, 1268, 1256, 1405, 2733, 2708, 604, 1908, 1011, 5)
    dallas = City("dallas", 32.79, 96.77, 1240, 1071, 1373, 1000, 1111, 0, 857, 1552, 554, 1681, 1633, 721, 828, 1070, 6)
    milwaukee = City("milwaukee", 43.06, 87.97, 1744, 1521, 734, 1242, 1268, 857, 0, 858, 478, 1692, 1720, 669, 1461, 446, 7)
    boston = City("boston", 42.33, 71.02, 2597, 2375, 190, 2099, 1256, 1552, 858, 0, 1328, 2492, 2540, 937, 2284, 483, 8)
    lincoln = City("lincoln", 40.81, 96.68, 1269, 1047, 1187, 796, 1405, 554, 478, 1328, 0, 1349, 1346, 834, 989, 877, 9)
    seattle = City("seattle", 47.62, 122.4, 959, 871, 2048, 701, 2733, 1681, 1692, 2492, 1349, 0, 145, 2182, 1218, 2138, 10)
    portland = City("portland", 45.54, 122.6, 825, 755, 2446, 636, 2708, 1633, 1720, 2540, 1346, 145, 0, 2173, 1111, 2166, 11)
    atlanta = City("atlanta", 33.76, 84.42, 1937, 1746, 746, 1583, 604, 721, 669, 937, 834, 2182, 2173, 0, 1543, 521, 12)
    tucson = City("tucson", 32.15, 110.9, 440, 362, 2123, 591, 1908, 828, 1461, 2284, 989, 1218, 1111, 1543, 0, 1808, 13)
    pittsburg = City("pittsburgh", 40.44, 79.98, 2137, 1920, 316, 1668, 1011, 1070, 446, 483, 877, 2138, 2166, 521, 1808, 0, 14)


    #with open('cd.csv') as csvfile:
    #    reader = csv.DictReader(csvfile)
    #    for row in reader:
    #        print(row['start_city'], row['end_city'], row['distance'])

    cities = [la, lv, nyc, slc, miami, dallas, milwaukee, boston, lincoln, seattle, portland, atlanta, tucson, pittsburg]

    #print (cities[0].name, cities[1].name, cities[2].name, cities[3].name, cities[4].name, cities[5].name)

    best_distance = 10000
    worst_distance = 0
    num_distances = []
    for run_times in range(1000000):
        total_miles = 0
        shuffle(cities)
        for i in range(len(cities)):


            #print(i)
            #print(cities[i].name)
            dictionary = cities[i].make_dictionary_of_distances()
            #print (dictionary)
            if (i < (len(cities) - 1)):
                next_city = "miles_to_" + cities[i + 1].name
                total_miles += dictionary[next_city]
                #print (next_city)
                #print (total_miles)
                #if (cities[i].miles)
                #print (cities[i].miles_to_ + cities[i + 1].name)
            else:
                next_city = "miles_to_" + cities[0].name
                total_miles += dictionary[next_city]
                #print(next_city)
                #print(total_miles)

        num_distances.append(total_miles)

        if (total_miles < best_distance):
            best_distance = total_miles
            best_cities = cities
            print("update best:", "Num: " + str(run_times))
            #for i in range(len(best_cities)):
                #print(best_cities[i].name, end=" ")


            print(best_distance)
        if (total_miles > worst_distance):
            worst_distance = total_miles
            worst_cities = cities
            print("update worst:", "Num: " + str(run_times))
            #for i in range(len(worst_cities)):
                #print(worst_cities[i].name, end=" ")

            print(worst_distance)

    print("This is the best distance")
    print (best_distance)
    print ("This is the worst Distance")
    print (worst_distance)
    # There is a bug here whcih makes so the cities do not print out the worst and best list.
    #for i in range(len(best_cities)):
     #  print (best_cities[i].name, end=" ")
    #for i in range(len(worst_cities)):
       # print (worst_cities[i].name, end=" ")
    '''
    with open('gendist.csv', 'w') as csvfile:
        #fieldnames = ['first_name', 'last_name',]
        fieldnames = ['distances']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(1000):
            writer.writerow({'distances': num_distances[i]})
        #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})'''

if __name__ == '__main__' :

    main()