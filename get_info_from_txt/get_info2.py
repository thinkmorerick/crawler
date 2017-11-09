# coding:utf-8

import os

try:
    os.mkdir('./output2/')
except:
    pass

fname = '15166020'

TXTtemp = open("txt/" + fname + ".txt","r+")
txtbuffer=TXTtemp.read().strip()

try:
    os.mkdir('./output2/' + fname)
except:
    pass

original=open("output2/"+fname+"/original_" + fname + ".txt","w")
original.write(txtbuffer)
original.close()

txtbuffer=" ".join(txtbuffer.split())
txtbuffer=txtbuffer[:-1].strip()
second=open("output2/"+fname+"/second_" + fname + ".txt","w")
second.write(txtbuffer)
second.close()

listname=list(txtbuffer.split(' '))
sharenum = ''
for s in listname:
    if '股票代码' == s:
        sharenum = listname[listname.index(s)+1]

print("sharenum:"+sharenum)
sharenumtxt=open("output2/"+fname+"/keywords_"+fname+".txt","a")
sharenumtxt.write("sharenum:"+sharenum+"\n")
sharenumtxt.close()
namearea=listname[:10]
name = ''
for n in namearea:
    if '公司' in n:
        name = n

print("namearea---->",namearea)
print("name---->",name)
txtname=open("output2/"+fname+"/keywords_"+fname+".txt","a")
txtname.write(str(name)+":\n")
txtname.write(str(namearea)+"\n")
txtname.close()


oldlist=['']
newlist=['']
flag1="按欠款方归集的期末余额前五名的其他应收款情况"
txtbuffer1=txtbuffer[txtbuffer.find(flag1):txtbuffer.find(flag1)+500]
keytxt1=open("output2/"+fname+"/keywords_"+fname+".txt","a")
keytxt1.write("按欠款方归集的期末余额前五名的其他应收款情况:\n")
keytxt1.write(str(txtbuffer1)+"\n")
keytxt1.close()

oldlist=list(txtbuffer1.split(' '))
print("oldlist：",oldlist)
print("===============================")
for o in oldlist:
    if "公司" in o:
        if o!=name:
            o=oldlist[oldlist.index(o)-1]+o
            newlist.append(o)

newlist=list(set(newlist))
print("newlist1：",newlist)
strlist="\n".join(newlist)

txtnew=open("output2/"+fname+"/customer_"+fname+".txt","a")
txtnew.write(strlist)
txtnew.close()
txtnew=open("output2/"+fname+"/keywords_"+fname+".txt","a")
txtnew.write("customer:\n")
txtnew.write(strlist+"\n")
txtnew.close()

oldlist=['']
newlist=['']
flag11="期末单项金额重大并单项计提坏帐准备的其他应收款"
txtbuffer11=txtbuffer[txtbuffer.find(flag11):txtbuffer.find(flag11)+200]
keytxt11=open("output2/"+fname+"/keywords_"+fname+".txt","a")
keytxt11.write("期末单项金额重大并单项计提坏帐准备的其他应收款:\n")
keytxt11.write(str(txtbuffer11)+"\n")
keytxt11.close()
oldlist=list(txtbuffer11.split(' '))

print("oldlist：",oldlist)
print("===============================")
for o in oldlist:
    if "公司" in o:
        if o!=name:
            newlist.append(o)

newlist=list(set(newlist))
print("newlist11：",newlist)
strlist="\n".join(newlist)

txtnew=open("output2/"+fname+"/customer_"+fname+".txt","a")
txtnew.write(strlist)
txtnew.close()
txtnew=open("output2/"+fname+"/keywords_"+fname+".txt","a")
txtnew.write("customer:\n")
txtnew.write(strlist+"\n")
txtnew.close()

oldlist=['']
newlist=['']
flag2="账龄超过 1 年的重要应付账款"
txtbuffer2=txtbuffer[txtbuffer.find(flag2):txtbuffer.find(flag2)+300]
keytxt2=open("output2/"+fname+"/keywords_"+fname+".txt","a")
keytxt2.write("账龄超过 1 年的重要应付账款:\n")
keytxt2.write(str(txtbuffer2)+"\n")
keytxt2.close()
oldlist=list(txtbuffer2.split(' '))
print("oldlist：",oldlist)
print("===============================")
for o in oldlist:
    if "公司" in o:
        if o!=name:
            newlist.append(o)

newlist=list(set(newlist))
print("newlist2：",newlist)
strlist="\n".join(newlist)

txtnew=open("output2/"+fname+"/supplier_"+fname+".txt","a")
txtnew.write(strlist)
txtnew.close()
txtnew=open("output2/"+fname+"/keywords_"+fname+".txt","a")
txtnew.write("supplier:\n")
txtnew.write(strlist+"\n")
txtnew.close()

oldlist=['']
newlist=['']
flag21="账龄超过 1 年的重要其他应付款"
txtbuffer21=txtbuffer[txtbuffer.find(flag21):txtbuffer.find(flag21)+500]
keytxt21=open("output2/"+fname+"/keywords_"+fname+".txt","a")
keytxt21.write("账龄超过 1 年的重要其他应付款:\n")
keytxt21.write(str(txtbuffer21)+"\n")
keytxt21.close()
oldlist=list(txtbuffer21.split(' '))
print("oldlist：",oldlist)
print("===============================")
for o in oldlist:
    if "公司" in o:
        if o!=name:
            newlist.append(o)

newlist=list(set(newlist))
print("newlist21：",newlist)
strlist="\n".join(newlist)

txtnew=open("output2/"+fname+"/supplier_"+fname+".txt","a")
txtnew.write(strlist)
txtnew.close()
txtnew=open("output2/"+fname+"/keywords_"+fname+".txt","a")
txtnew.write("supplier:\n")
txtnew.write(strlist+"\n")
txtnew.close()

print("name---->",name)
TXTtemp.close()