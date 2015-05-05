__author__ = 'jjzhu'
__doc__ = 'apriori关联分析' \
          '发现频繁项集和发现关联规则' \
          '伪代码：' \
          ''


def load_data_set():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


# 构建大小为1的候选项集的集合
# parm： data_set [[, , , ],[, , , ],[, , , , ,]]类型数据
def create_c1(data_set):
    c1 = []  # 存储候选项集
    for data in data_set:
        for item in data:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    return list(map(frozenset, c1))


# 数据集扫描辅助函数
# param：
#   data_set: 数据集
#   candidate： 候选项集合
#   min_support: 最小支持度
def scan_data(data_set, candidate_set, min_support):
    support_count = {}  # 存储候选项支持度
    for data in data_set:  # 遍历数据集中的所有集合
        for can in candidate_set:  # 遍历候选项集合
            if can.issubset(data):  # 判断候选项集合是否是data的子集
                if can not in support_count:  # 若can不存在候选项支持度字典中
                    support_count[can] = 1
                else:
                    support_count[can] += 1
    items_count = float(len(data_set))  # 集合个数
    return_list = []  # 存储满足条件的集合
    support_data = {}  # 保存所有集合支持率
    for key in support_count:
        support = support_count[key] / items_count  # 计算支持率
        if support >= min_support:
            return_list.insert(0, key)  # 插入到首部（不是必须这么做的）
        support_data[key] = support
    return return_list, support_data


# 构建由k个元素的候选项集合
# param:
#   freq_set: 频繁项集合
#   k: 待构建集合元素个数
def apriori_gen(freq_set, k):
    return_list = []
    len_freq_set = len(freq_set)
    for i in range(len_freq_set):
        for j in range(i + 1, len_freq_set):
            l1 = list(freq_set[i])[: k-2]  # 取前 k-2项
            l2 = list(freq_set[j])[: k-2]
            l1.sort()
            l2.sort()
            if l1 == l2:  # 若前 k-2项相同
                return_list.append(freq_set[i] | freq_set[j])  # 求并集
    return return_list


#
def apriori(data_set, min_support=0.5):
    c1 = create_c1(data_set)  # 创建只有一项的候选项集合
    data_format = list(map(set, data_set))  # 格式化为集合
    l1, support_data = scan_data(data_format, c1, min_support)  # 过滤项数为1的符合最小支持度的候选项
    result_list = [l1]  # 保存候选项
    k = 2
    while len(result_list[k-2]) > 2:
        ck = apriori_gen(result_list[k-2], k)  # 创建项数为K的候选项集合
        lk, support_data_k = scan_data(data_format, ck, min_support)  # 过滤
        support_data.update(support_data_k)  # 更新候选项的支持率
        result_list.append(lk)  # 保存
        k += 1
    return result_list, support_data


# 生成关联规则函数
# param:
#   freq_set: 频繁项集合
#   support_data: 频繁项集合支持率字典
#   min_conf: 最小可信度阀值 默认0.7
def generate_rules(freq_set_list, support_data, min_conf=0.7):
    big_rule_list = []  # 保存关联规则
    for i in range(1, len(freq_set_list)):  # 只读取项数 >= 2 的集合
        for freq_set in freq_set_list[i]:  # 遍历集合中的频繁集
            h1 = [frozenset([item]) for item in freq_set]  # 获取频繁集中项为1的子集
            if i > 1:  # 如果当前频繁集中频繁项的项数>2
                # 进行
                rules_from_conseq(freq_set, h1, support_data, big_rule_list, min_conf)
            else:
                # 计算可信度
                calc_conf(freq_set, h1, support_data, big_rule_list, min_conf)
    return big_rule_list


# 计算可信度，保存符合最小可信度条件的频繁项集合
# param:
#   freq_set: 频繁项集合
#   h: freq_set的含K项元素的子集（非空）
#   support_data: 所有频繁项集合支持率字典
#   brl: 仅存储关键规则列表
#   min_config: 最小支持度，默认0.7
def calc_conf(freq_set, h, support_data, brl, min_conf=0.7):
    pruned_h = []  # 保存规则列表
    for conseq in h:  # 遍历频繁项子集
        # 计算可信度
        # 计算公式
        #   A-->B规则的可信度：
        #   假设{A,B}的支持度为0.6， A的支持度为0.8
        #   则A-->B该条规则的可信度为support{A,B}/support(A)= 0.6/0.8 = 0.75
        conf = support_data[freq_set]/support_data[freq_set-conseq]
        if conf >= min_conf:  # 若当前规则可信度符合最小可信度
            print(freq_set-conseq, '-->', conseq, 'conf:', conf)
            brl.append((freq_set-conseq, conseq, conf))  # 保存关联规则
            pruned_h.append(conseq)  # 保存规则右部分
    return pruned_h


# 生成更多关联规则函数
# param:
#   freq_set: 频繁项集合
#   h: freq_set的含K项元素的子集（非空）
#   support_data: 所有频繁项集合支持率字典
#   brl: 仅存储关键规则列表
#   min_config: 最小支持度，默认0.7
def rules_from_conseq(freq_set, h, support_data, brl, min_conf=0.7):
    m = len(h[0])  # 获取h子集的长度
    if len(freq_set) > (m + 1):  # 判断当前频繁项集合是否可以移除大小为m的子集，
        hmp1 = apriori_gen(h, m+1)  # create Hm+1 new candidates
        hmp1 = calc_conf(freq_set, hmp1, support_data, brl, min_conf)
        if len(hmp1) > 1:   # need at least two sets to merge
            rules_from_conseq(freq_set, hmp1, support_data, brl, min_conf)


def test():
    data_set = load_data_set()
    r, s = apriori(data_set)
    rules = generate_rules(r, s, min_conf=0.5)
    print(rules)
    # c1 = create_c1(data_set)
    # print(c1)
    # d = list(map(set, data_set))
    # l1, support_data0 = scan_data(d, c1, 0.5)
    # print(l1)
    # print(support_data0)

if __name__ == '__main__':
    test()