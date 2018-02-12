# Generates necessary files to model South Korea

def main():
    cities = []

    # tup = (cname, pop, area, density)
    seo = ("seoul", 9805506, 605, 16202)
    cities.append(seo)
    bus = ("busan", 3440484, 768, 4477)
    cities.append(bus)
    inc = ("incheon", 2913024, 1032, 2822)
    cities.append(inc)
    dag = ("daegu", 2461002, 884, 2785)
    cities.append(dag)
    daj = ("daejeon", 1535445, 540, 2844)
    cities.append(daj)
    gwa = ("gwangju", 1501557, 501, 2996)
    cities.append(gwa)
    gyg = ("suwon", 1207032, 121, 9974)
    cities.append(gyg)
    uls = ("ulsan", 1166033, 1060, 110)
    cities.append(uls)
    gsn = ("changwon", 1053551, 745, 1414)
    cities.append(gsn)

    # Square numbers
    squares = get_nearest_squares(cities)

    # Generate node file
    #
    # Divide cities into square grids


    # Generate edge file

    # Generate city file

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
            this = square

            if square > area:
                break

        if area - last > this - area:
            squares[name] = this
        else:
            squares[name] = last

    return squares

if __name__ == "__main__":
    main()
