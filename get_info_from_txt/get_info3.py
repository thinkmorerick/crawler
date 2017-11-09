# coding:utf-8

import os

import re

try:
    os.mkdir('./output/')
except:
    pass

def get_filename(path,filetype):
    import os
    name=[]
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype in i:
                name.append(i.replace(filetype,''))
    return name

fnames=get_filename('txt/','.txt')
customerFlag = ["按欠款方归集的期末余额前五名的其他应收款情况",
                "期末单项金额重大并单项计提坏帐准备的其他应收款",
                "本公司大额应收收款项列示如下",
                "已背书未到期的应收票据",
                "本公司大额其他应收款项列示如下"]
supplierFlag = ["账龄超过 1 年的重要应付账款",
                "账龄超过 1 年的重要其他应付款",
                "账龄超过 3 年的其他应付款明细列示如下",
                "大额其他应付款项性质说明"]

def get_info(txtbuffer,flagNum,flag,filePath,fname,wordLength,type):
    newlist1 = ['']
    newlist2 = ['']
    txtbuffer = txtbuffer[txtbuffer.find(flag):txtbuffer.find(flag) + wordLength]
    keytxt = open("output/" + fname + "/"+filePath+"_" + fname + ".txt", "a")
    keytxt.write("（" + flagNum + "）" + flag + "：\n")
    # keytxt.write(str(txtbuffer) + "\n")
    keytxt.close()
    oldlist = list(txtbuffer.split(' '))
    for o in oldlist:
        if '：' not in o:
            if "公司" in o or 'LTD' in o or 'LIMITED' in o or "厂" in o:
                if o != name:
                    newlist1.append(o)
    for n in oldlist:
        if ',' in n:
            newlist2.append(n)

    strlist1 = "\n".join(newlist1)
    strlist1 = strlist1[1:]
    strlist2 = "\n".join(newlist2)
    strlist2 = strlist2[1:]

    txtnew = open("output/" + fname + "/"+type+"_" + fname + ".txt", "a")
    txtnew.write(strlist1)
    txtnew.close()
    txtnew = open("output/" + fname + "/"+filePath+"_" + fname + ".txt", "a")
    txtnew.write(strlist1 + "\t\n")
    txtnew.write(strlist2 + "\t\n")
    txtnew.close()
    pass

for fname in fnames:
    try:
        os.mkdir('./output/'+fname)
    except:
        pass
    TXTtemp = open("txt/"+fname+".txt","r+")

    txtbuffer=TXTtemp.read().strip()
    original=open("./output/"+fname+"/"+"original_"+fname+".txt","w")
    original.write(txtbuffer)
    original.close()

    txtbuffer=" ".join(txtbuffer.split())
    txtbuffer=txtbuffer[:-1].strip()
    second=open("./output/"+fname+"/second_"+fname+".txt","w")
    second.write(txtbuffer)
    second.close()

    listname=list(txtbuffer.split(' '))
    sharenum = ''
    for s in listname:
        if '股票代码' in s and listname[listname.index(s) + 1].isdigit() and len(listname[listname.index(s) + 1])==6:
            sharenum = listname[listname.index(s) + 1]
        elif '股代码' in s and re.sub("\D", "", listname[listname.index(s)]).isdigit() and len(re.sub("\D", "", listname[listname.index(s)]))==6:
            sharenum = re.sub("\D", "", listname[listname.index(s)])
        elif '目录' in s and listname[listname.index(s) - 1].isdigit() and len(listname[listname.index(s) + 1])==6:
            sharenum = listname[listname.index(s) - 1]
        elif '公司代码' in s and re.sub("\D", "", listname[listname.index(s)]).isdigit() and len(re.sub("\D", "", listname[listname.index(s)]))==6:
            sharenum = re.sub("\D", "", listname[listname.index(s)])
    sharenumtxt = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    sharenumtxt.write("1 股票代码：" + sharenum + "\n")
    sharenumtxt.close()
    namearea = listname[:30]
    name = ''
    for n in namearea:
        if '有限公司' in n:
            name = n

    txtname = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtname.write("2 公司名称：" + str(name) + "\n")
    # txtname.write(str(namearea) + "\n")
    txtname.close()

    txtname = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtname.write("3 客户：" + "\n")
    # txtname.write(str(namearea) + "\n")
    txtname.close()
    for i in range(5):
        get_info(txtbuffer, str(i+1) , customerFlag[i], "keywords", fname, 500, "customer")
    txtname = open("output/" + fname + "/keywords_" + fname + ".txt", "a")

    txtname.write("4 供应商：" + "\n")
    # txtname.write(str(namearea) + "\n")
    txtname.close()
    for i in range(4):
        get_info(txtbuffer, str(i+1) , supplierFlag[i], "keywords", fname, 500, "supplier")

    TXTtemp.close()