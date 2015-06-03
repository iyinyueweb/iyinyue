__author__ = 'jjzhu'
from pylab import *

decision_node = dict(boxstyle='sawtooth', fc='0.8')
leaf_node = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='-', connectionstyle="arc3,rad=.2")
arrow_args2 = dict(arrowstyle='->',  connectionstyle="arc3,rad=.2")
color_list = ['red', 'blue', 'yellow', 'cyan', 'magenta', 'darkolivegreen']


def plot_node(curr_node, center_location, parent_location, arrow_args=arrow_args):
    annotate(curr_node.name+':'+str(curr_node.count), xy=parent_location, xytext=center_location,
             va='center', ha='center',
             bbox=leaf_node, arrowprops=arrow_args)


def plot_header(text_str, center_location, parent_location, arrow_args=arrow_args):
    annotate(text_str, xy=parent_location, xytext=center_location,
             va='center', ha='center',
             bbox=leaf_node, arrowprops=arrow_args)


def plot_mid_text(center, parent_location, text_str):
    x_mid = (parent_location[0]-center[0])/2.0 + center[0]
    y_mid = (parent_location[1]-center[1])/2.0 + center[1]
    text(x_mid, y_mid, text_str)


def plot_tree(in_tree, parent_location, width, height, node_location):
    num_leafs = get_num_leafs(in_tree)
    depths = get_depth(in_tree)
    xoff = (width[1]-width[0])/num_leafs
    curr_location = (width[0]+((width[1]-width[0])/2.0), height)
    plot_node(in_tree, curr_location, parent_location)
    node_location[in_tree] = curr_location
    # plot_tree.yoff -= 1.0/plot_tree.height
    child_leafs = {}
    for child in in_tree.children.values():
        child_leafs[child] = get_num_leafs(child)
    used = 0
    for child, num in child_leafs.items():
        if num == 0:
            plot_node(child, (width[0]+used, width[0]+used + xoff), curr_location)
            node_location[child] = (width[0]+used, width[0]+used + xoff)
            used += xoff
        else:
            plot_tree(child, curr_location, [width[0]+used, width[0]+used + xoff*num],
                      curr_location[1]-plot_tree.yoff, node_location)
            used += xoff*num
    # for child in in_tree.children.values():
    #     if child.children.__len__ != 0:
    #
    #         plot_tree(child, curr_location, str(child.name))
    #     else:
    #         plot_tree.xoff += 1.0/plot_tree.width
    #         plot_node(child, (plot_tree.xoff, plot_tree.yoff), curr_location)
    #
    # plot_tree.yoff += 1.0/plot_tree.height


def create_plot(in_tree, table):
    figure(2, facecolor='white').clf()
    axprops = dict(xticks=[], yticks=[])
    create_plot.ax1 = subplot(111, frameon=False, **axprops)
    plot_tree.width = float(get_num_leafs(in_tree))
    plot_tree.used = 0
    plot_tree.height = float(get_depth(in_tree))
    plot_tree.xoff = -0.5/plot_tree.width
    plot_tree.yoff = 1.0/plot_tree.height
    node_location = {}
    plot_tree(in_tree, (0.5, 1.0), [0.0, 0.8], 1.0, node_location)
    show()
    # figure(2, facecolor='white').clf()
    # axprops = dict(xticks=[], yticks=[])
    # create_plot.ax1 = subplot(111, frameon=False, **axprops)
    # plot_tree.width = float(get_num_leafs(in_tree))
    # plot_tree.used = 0
    # plot_tree.height = float(get_depth(in_tree))
    # plot_tree.xoff = -0.5/plot_tree.width
    # plot_tree.yoff = 1.0/plot_tree.height
    # node_location = {}
    # plot_tree(in_tree, (0.5, 1.0), [0.0, 0.8], 1.0, node_location)
    # i = 0
    # print(node_location.__len__())
    # for item, linked in table.items():
    #     arrow_args2['color'] = color_list[i]
    #     plot_header(linked[1].name+":"+str(linked[0]), (0.9, 1-(i*1.0/table.__len__())),
    #                 node_location[linked[1]], arrow_args=arrow_args2)
    #     curr_node = linked[1]
    #     while curr_node.node_link is not None:
    #         plot_header('', node_location[curr_node],
    #                     node_location[curr_node.node_link], arrow_args=arrow_args2)
    #         curr_node = curr_node.node_link
    #     i += 1
    # # for node, location in node_location.items():
    # #     plot_node(node, (0.1, 1-(i*1.0/12)), (0.1, 1-(i*1.0/12)))
    # #     i += 1
    # show()
    # figure(2, facecolor='white').clf()
    # axprops = dict(xticks=[], yticks=[])
    # create_plot.ax1 = subplot(111, frameon=False, **axprops)
    # plot_tree.width = float(get_num_leafs(in_tree))
    # plot_tree.used = 0
    # plot_tree.height = float(get_depth(in_tree))
    # plot_tree.xoff = -0.5/plot_tree.width
    # plot_tree.yoff = 1.0/plot_tree.height
    # node_location = {}
    # plot_tree(in_tree, (0.5, 1.0), [0.2, 1.0], 1.0, node_location)
    # i = 0
    # print(node_location.__len__())
    # for item, linked in table.items():
    #     arrow_args2['color'] = color_list[i]
    #     plot_header(linked[1].name+":"+str(linked[0]), (0.1, 1-(i*1.0/table.__len__())),
    #                 node_location[linked[1]], arrow_args=arrow_args2)
    #     curr_node = linked[1]
    #     while curr_node.node_link is not None:
    #         plot_header('', node_location[curr_node],
    #                     node_location[curr_node.node_link], arrow_args=arrow_args2)
    #         curr_node = curr_node.node_link
    #     i += 1
    # show()


