
#读取.net文件
def read_net(network):
    with open('./network/%s/%s_net.txt'%(network, network), 'r') as f1:
        l1 = f1.readlines()
    length=len(l1)
    
    x=0
    while x < length:
        #去除空行
        if l1[x] == '\n':
            del l1[x]
            x -= 1
            length -= 1 
        x += 1
    #以~为截至点，找到所需行数
    for i in range(len(l1)):
        if '~' in l1[i]:
            l1_START_LINE = i+1
            break
    # str modify
    for i in range(5):
        l1[i] = l1[i].split(' ')#以“ ”进行分割
    node_count = eval(l1[1][-1])#点的数量第一行最后一列
    link_count = eval(l1[3][-1])#第三行，最后一列
    for i in range(l1_START_LINE, len(l1)):
        if network == 'bmc':
            l1[i] = l1[i].rstrip('\n')#除去右边的换行符 
            l1[i] = l1[i].rstrip(' ')#除去右边的空格
            l1[i] = l1[i].rstrip(';')#除去分号
            l1[i] = l1[i].replace(' ','')#去空格 
            l1[i] = l1[i].rstrip('\t')#去掉右边的字符
            l1[i] = l1[i].lstrip('\t')#去掉左边的字符
            l1[i] = l1[i].split('\t')#以剩下的制表符作为分割
        else:
            l1[i] = l1[i].rstrip('\n')
            l1[i] = l1[i].rstrip(';')
            l1[i] = l1[i].rstrip('\t')
            l1[i] = l1[i].lstrip('\t')
            l1[i] = l1[i].split('\t')   
    readlist = l1[l1_START_LINE:]#所需行数到最后
    #将行列转化为列表   线段的处理
    for i in range(link_count):#对线段进行循环处理
        for j in range(len(readlist[i])):#在每一行进行列的循环处理 
            readlist[i][j]=eval(readlist[i][j])
    #空字典
    Capacity = {}#容量
    Length = {}#长度
    Fftime = {}#费用
    Innode = {}#起点
    Outnode = {}#终点
    Link = []
    #建立个同点数相当的起终点的空集合
    for i in range(1, node_count+1):
        Innode[i] = []
        Outnode[i] = []
    #读取数，对每一个路段
    for i in range(link_count):
        ii = readlist[i][0]#起点
        jj = readlist[i][1]#终点
        Capacity[(ii, jj)] = readlist[i][2]
        Length[(ii, jj)] = readlist[i][3]
        Fftime[(ii, jj)] = readlist[i][4]/60  ##这里要换一步单位
        # Fftime[(ii, jj)] = readlist[i][4]
        
#不明白，不明白*****************        
        Innode[jj].append(ii)#
        Outnode[ii].append(jj)
#不明白，不明白******************        
        
        Link.append((ii, jj))
    return (Capacity, Length, Fftime, Innode, Outnode, Link, node_count, link_count)

def read_netnoncontinuous(network):
    with open('./network/%s/%s_net.txt' % (network, network), 'r') as f1:
        l1 = f1.readlines()
    # 去除空行
    length = len(l1)

    x = 0
    while x < length:
        if l1[x] == '\n':
            del l1[x]
            x -= 1
            length -= 1
        x += 1
    for i in range(len(l1)):
        if '~' in l1[i]:
            l1_START_LINE = i + 1
            break
    # str modify
    for i in range(5):
        l1[i] = l1[i].split(' ')
    link_count = eval(l1[3][-1])#第三行最后一列变为数字
    for i in range(l1_START_LINE, len(l1)):
        if network == 'bmc':
            l1[i] = l1[i].rstrip('\n')
            l1[i] = l1[i].rstrip(' ')
            l1[i] = l1[i].rstrip(';')
            l1[i] = l1[i].replace(' ', '')
            l1[i] = l1[i].rstrip('\t')
            l1[i] = l1[i].lstrip('\t')
            l1[i] = l1[i].split('\t')
        else:
            l1[i] = l1[i].rstrip('\n')
            l1[i] = l1[i].rstrip(';')
            l1[i] = l1[i].rstrip('\t')
            l1[i] = l1[i].lstrip('\t')
            l1[i] = l1[i].split('\t')
    readlist = l1[l1_START_LINE:]
    for i in range(link_count):
        for j in range(len(readlist[i])):
            readlist[i][j] = eval(readlist[i][j])
    Capacity = {}
    Length = {}
    Fftime = {}
    Innode = {}
    Outnode = {}
    Link = []
    
