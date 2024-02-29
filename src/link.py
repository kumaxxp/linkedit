# src/link.py
import matplotlib.pyplot as plt
import math

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
        self.connected_links = []  # Initialize the connected_links list

    def add_node(self, x, y, node_type):
        """節点をリンクに追加する"""
        self.nodes.append(Node(x, y, node_type))

    def set_actuation_point(self, x, y):
        """作用点を設定する"""
        self.actuation_point = (x, y)

    def __repr__(self):
        return f"Link(Nodes: {self.nodes}, Actuation Point: {self.actuation_point})"

    def calculate_distance(self, node1_index, node2_index):
        """指定された2つの節点間の距離を計算する"""
        node1 = self.nodes[node1_index]
        node2 = self.nodes[node2_index]
        return ((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2) ** 0.5

    def visualize(self):
        """リンクの可視化"""
        fig, ax = plt.subplots()
        # 節点の描画
        for node in self.nodes:
            ax.plot(node.x, node.y, 'o')  # 節点をプロット
        # 節点間の接続を描画
        for i in range(len(self.nodes) - 1):
            ax.plot([self.nodes[i].x, self.nodes[i + 1].x], 
                    [self.nodes[i].y, self.nodes[i + 1].y], 'k-')
        # 作用点の描画（存在する場合）
        if self.actuation_point:
            ax.plot(self.actuation_point[0], self.actuation_point[1], 'rx')  # 作用点をプロット
        plt.axis('equal')
        plt.show()

    def rotate(self, angle, pivot_node_index=0):
        """リンクを回転させる。pivot_node_indexで指定された節点が回転の中心となる。"""
        pivot = self.nodes[pivot_node_index]
        rad_angle = math.radians(angle)
        cos_angle = math.cos(rad_angle)
        sin_angle = math.sin(rad_angle)

        for node in self.nodes:
            if node != pivot:
                # pivotを中心とした回転
                relative_x = node.x - pivot.x
                relative_y = node.y - pivot.y
                rotated_x = relative_x * cos_angle - relative_y * sin_angle
                rotated_y = relative_x * sin_angle + relative_y * cos_angle
                node.x = rotated_x + pivot.x
                node.y = rotated_y + pivot.y

    def apply_force(self, force, node_index):
        """指定された節点に力を適用する。"""
        # 力のベクトルを適用するための基本的な物理法則の実装
        # この例では、単純化のために力を直接節点の位置に加算しています
        self.nodes[node_index].x += force[0]
        self.nodes[node_index].y += force[1]

    def add_connection(self, other_link, node_index, other_node_index):
        """このリンクの節点を他のリンクの節点に接続する。"""
        self.connected_links.append((other_link, node_index, other_node_index))
        # 接続点の位置の更新や、力の伝達などの処理が必要

        