def get_num_leafs(in_tree):
    num_leafs = in_tree.children.__len__()
    if num_leafs < 1:
        return 1
    for child in in_tree.children.values():
        num_leafs += get_num_leafs(child)-1
    return num_leafs


def get_depth(in_tree):
    max_depth = 0
    for child in in_tree.children.values():
        if child.children.__len__() == 0:
            curr_depth = 1
        else:
            curr_depth = 1 + get_depth(child)
        if curr_depth > max_depth:
            max_depth = curr_depth
    return max_depth


# FP树节点类
class TreeNode:
    __doc__ = '树节点数据结构\n' \
              'name: 对应元素\n' \
              'count:当前元素的支持度(int)\n' \
              'node_link: 相似元素节点(TreeNode)\n' \
              'parent_node: 父节点(TreeNode)\n' \
              'children:子节点(dict)\n '

    def __init__(self, name, num_occur, parent_node):
        self.name = name
        self.count = num_occur
        self.node_link = None
        self.parent = parent_node
        self.children = {}

    def increase(self, num_occur):
        self.count += num_occur

    def display(self, ind=1):
        print('--'*ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.display(ind+1)


def create_tree(data_set, min_support=1):
    header_table = {}
    for trans in data_set:  # 统计单个元素的出现次数
        for item in trans:
            header_table[item] = header_table.get(item, 0) + data_set[trans]
    delete_keys = []  # 存储支持度小于min_support条件的待删除的key
    for k in header_table.keys():
        if header_table[k] < min_support:
            delete_keys.append(k)
    for k in delete_keys:
        del(header_table[k])  # 删除不满足条件的元素
    freq_item_set = set(header_table.keys())  # key集合
    if len(freq_item_set) == 0:  # 没有符合条件的元素项
        return None, None  # 直接返回
    # 初始化， [count, treeNode]，
    # 数组[0]存储元素支持度，[1]存储的是一个树节点
    for k in header_table:
        header_table[k] = [header_table[k], None]
    return_tree = TreeNode('null set', 1, None)  # 创建一个只有根节点的树
    for tran_set, count in data_set.items():  # 遍历数据中的所有元素集
        local_dict = {}  # 存储元素集中的元素
        for item in tran_set:  # 遍历元素集中的元素
            # 判断元素集中的元素是否符合条件集合中，即支持度大于最小支持度
            if item in freq_item_set:
                local_dict[item] = header_table[item][0]  # 获取当前元素的支持度
        if len(local_dict) > 0:  # 非空
            # 按照支持度大小降序排序
            ordered_items = [v[0] for v in sorted(
                local_dict.items(), key=lambda p:p[1], reverse=True)]
            update_tree(ordered_items, return_tree, header_table, count)  # 更新树
    return return_tree, header_table


# 树的更新函数,（递归）
# params
#   items: 待更新的元素集
#   in_tree: 待更新的目标树
#   header_table: 头指针表
#   count: 待更新元素集支持度
def update_tree(items, in_tree, header_table, count):
    if items[0] in in_tree.children:  # 如果待更新元素集合的第一项已经是树节点
        in_tree.children[items[0]].increase(count)   # 更新支持度
    else:  # 若不是
        in_tree.children[items[0]] = TreeNode(items[0], count, in_tree)  # 新建节点
        if header_table[items[0]][1] is None:  # 如果头指针表中对应节点的指针为空
            # 则将该元素的对应节点指针指向当前节点
            header_table[items[0]][1] = in_tree.children[items[0]]
        else:  # 否则
            update_header(header_table[items[0]][1],
                          in_tree.children[items[0]])  # 更新头指针表
    if len(items) > 1:  # 若待更新元素集元素>1
        # 则截取1 - len(items) 元素 ， 递归调用树更新函数
        update_tree(items[1::], in_tree.children[items[0]], header_table, count)


# 更新头指针表函数
# param:
#   node_to_test: 待更新的头指针对应的节点
#   target_node: 目标节点
def update_header(node_to_test, target_node):
    while node_to_test.node_link is not None:  # 找到末尾节点
        node_to_test = node_to_test.node_link
    node_to_test.node_link = target_node  # 插入目标节点


# 上溯遍历整棵树
# param:
#   leaf_node: 遍历的起始节点
#   prefix_path: 遍历的路径列表，存储元素名
def ascend_tree(leaf_node, prefix_path):
    if leaf_node.parent is not None:
        prefix_path.append(leaf_node.name)
        ascend_tree(leaf_node.parent, prefix_path)


# 生成给定元素的前缀路径
# param:
#   tree_node: 给定元素树节点，来自与头指针列表中存储的节点！！！
def find_prefix_path(tree_node):
    condition_patterns = {}  # 存储条件模式基
    while tree_node is not None:
        prefix_path = []
        ascend_tree(tree_node, prefix_path)  # 获取上溯路径
        if len(prefix_path) > 1:  # 路径非空
            # 记录模式基
            condition_patterns[frozenset(prefix_path[1:])] = tree_node.count  
        tree_node = tree_node.node_link
    return condition_patterns

# 递归创建条件树，查找频繁项集
def mine_tree(in_tree, header_table, min_support, prefix, freq_item_list):
    ordered_items = [item[0] for item in sorted(header_table.items(),
                                                key=lambda p:p[0])]  # 升序
    for item in ordered_items:
        new_freq_set = prefix.copy()
        new_freq_set.add(item)
        freq_item_list.append(new_freq_set)
        condition_pattern_bases = find_prefix_path(header_table[item][1])
        condition_tree, head = create_tree(condition_pattern_bases, min_support)
        if head is not None:
            # create_plot(condition_tree, None)
            mine_tree(condition_tree, head, min_support, new_freq_set, freq_item_list)


def load_simple_data():
    simple_data = [['r', 'z', 'h', 'j', 'p'],
                   ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
                   ['z'],
                   ['r', 'x', 'n', 'o', 's'],
                   ['y', 'r', 'x', 'z', 'q', 't', 'p'],
                   ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simple_data


def create_init_set(data_set):
    return_dict = {}
    for trans in data_set:
        return_dict[frozenset(trans)] = 1
    return return_dict


def fp_growth(user, data):
    all_data = []
    for u, p in data.items():
        temp = []
        for m in p:
            temp.append(m.id)
        all_data.append(temp)

    init_set = create_init_set(all_data)
    tree, table = create_tree(init_set, 3)
    freq_item = []
    mine_tree(tree, table, 3, set([]), freq_item)
    return freq_item


def test():
    simple_data = load_simple_data()
    init_set = create_init_set(simple_data)
    return init_set

if __name__ == '__main__':
    init_set = test()
    tree, table = create_tree(init_set, 3)
    freq_item = []
    mine_tree(tree, table, 3, set([]), freq_item)
    print(table)
    print(freq_item)
    create_plot(tree, table)
    tree.display()