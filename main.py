from KNN import KNN

def main():
    knn = KNN()
    knn.read("sample1.json")

    while True:
        func = int(input("[1]add [2]check [3]disp [4]plot [0]exit :"))

        if func == 0:

            save = input("save current nodes? (y/n) :")
            if save == "y" or "Y":
                knn.write(input("file name :"))
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

        elif func == 4:
            colors = {}
            for cluster in knn.clusterList():
                color = input("colors for {0} :".format(cluster))
                colors[cluster] = color
            knn.plot(colors)

        else:
            print("Error! : illegal input")

if __name__ == '__main__':
    main()
