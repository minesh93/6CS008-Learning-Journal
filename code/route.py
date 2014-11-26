import itertools 


def exhaustiveRouteFind(map,start,finish):
    cityList = map.keys();

    filters = []

    perms = itertools.permutations(cityList)

    # for perm in perms:
        # if perm[0] == start and perm[-1] == finish:
        #     filters.append(perm)


    print 'finished making permutations'
    print len(filters);
    return 1    



print exhaustiveRouteFind(world_map,'Arad','Bucharest')
# Greedy route is: ['Zerind', 'Orades', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']