# Intern assignment for emarsys - Tóth Bálint
# Route planner
# Implemented in python

# Based on the given assignment, the following TODO's I have:

 - Creating a STOP class, where every instance has a 'name' field (e.g. "x") and a 'previous' field to keep track of the optional previous stop.

 - Creating a Route class, its stops list will collect the located stops.

 - Creating a Planner class, it recieves a list of unlocated stops, and places them in order. Its methods return infos bout the route.

 - Writing test  - for the edge cases also (circle, forking, unable to start)

# Basic algorithm to create the order:

 - Keep picking out a stop from the unlocated stops

 - The one that is picked out is either the one that has the current last as 'previous'

 - ... or if there is none like that, one with 'None' as previous

# TODO:

 - The algorithm above is really slow - kind of brute force - research is needed for a faster sorting method
