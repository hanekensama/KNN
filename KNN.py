from collections import Counter, defaultdict
from math import hypot

class KNN:
    """ K近傍法のためのノードを集めた集合
        add(): ノードの追加
        cluster(): 指定したノードのクラスタの番号を取得
        dataList(): 指定したクラスタのノードのリストを取得
        clusterList(): 存在するクラスタのリストを取得
    """

    def __init__(self, nodes=None):
        """ ノードリストの初期化
            辞書が引数で渡された場合は, そのデータでノードリストを初期化する
            :param str nodes: クラスタをkey, 値をvalueとする辞書
        """
        self.nodes = defaultdict(list)

        # ディープコピー
        if nodes is not None:
            for item in nodes.items():
                self.nodes[item[0]] = item[1]


    def add(self, value, k=3, cluster=None):
        """ ノードの追加
            最初の学習時にはclusterに値を入れる
            学習後に新たにノードを追加する場合はclusterの値はなし
            :param value: データの値
            :param int k: k近傍で用いるkの値
            :param cluster: クラスタの識別子
            :return: 新たに入れたデータのノード
        """
        if cluster is None:
            cluster = self._checkCluster(value, k)

        self.nodes[cluster].append(value)
        return cluster

    def cluster(self, value, k=3):
        """ 指定したノードのクラスタを調べる
            O(n) nは保持しているデータの数
            :param value: ノードの値
            :param int k: k近傍で用いるkの値
            :return: クラスタの識別子
        """
        for key in self.nodes.keys():
            if value in self.nodes[key]:
                return key

        else:
            return self._checkCluster(value, k)

    def getNodes(self, cluster):
        """ 指定したクラスタのノードのリストを取得
            :param cluster クラスタ
            :return: ノードのリスト
            :rtype: list of [Node.value, ... ]
        """
        if cluster in self.nodes:
            return self.nodes[cluster]
        else:
            return None

    def clusterList(self):
        """
        クラスタのリストを取得
        :return: クラスタのリスト
        """
        return self.nodes.keys()

    def _checkCluster(self, value, k):
        """ 指定された値のノードのクラスタをユークリッド距離によるk近傍法にて求める
            O(n) ただし、nはこれまでに学習したデータ量
            :param value: ノードの値
            :return: ノードが含まれるクラスタ
            :rtype: cluster
        """
        #TODO 探索の計算量を減らす  (近似最近傍探索を使う？)
        dists = []
        for key in self.nodes.keys():
            for node in self.nodes[key]:
                dx = node[0] - value[0]
                dy = node[1] - value[1]
                dists.append((hypot(dx, dy), key))

        dists.sort()
        counter = Counter()
        for i in range(min(k, len(dists))):
            counter[dists[1]] += 1

        most_common = counter.most_common(1)[0]
        cluster = most_common[0][1]
        return cluster
