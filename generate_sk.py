# Generates necessary files to model South Korea

import random

PROB_START_STATION = .1
PROB_FUT_STATION = .2
NUM_WEEKS = 100

def main():
    cities = []
    edges = {}

    # tup = (cname, pop, area, density)
    seo = ("seoul", 9805506, 605, 16202)
    seo_edges = [330, 30, 240, 140, 270, 30, 310, 300]
    cities.append(seo)
    edges[seo[0]] = seo_edges

    bus = ("busan", 3440484, 768, 4477)
    bus_edges = [340, 100, 200, 190, 300, 50, 40]
    cities.append(bus)
    edges[bus[0]] = bus_edges

    inc = ("incheon", 2913024, 1032, 2822)
    inc_edges = [240, 140, 260, 30, 320, 300]
    cities.append(inc)
    edges[inc[0]] = inc_edges

    dag = ("daegu", 2461002, 884, 2785)
    dag_edges = [120, 170, 210, 80, 70]
    cities.append(dag)
    edges[dag[0]] = dag_edges

    daj = ("daejeon", 1535445, 540, 2844)
    daj_edges = [140, 110, 190, 170]
    cities.append(daj)
    edges[daj[0]] = daj_edges

    gwa = ("gwangju", 1501557, 501, 2996)
    gwa_edges = [240, 220, 160]
    cities.append(gwa)
    edges[gwa[0]] = gwa_edges

    gyg = ("suwon", 1207032, 121, 9974)
    gyg_edges = [280, 270]
    cities.append(gyg)
    edges[gyg[0]] = gyg_edges

    uls = ("ulsan", 1166033, 1060, 110)
    uls_edges = [70]
    cities.append(uls)
    edges[uls[0]] = uls_edges

    gsn = ("changwon", 1053551, 745, 1414)
    cities.append(gsn)
    edges[gsn[0]] = []

    # Square numbers
    squares = get_nearest_squares(cities)
    edge_dist = str(1)

    # Generate files
    city_nodes, counter = make_nodes(cities, squares)

    with open("sk_nodes.txt", "w") as node_f, open("sk_edges.txt", "w") as edge_f, open("sk_cities.txt", "w") as city_f:
        road_string = "road"

        for h in range(len(cities)):
            city = cities[h]
            nodes = city_nodes[city]
            city_string = city[0]

            for i in range(len(nodes)):
                node_row = nodes[i]

                for j in range(len(node_row)):
                    node = node_row[j]
                    name = node[0]
                    time = node[1]
                    is_station = node[2]

                    node_f.write(name + ", " + time + ", " + is_station + "\n")

                    if j > 0:
                        left_name = node_row[j-1][0]
                        edge_f.write(name + ", " + left_name + ", " + edge_dist + "\n")
                    if i > 0:
                        up_name = nodes[i-1][j][0]
                        edge_f.write(name + ", " + up_name + ", " + edge_dist + "\n")

                    city_string = city_string + ", " + name

            city_f.write(city_string + "\n")

            for j in range(len(edges[city[0]])):
                to_city = h + j + 1
                to_node = cities[to_city]
                dist = edges[city[0]][j]

                for k in range(dist / 10 + 1):
                    name = str(counter)
                    prev = str(counter - 1)
                    counter += 1

                    if k != 0:
                        edge_f.write(name + ", " + prev + ", " + str(10) + "\n")
                    else:
                        ind_1 = random.randrange(0, len(nodes)-1)
                        ind_2 = random.randrange(0, len(nodes[ind_1])-1)

                        edge_f.write(name + ", " + nodes[ind_1][ind_2][0] + ", " + str(10) + "\n")

                    time = "inf"
                    is_station = "False"                    

                    if random.random() < PROB_FUT_STATION:
                        time = str(random.randrange(1, NUM_WEEKS))
                    elif random.random() < PROB_START_STATION:
                        is_station = "True"
                    
                    node_f.write(name + ", " + time + ", " + is_station + "\n")

                    road_string += ", " + name

                    if k == dist / 10:
                        ind_1 = random.randrange(0, len(city_nodes[to_node]) -1)
                        ind_2 = random.randrange(0, len(city_nodes[to_node][ind_1])-1)
                        edge_f.write(name + ", " + city_nodes[to_node][ind_1][ind_2][0] + ", " + str(10) + "\n")

        city_f.write(road_string + "\n")
            

def get_nearest_squares(cities):
    squares = {} # key = city name, value = nearest square area    

    for city in cities:
        area = city[2]
        name = city[0]
        last = 0
        this = 0

        for i in range(2500):
            square = i*i
            last = this
            this = i

            if square > area:
                break

        if area - last > this - area:
            squares[name] = this
        else:
            squares[name] = last

    return squares

def make_nodes(cities, squares):
    counter = 0
    city_nodes = {}

    for city in cities:
        dimension = squares[city[0]]
        nodes = []

        for i in range(dimension):
            node_row = []

            for j in range(dimension):
                name = str(counter)
                counter += 1
                time = "inf"
                is_station = "False"                    

                if random.random() < PROB_FUT_STATION:
                    time = str(random.randrange(1, NUM_WEEKS))
                elif random.random() < PROB_START_STATION:
                    is_station = "True"

                node_row.append((name, time, is_station))

            nodes.append(node_row)

        city_nodes[city] = nodes

    return city_nodes, counter

if __name__ == "__main__":
    main()
