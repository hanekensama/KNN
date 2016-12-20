import simplejson as json

from KNN import KNN


def main():
    with open("test1.json") as read_file:
        knn = KNN(json.load(read_file))

    while True:
        func = int(input("[1]add [2]check [3]disp [0]exit :"))
        if func == 0:
            save = input("save current nodes? (y/n) :")
            if save == "y" or "Y":
                file_name = input("file name :")
                with open(file_name, "w") as write_file:
                    json.dump(knn.nodes, write_file, sort_keys=True, indent=2)
            break

        elif func == 1:
            x, y = map(int, input("x y :").split())
            k = int(input("k :"))
            print(knn.add(value=(x, y), k=k))

        elif func == 2:
            x, y = map(int, input("x y :").split())
            print(knn.cluster(value=(x, y)))

        elif func == 3:
            print(knn.nodes)

        else:
            print("Error! : illegal input")

if __name__ == '__main__':
    main()
