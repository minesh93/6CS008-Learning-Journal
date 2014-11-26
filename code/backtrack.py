world_map ={'Orades': {'Zerind':71, 'Sibiu':151},
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


from sets import Set

def greedy_route(current_map,start, end, route = [], visited = Set(), total_distance = 0):
    
    visited.add(start)   # visited will contain all the cities we've already visited, so that we avoid going in circles!
    
    if start == end:     # in case our start and end are the same city
        print 'Start city is the same as end!'
        return route,0
    
    if not current_map.has_key(start) or not current_map.has_key(end):   # in case the start or the end aren't in our current_map
        print 'No possible route'
        return
    
    else:                                          # if all's well, let's find the closest city to our current 'start'
        min_distance = 100000                      # temporarily set the minimum distance from 'start' city to high number                              
        closest_city = '';                                                               
        
        for dest in current_map[start].keys():     #iterate through the connected cities and get/print their distance                  
            print '%s->%s: %d' % (start, dest, current_map[start][dest])    
            
            if dest == end:                       # if we've found our final destination, even if it's not the closest city
                route.append(dest)
                total_distance = total_distance + current_map[start][dest]
                return route, total_distance
            
            elif current_map[start][dest] < min_distance and dest not in visited:   # if the city we are examining now is closer than the current minimum
                min_distance = current_map[start][dest]                             # AND also we haven't visited the city already
                closest_city = dest
        
        if closest_city == '':                            # if we reach a dead-end
            print 'Dead end!'
            return [],0
        
        route.append(closest_city)                         # add the closest_city to the route and the set of visited cities
        visited.add(closest_city)                
        total_distance = total_distance + min_distance      # also add its distance to total distance
        print 'Closest  (& not visited): %s' % closest_city
        print 'Distance so far: %d \n' % total_distance
        
        if closest_city == end:
            return route,total_distance
        else:
            route, total_distance = greedy_route(current_map,closest_city,end,route,visited,total_distance)
          
        return route,total_distance
            
        
itenary, distance = greedy_route(world_map, 'Arad','Bucharest')
print 'Greedy route is:', itenary
print 'Total km:', distance