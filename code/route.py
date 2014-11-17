import itertools 


world_map = {'Orades': {'Zerind':71, 'Sibiu':151},
            'Zerind': {'Arad':75, 'Orades':71},
            'Arad': {'Timisoara':118, 'Zerind':75, 'Sibiu':140},
            'Timisoara': {'Lugoj': 111, 'Arad':118},
            'Lugoj': {'Mehadia':70, 'Timisoara':111},
            'Mehadia':{'Dobreta':75, 'Lugoj':70},
            'Dobreta': {'Craiova':120,'Mehadia':70},
            'Craiova': {'Rimnicu Vilcea':146, 'Pitesti':138},
            'Rimnicu Vilcea': {'Sibiu':80, 'Pitesti':97, 'Craiova':138},
            'Sibiu': {'Arad':140, 'Oradea':151, 'Fagares':99, 'Rimnicu Vilcea':80},
            'Fagares': {'Bucharest':211, 'Sibiu':99},
            'Pitesti': {'Rimnicu Vilcea':97, 'Bucharest':101, 'Craiova':138},
            'Bucharest': {'Giurgiu':90, 'Urziceni':85, 'Fagares':211, 'Pitesti':101},
            'Urziceni': {'Hirsova':98, 'Vaslui':142, 'Bucharest':85},
            'Giurgiu': {'Bucharest':90},
            'Hirsova': {'Eforie':86, 'Urziceni':98},
            'Eforie': {'Hirsova':86},
            'Vaslui': {'Iasi':92, 'Urziceni':142},
            'Iasi' : {'Neamt':87, 'Vaslui':92},
            'Neamt': {'Iasi':87},
          }






def exhaustiveRouteFind(map,start,finish):
    cityList = map.keys();  
    size = len(cityList)
    for c in itertools.permutations(cityList, size):
        print c[0]


    return 1    
exhaustiveRouteFind(world_map,'Arad','Bucharest')

# Greedy route is: ['Zerind', 'Orades', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']


    # visited = []
    # current = map[start]
    # currentCity = start
    # breakCount = 0
    # totalDisance = 0

    # while start != finish:
    # while breakCount != 20:
    #     current = map[currentCity]
    #     lowestDistance = 100000
    #     lowestCurrent = ""
    #     for choices in current.keys():
    #         # print 'distance from ' + currentCity + " to " + choices + " is: " + str(current[choices])

    #         # if current[choices] < lowestDistance:
    #         #     lowestDistance = current[choices]
    #         #     lowestCurrent = choices

    #     # currentCity = lowestCurrent
    #     # print 'Moving to ' + currentCity
    #     # visited.append(currentCity);

    #     # print lowestDistance
    #     breakCount +=1

    # print visited