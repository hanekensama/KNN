from collections import Counter
from  math import hypot


class KNN:
    """ K近傍法のためのノードを集めた集合
        add(): ノードの追加
        cluster(): 指定したノードのクラスタの番号を取得
        dataList(): 指定したクラスタのノードのリストを取得
        dict(): 保持しているデータとそのクラスタを辞書型のデータ構造にまとめる
    """

    def __init__(self, json=None):
        """ ノードリストの初期化
            json文字列が引数で渡された場合は, そのデータでノードリストを初期化する
            json文字列が渡されなかった場合は, ノードリストは空のリストとする
            :param str json: jsonの文字列
        """
        if json is None:
            self.nodes = []

        # TODO 実装
        else:
            self.nodes = []

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

        self.nodes.append((value, cluster))
        return cluster

    def cluster(self, value, k=3):
        """ 指定したノードのクラスタを調べる
            :param value: ノードの値
            :param int k: k近傍で用いるkの値
            :return: クラスタの識別子
        """
        if value in self.nodes:
            return self._search(value)[1]

        else:
            return self._checkCluster(value, k)

    def getNodes(self, cluster):
        """ 指定したクラスタのノードのリストを取得
            :param cluster クラスタ
            :return: ノードのリスト
            :rtype: list of [Node.value, ... ]
        """
        list = []

        for node in self.nodes:
            if node[1] == cluster:
                list.append(node[0])

        return list

    def dict(self):
        """ 保持しているデータとそのクラスタを辞書型のデータ構造にまとめる
        :return: 辞書データ
        :rtype:dict{"node":["data":data, "cluster":cluster]}
        """
        # TODO 実装
        pass

    def _search(self, value):
        """ 指定された値のノードを探索する
            O(n) ただし、nはこれまでに学習したデータ量
            :param value: ノードの値
            :return: ノードが見つかった場合はそのノード、見つからなければNone
            :rtype: tuple of (value, cluster) or None
        """
        # TODO 探索の計算量を減らす.
        for node in self.nodes:
            if node[0] == value:
                return node

        return None

    def _checkCluster(self, value, k):
        """ 指定された値のノードのクラスタをユークリッド距離によるk近傍法にて求める
            O(n) ただし、nはこれまでに学習したデータ量
            :param value: ノードの値
            :return: ノードが含まれるクラスタ
            :rtype: cluster
        """
        #TODO 探索の計算量を減らす  (近似最近傍探索を使う？)
        dists = []
        for node in self.nodes:
            dx = node[0][0] - value[0]
            dy = node[0][1] - value[1]
            dists.append((hypot(dx, dy), node[1]))

        dists.sort()
        counter = Counter()
        for i in range(min(k, len(dists))):
            counter[dists[1]] += 1

        most_common = counter.most_common(1)[0]
        cluster = most_common[0][1]
        return cluster
