

#                   ----------------------------------------------------------------------
#                   |             * PLATONOV Sergey         KALTRACHIAN Téo              |
#                   |             * Algorithmes avancées                                 |
#                   |             * Algorithmes de Ford-Fulkerson                        | 
#                   |             * HEPIA ITI sem. 3            * max_flow.py            | 
#                   ----------------------------------------------------------------------

#!/usr/bin/python3
import sys

#============================================================#
#                  Variables initialization                  #
#============================================================#
nb_nodes = 0
nb_edges = 0
capacity = 0
splitted = []
network_edges = []

#============================================================#
#              Take arguments from command-line              #
#============================================================#
input_file_name = sys.argv[1]

#============================================================# 
#          Get and organize contents of the file             #
#============================================================#
with open (input_file_name, "r") as f:
    for index, line in enumerate(f):
        line = line.rstrip()
        splitted = line.split(" ")
        if index == 0:              
            nb_nodes = int(splitted[0])
            nb_edges = int(splitted[1])
        else:
            edge_vals = []
            for i in range(3):
                edge_vals.append(int(splitted[i]))
            network_edges.append(edge_vals)

#============================================================# 
#                       Hidden Layer                         #
#============================================================#


