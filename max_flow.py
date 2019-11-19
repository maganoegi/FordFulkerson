


'''  
       ./=======================================================================\.
        |           * PLATONOV Sergey         KALTRACHIAN Téo                   | 
        |           * Algorithmes avancées                                      | 
        |           * Algorithme de Ford-Fulkerson                              | 
        |           * HEPIA ITI sem. 3            * max_flow.py                 | 
       .\=======================================================================/. 
'''

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
if(len(mlib.sys.argv) != 2):
    mlib.sys.exit(mlib.bcolors.WARNING + "====== Please provide 1 argument: ======" + mlib.bcolors.ENDC + "\n\tInput file name describing the network.")
else:
    input_file_name = mlib.sys.argv[1]

#============================================================#
#            Calculate Max flow and write to file            #
#============================================================#
mlib.edmondsKarp(input_file_name)




# EXEMPLES

# maxflow: 10
    # 4 5
    # 1 2 4
    # 2 4 5
    # 1 3 7
    # 3 4 6
    # 2 3 12

# maxflow: 23
    # 6 10
    # 1 2 16
    # 1 3 13
    # 2 3 10
    # 3 2 4
    # 2 4 12
    # 3 5 14    
    # 4 3 9
    # 5 4 7
    # 4 6 20
    # 5 6 4

# maxflow: 24
    # 23 32 
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
