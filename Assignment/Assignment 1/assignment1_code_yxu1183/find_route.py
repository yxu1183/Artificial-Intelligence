"""
Name: Yunika Upadhayaya
ID: 1001631183
Assignment: 1
Professor: Dr. Vamsikrishna Gopikrishna
CSE - 4308 - 002
"""

import sys

# Important implementation of functions from another file
from implementation import change_node
from implementation import node_visit


def ucs():  # Function that implements uninformed search using uniform cost search algorithm
    map_fringe = []
    nodes_searched = []
    end_node = fringe_nodes.index(city_dest)
    cost = False
    map_fringe.append({
        "current_position": fringe_nodes.index(city_origin),
        "cost": 0,
        "parent_position": None
    })
    find_generated = 0
    find_expanded = 0
    while len(map_fringe) > 0:
        if node_visit(nodes_searched, map_fringe[0]["current_position"]):
            del map_fringe[0]
            find_expanded += 1
            continue
        elif map_fringe[0]["current_position"] == end_node:
            nodes_searched.append({
                "current": map_fringe[0]["current_position"],
                "parent_position": map_fringe[0]["parent_position"]
            })
            cost = map_fringe[0]
            find_expanded += 1
            break
        else:
            find_expanded += 1
            nodes_searched.append({
                "current": map_fringe[0]["current_position"],
                "parent_position": map_fringe[0]["parent_position"]
            })
            for i in range(len(fringe[map_fringe[0]["current_position"]])):
                if fringe[map_fringe[0]["current_position"]][i] > 0:
                    map_fringe.append({
                        "current_position": i,
                        "cost": map_fringe[0]["cost"] + fringe[map_fringe[0]["current_position"]][i],
                        "parent_position": map_fringe[0]["current_position"]
                    })
                    find_generated += 1

            del map_fringe[0]
            map_fringe = change_node(map_fringe, False)

    find_generated += 1
    find_track(find_expanded, cost, nodes_searched, find_generated)
    return


def a_algo():  # Function to implement informed search -  A* algorithm
    map_fringe = []
    nodes_searched = []
    end_node = fringe_nodes.index(city_dest)
    cost = False
    find_generated = 0
    find_expanded = 0
    map_fringe.append({
        "current_position": fringe_nodes.index(city_origin),
        "cost": 0,
        "value_h": fringe_heu[fringe_nodes.index(city_origin)],
        "parent_position": None
    })
    while len(map_fringe) > 0:
        if node_visit(nodes_searched, map_fringe[0]["current_position"]):
            del map_fringe[0]
            find_expanded += 1
            continue
        elif map_fringe[0]["current_position"] == end_node:
            nodes_searched.append({
                "current": map_fringe[0]["current_position"],
                "parent_position": map_fringe[0]["parent_position"]
            })
            cost = map_fringe[0]
            find_expanded += 1
            break
        else:
            nodes_searched.append({
                "current": map_fringe[0]["current_position"],
                "parent_position": map_fringe[0]["parent_position"]
            })
            find_expanded += 1
            for i in range(len(fringe[map_fringe[0]["current_position"]])):
                if fringe[map_fringe[0]["current_position"]][i] > 0:
                    map_fringe.append({
                        "current_position": i,
                        "cost": map_fringe[0]["cost"] + fringe[map_fringe[0]["current_position"]][i],
                        "value_h": fringe_heu[i],
                        "parent_position": map_fringe[0]["current_position"]
                    })
                    find_generated += 1
            del map_fringe[0]
            map_fringe = change_node(map_fringe, True)

    find_generated += 1
    find_track(find_expanded, cost, nodes_searched, find_generated)
    return


def find_track(find_expanded, cost, checked_array, find_generated_nodes):  # Function to find the route by backtracking
    path_tracker = []

    def reverse(city_dest, checked_array):
        if city_dest is not None:
            for node_visited in checked_array:
                if node_visited["current"] == city_dest:
                    path_tracker.append(city_dest)
                    reverse(node_visited["parent_position"], checked_array)
        else:
            return

    if not cost:
        print("nodes expanded: " + str(find_expanded))
        print("nodes generated: " + str(find_generated_nodes))
        print("distance: infinity")
        print("route:")
        print("none")
    else:
        print("nodes expanded: " + str(find_expanded))
        print("nodes generated: " + str(find_generated_nodes))
        print(f"distance: {cost['cost']:.1f} km")
        print("route:")
        reverse(cost["current_position"], checked_array)
        path_tracker.reverse()
        for i in range(0, len(path_tracker) - 1):
            print(f"{fringe_nodes[path_tracker[i]]} to {fringe_nodes[path_tracker[i + 1]]}, "
                  f"{fringe[path_tracker[i]][path_tracker[i + 1]]:.1f} km")
    return


def fringe_Creation(inp_file):  # Function that reads input file and constructs the map for further operations
    for path in inp_file:
        if path.upper() != 'END OF INPUT':
            cloner_path = path.strip().split(" ")
            a = cloner_path[0]
            b = cloner_path[1]
            if b not in fringe_nodes:
                fringe_nodes.append(b)
            else:
                pass
            if a not in fringe_nodes:
                fringe_nodes.append(a)
            else:
                pass
        else:
            break

    fringe_nodes.sort()

    for i in range(len(fringe_nodes)):
        fringe.append([])
        for j in range(len(fringe_nodes)):
            fringe[i].append(-1)
        fringe[i][j] = 0

    for path in inp_file:
        if path.upper() != 'END OF INPUT':
            cloner_path = path.strip().split(" ")
            a = cloner_path[0]
            b = cloner_path[1]
            c = cloner_path[2]
            fringe[fringe_nodes.index(a)][fringe_nodes.index(b)] = int(c)
            fringe[fringe_nodes.index(b)][fringe_nodes.index(a)] = int(c)
        else:
            break
    return


def h_fringe(heur_file):  # Function that adds the huerisitic values in a list
    for value_h in heur_file:
        if value_h.upper() != 'END OF INPUT':
            final_value = value_h.split(" ")
            fringe_heu[fringe_nodes.index(final_value[0])] = int(final_value[1])
        else:
            break
    return


# Main function starts here
if len(sys.argv) < 4 or len(sys.argv) > 5:  # Prompt user to provide correct arguments if wrong
    print('Improper format!')
    print('Try:')
    print('find_route.py <input_file> <origin> <destination>"--> for uniformed search')
    print('OR:')
    print('"find_route.py <input_file> <origin> <destination> <heuristic_file>"--> for informed search')
else:
    fringe_nodes = []
    fringe = []
    city_origin = sys.argv[2]
    city_dest = sys.argv[3]
    input_file = open(sys.argv[1], "r")
    fringe_Creation(input_file.read().split("\n"))

    if len(sys.argv) == 5:
        fringe_heu = [0] * len(fringe_nodes)
        heur_file = sys.argv[4]
        input_hue = open(sys.argv[4], "r")
        h_fringe(input_hue.read().split("\n"))
        a_algo()
        input_hue.close()
    elif len(sys.argv) == 4:
        ucs()
        input_file.close()
