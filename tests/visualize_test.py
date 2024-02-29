from src.link import Link

# リンクの作成と節点の追加
link = Link()
link.add_node(0, 0, 'upper')
link.add_node(100, 0, 'lower')
link.add_node(100, 100, 'fixed')
link.set_actuation_point(50, 50)

# リンクの可視化
link.visualize()
