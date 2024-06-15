#Task 1 Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def common_destinations(our_routes, competitor_routes):
    common_routes = our_routes.intersection(competitor_routes)
    return common_routes

def our_unique_destinations(our_routes, competitor_routes):
    our_exclusive_routes = our_routes.difference(competitor_routes)
    return our_exclusive_routes

def unshared_destinations(our_routes, competitor_routes):
    unique_routes = our_routes.symmetric_difference(competitor_routes)
    return unique_routes

common_destination = common_destinations(our_routes, competitor_routes)
print(f"\nThe following destinationas are common to both airlines: {common_destination}")
'''
I used the .intersection method to set up the common_destinations funtion and assigned its return to the vaiable common_destination before using that in a print statement
'''

our_unique_destination = our_unique_destinations(our_routes, competitor_routes)
print(f"\nThe following destinationas are unique to our airline: {our_unique_destination}")
'''
After using the .difference method in the our_unique_destinations function I repeated the same process for common destinations to print off the set of destinations unique to our airline
'''

unshared_destination = unshared_destinations(our_routes, competitor_routes)
print(f"\nThe following destinationas are unique for either airline: {unshared_destination}")
'''
I used the .symmetric_difference method in the unshared_destinations fucntion and saved its return in the variable unshared_destinations before using that variable in a print statement to display the set of destinations neither airlines share. 
'''