import json, math

#Function that takes an origin in the format a,b
def coordinates_distance(origin):

    #Opening the file to read all the 26 coordinates
    with open('coordinates.json') as fp:
        data = json.load(fp)
	
    output = []
	
	#iterating through the above read data
    for c in data:
		#getting the coordinates in a list by splitting with ','
        cords = [int(x) for x in c['value'].split(',')]
		
		#calculating the distance using the distance formula i.e sqrt((x2-x1)**2 + (y2-y1)**2)
        dis = math.sqrt((origin[0] - cords[0]) ** 2 + (origin[1] - cords[1]) ** 2)
		
        o = c.copy()
		
		#adding another key - distance in the dictionary o.
        o.update({'distance': dis})
        output.append(o)

		
	#sorting the dictionary with the 'distance' key	
    output = sorted(output, key = lambda x: x['distance'])
    actualout = []
	
	#for getting the output
    for i in output:
        x = i.copy()
        x.pop('distance')
        actualout.append(x)
        print x

    return actualout

	
if __name__ == '__main__':

	#asking the user for an input
    origin = raw_input('Enter origin')
    origin = [int(x) for x in str(origin).split(',')]
	
	#calling the function and passing the user's coordinates
    coordinates_distance(origin)