#这个是啥子*********************
    nodeset = []
#这个是啥子*********************
    
    for i in range(link_count):
        ii = readlist[i][0]
        jj = readlist[i][1]
        nodeset.append(ii)
        nodeset.append(jj)
    nodeset1 = list(set(nodeset))#去掉重复元素，获得点集
    node_count = len(nodeset1)
    for i in nodeset1:
        Innode[i] = []
        Outnode[i] = []
    for i in range(link_count):
        ii = readlist[i][0]
        jj = readlist[i][1]
        Capacity[(ii, jj)] = readlist[i][2]
        Length[(ii, jj)] = readlist[i][3]
        Fftime[(ii, jj)] = readlist[i][4] / 60  ##这里要换一步单位
        # Fftime[(ii, jj)] = readlist[i][4]
#是不是双向的路段=============================
        Innode[jj].append(ii)
        Outnode[ii].append(jj)
#是不是双向的路段=============================
        Link.append((ii, jj))
    return (Capacity, Length, Fftime, Innode, Outnode, Link, node_count, link_count)
#读取.trp文件
def read_trp(network):
    with open('./network/%s/%s_trp.txt'%(network, network), 'r') as f2:
        l2 = f2.readlines()
    length=len(l2)
    x=0
    while x < length:
        if l2[x] == '\n':
            del l2[x]
            x -= 1
            length -= 1
        x += 1
    # str modify
    for i in range(3):
        l2[i] = l2[i].split(' ')
    flow_count = eval(l2[1][-1])
    changelinecount = 0
    changeline=[]

    for i in range(len(l2)):
        if 'Origin' in l2[i]:
            changeline.append(i)
            changelinecount += 1
#不明白具体在做什么====================================
    changelinerolling = changeline[1:]
    changelinerolling.append(len(l2))
#不明白具体在做什么====================================        
    for i,t in zip(changeline,changelinerolling):
        l2[i] = l2[i].rstrip('\n')
        if (network == 'sf') or (network == 'toy') or (network == 'bmc') or (network[0:2] == 'br')or(network == 'hearn')or (network == 'ft')or (network == 'bar'):
            l2[i] = l2[i].replace(' ','')
            l2[i] = l2[i].split('\t')
        elif network == 'cs'or (network == 'cr')or(network == 'an'):
            l2[i] = l2[i].split(' ')
        else:
            print('Check the style of trp file and rectify the code!')
        for j in range(1, t-i):
            l2[i+j] = l2[i+j].rstrip('\n')
            l2[i+j] = l2[i+j].replace(' ','')
            if network == 'bmc':
                l2[i+j] = l2[i+j].replace('\t','')
            l2[i+j] = l2[i+j].rstrip(';')
            l2[i+j] = l2[i+j].split(';')
    #flatten demand
    readlist2=[]
    for i,t in zip(changeline, changelinerolling):
        readlist2.append([l2[i][0],l2[i][-1]])
        ext = []
        for j in range(1,t-i):
            ext.extend(l2[i+j])
        readlist2.append(ext) 
    Demand = {}
    Odtree = {}
    for i in range(0,len(readlist2), 2):#这里没明白2是什么
        o_id = eval(readlist2[i][-1])
        d_id_list = []
        for j in range(len(readlist2[i+1])):
            d_id, demand = eval(readlist2[i+1][j].split(':')[0]),eval(readlist2[i+1][j].split(':')[-1])
            if (d_id != o_id) and (abs(demand-0) > pow(10,-8)):
                d_id_list.append(d_id)
                Demand[(o_id, d_id)]=demand
        Odtree[o_id] = d_id_list
        print(Odtree)
    return (Odtree, Demand, flow_count)

