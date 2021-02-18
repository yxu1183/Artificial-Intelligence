"""
Name: Yunika Upadhayaya
ID: 1001631183
Assignment: 1
Professor: Dr. Vamsikrishna Gopikrishna
CSE - 4308 - 002
"""


# This file consists of all the functions required to implement search algorithms in main file


def change_node(map_fringe, search_inf):  # Function to sort the fringe in the search algorithms
    if len(map_fringe) <= 1:
        return map_fringe
    else:
        for check in range(0, len(map_fringe) - 1):
            first = check
            for next_check in range(check + 1, len(map_fringe)):
                a = map_fringe[first]["cost"]
                value = map_fringe[next_check]["cost"]
                if search_inf:
                    a += map_fringe[first]["value_h"]
                    value += map_fringe[next_check]["value_h"]
                if a > value:
                    first = next_check
            cloner_path = map_fringe[first]
            map_fringe[first] = map_fringe[check]
            map_fringe[check] = cloner_path
        return map_fringe


def node_visit(checked_array, indx_nod):  # Function to check if the node is already visited
    for node_pres in checked_array:
        if indx_nod == node_pres["current"]:
            return 1
    return 0
