from KNN import KNN


def main():
    knn = KNN()
    values = [(1, 2), (1, 3), (1, 1), (4, 4), (4, 5), (4, 6)]
    clusters = ["red", "red", "red", "blue", "blue", "blue"]
    for i in range(len(values)):
        knn.add(value=values[i], cluster=clusters[i])

    print(knn.add(value=(2, 1), k=5))  # red
    print(knn.add(value=(5, 5), k=3))  # blue


if __name__ == '__main__':
    main()
