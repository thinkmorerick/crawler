# coding:utf-8

import os

import re



# 创建输出目录
try:
    os.mkdir('./output/')
except:
    pass

# 获取文件名称函数
def get_filename(path,filetype):
    import os
    name=[]
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype in i:
                name.append(i.replace(filetype,''))
    return name


# 获取文件名称
fnames=get_filename('txt/','.txt')

# 关键字
customerFlag = ["按欠款方归集的期末余额前五名的其他应收款情况",
                "期末单项金额重大并单项计提坏帐准备的其他应收款",
                "本公司大额应收收款项列示如下",
                "已背书未到期的应收票据",
                "本公司大额其他应收款项列示如下"]
supplierFlag = ["账龄超过 1 年的重要应付账款",
                "账龄超过 1 年的重要其他应付款",
                "账龄超过 3 年的其他应付款明细列示如下",
                "大额其他应付款项性质说明"]

# 提取文本信息函数
def get_txt_info(txtbuffer,flagNum,flag,filePath,fname,wordLength,type):
    # 公司名称集合
    newlist = ['']
    txtbuffer = "\n".join(txtbuffer.split("\n"))
    txtbuffer = txtbuffer[txtbuffer.find(flag):txtbuffer.find(flag) + wordLength]

    # 写入大标题
    keytxt = open("output/" + fname + "/"+filePath+"_" + fname + ".txt", "a")
    keytxt.write("(" + flagNum + "）" + flag + "：\n")
    keytxt.close()

    # 提取公司名称信息
    oldlist = list(txtbuffer.split(' \n'))
    for oli in oldlist:
        if '有限公司' in oli and '年度报告' in oli:
            oldlist.remove(oli)
    for o in oldlist:
        if '：' not in o and '，' not in o:
            if "公司" in o or 'LTD' in o or 'LIMITED' in o or "厂" in o:
                if o != name:
                    newlist.append(o)

    # 格式化处理
    strlist = "\n".join(newlist[1:])

    # 分别写入文件
    txtnew = open("output/" + fname + "/"+type+"_" + fname + ".txt", "a")
    txtnew.write(strlist)
    txtnew.close()
    txtnew = open("output/" + fname + "/"+filePath+"_" + fname + ".txt", "a")
    txtnew.write(strlist + "\t\n")
    txtnew.close()
    pass

# 提取数字信息函数
def get_digit_info(txtbuffer,flagNum,flag,filePath,fname,wordLength,type):
    # 公司数据集合
    newlist = ['']
    txtbuffer = "\n".join(txtbuffer.split("\n"))
    txtbuffer = txtbuffer[txtbuffer.find(flag):txtbuffer.find(flag) + wordLength]

    # 写入大标题
    keytxt = open("output/" + fname + "/" + filePath + "_" + fname + ".txt", "a")
    # keytxt.write("(" + flagNum + "）" + flag + "：\n")
    keytxt.close()

    # 提取公司数据信息
    oldlist = list(txtbuffer.split(' '))
    for nn in oldlist:
        if ',' in nn:
            nn = nn.replace(',','')
            nn = re.sub(r"^\d*\.$\d*","",nn)
            nn = " ".join(nn.split(" \n")).strip()
            nn = " ".join(nn.split("  \n")).strip()
            nn = " ".join(nn.split("\n")).strip()
            nn = " ".join(nn.split("\t")).strip()
            nn = " ".join(nn.split("\t")).strip()
            nn = " ".join(nn.split("  ")).strip()
            nn = " ".join(nn.split("   ")).strip()
            nn = " ".join(nn.split("\v")).strip()
            nn = " ".join(nn.split("\r")).strip()
            nn = " ".join(nn.split("\f")).strip()
            if "." in nn:
                newlist.append(nn)

    # 格式化处理
    strlist = "\n".join(newlist[1:])

    # 写入文件
    txtnew = open("output/" + fname + "/"+filePath+"_" + fname + ".txt", "a")
    txtnew.write(strlist + "\t\n")
    txtnew.close()
    pass

# 遍历信息
for fname in fnames:
    # 创建子目录
    try:
        os.mkdir('./output/'+fname)
    except:
        pass
    # 打开待读取文件
    TXTtemp = open("txt/"+fname+".txt","r+")
    txtbuffer=TXTtemp.read()
    # 写入初次转换文本
    original=open("./output/"+fname+"/"+"original_"+fname+".txt","w")
    original.write(txtbuffer)
    original.close()
    TXTtemp.close()

    # 格式化处理
    listname=list(txtbuffer.split('\n'))
    # 提取股票代码
    sharenum = ''
    for s in listname:
        if '股票代码' in s and listname[listname.index(s) + 1].isdigit() and len(listname[listname.index(s) + 1])==6:
            sharenum = listname[listname.index(s) + 1]
        elif '股票代码 ' in s and listname[listname.index(s) + 2].strip().isdigit() and len(listname[listname.index(s) + 2].strip())==6:
            sharenum = listname[listname.index(s) + 2].strip()
        elif '股代码' in s and re.sub("\D", "", listname[listname.index(s)]).isdigit() and len(re.sub("\D", "", listname[listname.index(s)]))==6:
            sharenum = re.sub("\D", "", listname[listname.index(s)])
        elif '目录' in s and listname[listname.index(s) - 1].isdigit() and len(listname[listname.index(s) + 1])==6:
            sharenum = listname[listname.index(s) - 1]
        elif '目录 ' in s and re.sub("\D", "", listname[listname.index(s) - 2]).isdigit() and len((re.sub("\D", "", listname[listname.index(s) - 2]))[4:10])==6:
            sharenum = (re.sub("\D", "", listname[listname.index(s) - 2]))[4:10]
        elif '公司代码' in s and re.sub("\D", "", listname[listname.index(s)]).isdigit() and len(re.sub("\D", "", listname[listname.index(s)]))==6:
            sharenum = re.sub("\D", "", listname[listname.index(s)])
    # 写入股票代码信息
    sharenumtxt = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    sharenumtxt.write("1 股票代码：" + sharenum + "\n")
    sharenumtxt.close()

    # 提取公司名称信息
    namearea = listname[:30]
    name = ''
    for n in namearea:
        if '有限公司' in n:
            name = n.strip().split(" ")[0]
        elif '有 限 公 司' in n:
            name = "".join(n.strip().split())
    # 写入公司名称信息
    txtname = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtname.write("2 公司名称：" + str(name) + "\n")
    txtname.close()

    # 提取客户信息
    txtname = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtname.write("3 客户：" + "\n")
    txtname.close()
    for i in range(5):
        get_txt_info(txtbuffer, str(i+1) , customerFlag[i], "keywords", fname, 500, "customer")
        get_digit_info(txtbuffer, str(i+1) , customerFlag[i], "keywords", fname, 500, "customer")
    txtname = open("output/" + fname + "/keywords_" + fname + ".txt", "a")

    # 提取供应商信息
    txtname.write("4 供应商：" + "\n")
    # txtname.write(str(namearea) + "\n")
    txtname.close()
    for i in range(4):
        get_txt_info(txtbuffer, str(i+1) , supplierFlag[i], "keywords", fname, 500, "supplier")
        get_digit_info(txtbuffer, str(i+1) , supplierFlag[i], "keywords", fname, 500, "supplier")
