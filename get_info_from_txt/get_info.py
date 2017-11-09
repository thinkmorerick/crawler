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

    oldlist=['']
    newlist=['']
    flag1="按欠款方归集的期末余额前五名的其他应收款情况"
    txtbuffer1=txtbuffer[txtbuffer.find(flag1):txtbuffer.find(flag1)+500]
    keytxt1 = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    keytxt1.write("3 客户：\n")
    keytxt1.write("（1）"+flag1+"：\n")
    keytxt1.write(str(txtbuffer1) + "\n")
    keytxt1.close()

    oldlist=list(txtbuffer1.split(' '))
    for o in oldlist:
        if "公司" in o:
            if o!=name:
                newlist.append(o)

    newlist=list(set(newlist))
    strlist="\n".join(newlist)
    strlist=strlist[1:]

    txtnew=open("output/"+fname+"/customer_"+fname+".txt","a")
    txtnew.write(strlist)
    txtnew.close()
    txtnew = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtnew.write(strlist + "\n")
    txtnew.close()

    oldlist=['']
    newlist=['']
    flag11="期末单项金额重大并单项计提坏帐准备的其他应收款"
    txtbuffer11=txtbuffer[txtbuffer.find(flag11):txtbuffer.find(flag11)+200]
    keytxt11 = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    keytxt11.write("（2）"+flag11+"：\n")
    keytxt11.write(str(txtbuffer11) + "\n")
    keytxt11.close()
    oldlist=list(txtbuffer11.split(' '))

    for o in oldlist:
        if "公司" in o:
            if o!=name:
                newlist.append(o)

    newlist=list(set(newlist))
    strlist="\n".join(newlist)
    strlist = strlist[1:]

    txtnew=open("output/"+fname+"/customer_"+fname+".txt","a")
    txtnew.write(strlist)
    txtnew.close()
    txtnew = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtnew.write(strlist + "\n")
    txtnew.close()


    oldlist=['']
    newlist1=['']
    newlist2=['']
    flag12="本公司大额应收收款项列示如下"
    txtbuffer12=txtbuffer[txtbuffer.find(flag12):txtbuffer.find(flag12)+200]
    keytxt12 = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    keytxt12.write("（3）"+flag12+"：\n")
    keytxt12.write(str(txtbuffer12) + "\n")
    keytxt12.close()
    oldlist=list(txtbuffer12.split(' '))
    for o in oldlist:
        if "：" not in o:
            if "公司" in o or 'LTD' in o or 'LIMITED' in o:
                if o!=name:
                    newlist1.append(o)

    for n in oldlist:
        if "," in n:
            newlist2.append(n)

    # newlist=list(set(newlist))
    strlist1="\n".join(newlist1)
    strlist1 = strlist1[1:]
    strlist2="\n".join(newlist2)
    strlist2 = strlist2[1:]
    txtnew=open("output/"+fname+"/customer_"+fname+".txt","a")
    txtnew.write(strlist1)
    txtnew.close()

    txtnew=open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtnew.write(strlist1 + "\n")
    txtnew.write(strlist2 + "\n")
    txtnew.close()

    oldlist=['']
    newlist=['']
    flag13="已背书未到期的应收票据"
    txtbuffer13=txtbuffer[txtbuffer.find(flag13):txtbuffer.find(flag13)+200]
    keytxt13 = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    keytxt13.write("（4）"+flag13+"：\n")
    keytxt13.write(str(txtbuffer13) + "\n")
    keytxt13.close()
    oldlist=list(txtbuffer13.split(' '))

    for o in oldlist:
        if "公司" in o or 'LTD' in o or 'LIMITED' in o:
            if o!=name:
                newlist.append(o)

    # newlist=list(set(newlist))
    strlist="\n".join(newlist)
    strlist = strlist[1:]

    txtnew=open("output/"+fname+"/customer_"+fname+".txt","a")
    txtnew.write(strlist)
    txtnew.close()
    txtnew = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtnew.write(strlist + "\n")
    txtnew.close()

    oldlist=['']
    newlist1=['']
    newlist2=['']
    flag14="本公司大额其他应收款项列示如下"
    txtbuffer14=txtbuffer[txtbuffer.find(flag14):txtbuffer.find(flag14)+200]
    keytxt14 = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    keytxt14.write("（5）"+flag14+"：\n")
    keytxt14.write(str(txtbuffer14) + "\n")
    keytxt14.close()
    oldlist=list(txtbuffer14.split(' '))
    for o in oldlist:
        if '：' not in o:
            if "公司" in o or 'LTD' in o or 'LIMITED' in o or "厂" in o:
                if o!=name:
                    newlist1.append(o)
    for n in oldlist:
        if ',' in n:
            newlist2.append(n)

    # newlist=list(set(newlist))
    strlist1="\n".join(newlist1)
    strlist1 = strlist1[1:]
    strlist2 = "\n".join(newlist2)
    strlist2 = strlist2[1:]

    txtnew=open("output/"+fname+"/customer_"+fname+".txt","a")
    txtnew.write(strlist1)
    txtnew.close()
    txtnew = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtnew.write(strlist1 + "\t\n")
    txtnew.write(strlist2 + "\t\n")
    txtnew.close()


    oldlist=['']
    newlist=['']
    flag2="账龄超过 1 年的重要应付账款"
    txtbuffer2=txtbuffer[txtbuffer.find(flag2):txtbuffer.find(flag2)+300]
    keytxt2 = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    keytxt2.write("4 供应商：\n")
    keytxt2.write("（1）"+flag2+"：\n")
    keytxt2.write(str(txtbuffer2) + "\n")
    keytxt2.close()
    oldlist=list(txtbuffer2.split(' '))
    for o in oldlist:
        if "公司" in o:
            if o!=name:
                newlist.append(o)

    newlist=list(set(newlist))
    strlist="\n".join(newlist)
    strlist = strlist[1:]

    txtnew=open("output/"+fname+"/supplier_"+fname+".txt","a")
    txtnew.write(strlist)
    txtnew.close()
    txtnew = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtnew.write(strlist + "\n")
    txtnew.close()

    oldlist=['']
    newlist=['']
    flag21="账龄超过 1 年的重要其他应付款"
    txtbuffer21=txtbuffer[txtbuffer.find(flag21):txtbuffer.find(flag21)+400]
    keytxt21 = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    keytxt21.write("（2）"+flag21+"：\n")
    keytxt21.write(str(txtbuffer21) + "\n")
    keytxt21.close()
    oldlist=list(txtbuffer21.split(' '))
    for o in oldlist:
        if "公司" in o:
            if o!=name:
                newlist.append(o)

    newlist=list(set(newlist))
    strlist="\n".join(newlist)
    strlist = strlist[1:]

    txtnew=open("output/"+fname+"/supplier_"+fname+".txt","a")
    txtnew.write(strlist)
    txtnew.close()
    txtnew = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtnew.write(strlist + "\n")
    txtnew.close()

    oldlist=['']
    newlist1=['']
    newlist2=['']
    flag22="账龄超过 3 年的其他应付款明细列示如下"
    txtbuffer22=txtbuffer[txtbuffer.find(flag22):txtbuffer.find(flag22)+400]
    keytxt22 = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    keytxt22.write("（3）"+flag22+"：\n")
    keytxt22.write(str(txtbuffer22) + "\n")
    keytxt22.close()
    oldlist=list(txtbuffer22.split(' '))
    for o in oldlist:
        if "公司" in o:
            if o!=name:
                newlist1.append(o)
    for n in oldlist:
        if "," in n:
            newlist2.append(n)
    # newlist=list(set(newlist))
    strlist1="\n".join(newlist1)
    strlist1 = strlist1[1:]
    strlist2="\n".join(newlist2)
    strlist2 = strlist2[1:]

    txtnew=open("output/"+fname+"/supplier_"+fname+".txt","a")
    txtnew.write(strlist1)
    txtnew.close()
    txtnew = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtnew.write(strlist1 + "\n")
    txtnew.write(strlist2 + "\n")
    txtnew.close()

    oldlist=['']
    newlist1=['']
    newlist2=['']
    flag23="大额其他应付款项性质说明"
    txtbuffer23=txtbuffer[txtbuffer.find(flag23):txtbuffer.find(flag23)+400]
    keytxt23 = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    keytxt23.write("（4）"+flag23+"：\n")
    keytxt23.write(str(txtbuffer23) + "\n")
    keytxt23.close()
    oldlist=list(txtbuffer23.split(' '))
    for o in oldlist:
        if "公司" in o:
            if o!=name:
                newlist1.append(o)
    for n in oldlist:
        if ',' in n:
            newlist2.append(n)
    # newlist1=list(set(newlist1))
    strlist1="\n".join(newlist1)
    strlist1 = strlist1[1:]
    strlist2="\n".join(newlist2)
    strlist2 = strlist2[1:]

    txtnew=open("output/"+fname+"/supplier_"+fname+".txt","a")
    txtnew.write(strlist1)
    txtnew.close()
    txtnew = open("output/" + fname + "/keywords_" + fname + ".txt", "a")
    txtnew.write(strlist1 + "\n")
    txtnew.write(strlist2 + "\n")
    txtnew.close()

    TXTtemp.close()