class KNN:
    """ K近傍法のためのノードを集めた集合
        add: ノードの追加
        cluster: 指定したノードのクラスタの番号を取得
        nodes: 指定したクラスタのノードのリストを取得
    """

    def __init__(self):
        self.nodes = []

    def add(self, value, cluster=None):
        """ ノードの追加"""
        if cluster is None:
            pass

        else:
            pass

    def cluster(self, value):
        """ 指定したノードのクラスタの番号を取得
            :param value ノードの値
        """
        if not value in self.nodes:
            return None

        else
            self._search(value):
            pass

    def nodes(self, cluster):
        """ 指定したクラスタのノードのリストを取得
            :param cluster クラスタ
        """
