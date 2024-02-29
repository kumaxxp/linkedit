# src/link.py

class Node:
    def __init__(self, x, y, node_type):
        self.x = x  # X座標 (mm)
        self.y = y  # Y座標 (mm)
        self.node_type = node_type  # 節のタイプ: 'power', 'upper', 'lower', 'fixed'

    def __repr__(self):
        return f"Node({self.x}, {self.y}, '{self.node_type}')"

class Link:
    def __init__(self):
        self.nodes = []  # このリンクの節点
        self.actuation_point = None  # 作用点

    def add_node(self, x, y, node_type):
        """節点をリンクに追加する"""
        self.nodes.append(Node(x, y, node_type))

    def set_actuation_point(self, x, y):
        """作用点を設定する"""
        self.actuation_point = (x, y)

    def __repr__(self):
        return f"Link(Nodes: {self.nodes}, Actuation Point: {self.actuation_point})"