#读取.nod文件
def read_nod(network):
    with open('./network/%s/%s_nod.txt'%(network, network), 'r') as f3:
        l3 = f3.readlines()
    #去除空行
    length=len(l3)
    x=0
    while x < length:
        if l3[x] == '\n':
            del l3[x]
            x -= 1
            length -= 1
        x += 1
    #添加到Node属性
    for i in range(1, len(l3)):
        l3[i] = l3[i].rstrip('\n')
        if (network == 'sf')or(network == 'toy')or(network == 'bmc')or (network[0:2] == 'br')or (network == 'ft')or (network == 'bar'):
            l3[i] = l3[i].rstrip(';')
            l3[i] = l3[i].rstrip('\t')
        l3[i] = l3[i].split('\t')
    readlist3 = l3 #0位置使用题头占用
    for i in range(1,len(readlist3)):
        for j in range(len(readlist3[i])):
            #print(readlist3[i][j])
            readlist3[i][j] = eval(readlist3[i][j])
    Nodeloc = {}
    for i in range(1,len(readlist3)):
        Nodeloc[readlist3[i][0]]=(readlist3[i][1],readlist3[i][2])
    return Nodeloc


#读取.tol文件
def read_tol(network):
    with open('./network/%s/%s_tol.txt'%(network, network), 'r') as f4:
        l4 = f4.readlines()
    length = len(l4)
    for i in range(1,length):
        l4[i] = l4[i].split()
        for j in range(len(l4[i])):
            l4[i][j] = eval(l4[i][j])
    Toll={}
    for i in range(1,len(l4)):
        Toll[(l4[i][0],l4[i][1])] = l4[i][2]
    return Toll

def read_diffmtoll(network, multiple):
    with open('./network/%s/%s_tol_m%s.txt'%(network, network, multiple), 'r') as f4:
        l4 = f4.readlines()
    length = len(l4)
    for i in range(1,length):
        l4[i] = l4[i].split()
        for j in range(len(l4[i])):
            l4[i][j] = eval(l4[i][j])
    Toll={}
    for i in range(1,len(l4)):
        Toll[(l4[i][0],l4[i][1])] = l4[i][2]
    return Toll

# 读取.tb文件
def read_tb(network):
    with open('./network/%s/%s_tb.txt'%(network, network), 'r') as f4:
        l4 = f4.readlines()
    length = len(l4)
    for i in range(2,length):
        l4[i] = l4[i].split()
        for j in range(len(l4[i])):
            l4[i][j] = eval(l4[i][j])
    Tollbound={}
    for i in range(2,len(l4)):
        Tollbound[(l4[i][0],l4[i][1])] = (l4[i][2], l4[i][3])
    return Tollbound

#综合读取
def read(network):
    try:
        Capacity, Length, Fftime, Innode, Outnode, Link, node_count, link_count = read_net(network)
    except:
        Capacity, Length, Fftime, Innode, Outnode, Link, node_count, link_count = read_netnoncontinuous(network)
    Odtree, Demand, flow_count = read_trp(network)
    try:
        Nodeloc = read_nod(network)
    except:
        print('无节点位置文件！')
        Nodeloc = 0
    Toll = read_tol(network)
    return (node_count, link_count, flow_count, Innode, Outnode, Link, Odtree, Nodeloc, Capacity, Length, Fftime, Toll, Demand)

def read_notoll(network):
    Capacity, Length, Fftime, Innode, Outnode, Link, node_count, link_count = read_net(network)
    Odtree, Demand, flow_count = read_trp(network)
    try:
        Nodeloc = read_nod(network)
    except:
        print('无节点位置文件！')
        Nodeloc = 0
    return (node_count, link_count, flow_count, Innode, Outnode, Link, Odtree, Nodeloc, Capacity, Length, Fftime, Demand)

def read_bcp(network):
    Capacity, Length, Fftime, Innode, Outnode, Link, node_count, link_count = read_net(network)
    Odtree, Demand, flow_count = read_trp(network)
    print('before readatollbound')
    try:
        Nodeloc = read_nod(network)
    except:
        print('无节点位置文件！')
        Nodeloc = 0
    Tollbound = read_tb(network)
    return (node_count, link_count, flow_count, Innode, Outnode, Link, Odtree, Nodeloc, Capacity, Length, Fftime, Tollbound, Demand)
    
        
        