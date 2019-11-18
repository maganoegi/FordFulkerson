

#                   ----------------------------------------------------------------------
#                   |             * PLATONOV Sergey         KALTRACHIAN Téo              |
#                   |             * Algorithmes avancées                                 |
#                   |             * Algorithme de Ford-Fulkerson                         | 
#                   |             * HEPIA ITI sem. 3            * max_flow.py            | 
#                   ----------------------------------------------------------------------

#!/usr/bin/python3
import mylib as mlib

#============================================================#
#                  Variables initialization                  #
#============================================================#
nb_nodes = 0
splitted = []
network_edges = []
graph = []
#============================================================#
#              Take arguments from command-line              #
#============================================================#
# input_file_name = sys.argv[1]
input_file_name = "input_network.txt"

#============================================================# 
#     Extract contents file     +     Populate matrix        #
#============================================================#
with open(input_file_name, "r") as f:
    for index, line in enumerate(f):
        # remove trailing \n in the end of the string
        line = line.rstrip()

        # split string into array of substrings
        splitted = line.split(" ")

        # first line is data about the flow network ...
        if index == 0:  
            nb_nodes = int(splitted[0])
            
            # use the data to create a matrix filled with zeros
            graph = mlib.generate_matrix_of_dimension(nb_nodes, nb_nodes)

        # ... and the rest are edges, whose info we insert into the matrix
        else:    
            source = int(splitted[0]) - 1           #======================#         
            destination = int(splitted[1]) - 1      #  Matrix:     0-based
            capacity = int(splitted[2])             #  Nodes:      1-based
                                                    #  hence, "-1" here     
            graph[source][destination] = capacity   #======================#
                                                    
    f.close()

#============================================================# 
#               Apply Ford-Fulkerson algorithm               #
#============================================================#

# create an instance of the graph class, using our matrix
g = mlib.Graph(graph)

# execute algorithm
source = 0; sink = (nb_nodes - 1)
maximum_flow = g.FordFulkerson(source, sink)


#============================================================# 
#                    Visualisation Results                   #
#============================================================#
print ("Max Flow of this network is = " + mlib.bcolors.GREEN + str(maximum_flow) + mlib.bcolors.ENDC)

for i in range(nb_nodes):
    print(str(graph[i]))






# 6 10
# 1 2 16
# 1 3 13
# 2 3 10
# 3 2 4
# 2 4 12
# 3 5 14     maxflow: 23 
# 4 3 9
# 5 4 7
# 4 6 20
# 5 6 4

# 23 32     maxflow: 24
# 1 2 10
# 1 3 14
# 2 13 25
# 13 5 72
# 13 20 15
# 5 7 9
# 5 14 18
# 7 9 4
# 14 17 24
# 14 20 34
# 9 11 42
# 9 19 42
# 11 19 50
# 17 21 12
# 20 22 14
# 21 22 16
# 21 23 25
# 19 21 19
# 19 23 16
# 3 15 10
# 3 4 11 
# 4 15 12
# 4 6 17
# 15 6 19
# 15 16 34
# 6 18 35
# 16 8 10
# 8 22 16
# 18 10 58
# 10 12 11
# 12 22 45
# 22 23 32
