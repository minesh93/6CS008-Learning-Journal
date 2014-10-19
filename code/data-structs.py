#-- Normal Array of Ints
array = [0,1,23,45,67,89];

print array[3];

#-- Mixed Array
mixedArray = ["two",1,"one"];

#-- The string
print mixedArray[0];

#-- The Int
print mixedArray[1];

#-- Iterate over the array with a for loop

counter = 0;

for item in mixedArray:
	print 'Index of [' + str(counter) + '] is: ' + str(item)

	#-- Python does not like incrementing values like that as it throws an error
	#-- counter++
	#--! Find out why.

	#-- That works		
	counter += 1



#-- Set everything in the array to 0

#-- First reset the counter
counter = 0;

for item in mixedArray:
	mixedArray[counter] = 0

	#-- Python does not like incrementing values like that as it throws an error
	#-- counter++
	#--! Find out why.

	#-- That works		
	counter += 1

print mixedArray

#-- Aaaand sublime has an inbuilt python console!


