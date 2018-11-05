import requests

url='https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text'
r=requests.get(url)
r.encoding='utf8'
data=str(r.text)
begin=data.find("President Donald Trump")
end=data.rfind('Thank you very much')
a=data[begin:end]

mydict={}
words=str(a)
words=words.replace('<','')
words=words.replace('"','')
words=words.replace(',','')
words=words.replace("'",'')
words=words.replace('.','')
words=words.replace('>','')
words=words.replace('/','')
words=words.replace('=','')
words=words.replace('-','')
words=words.replace('#','')


words=str(a).split()

for w in words:
    if w in mydict:
        mydict[w]+=1
    else:
        mydict[w]=1

for k in sorted(mydict,key=mydict.__getitem__, reverse=True):
    print(k,mydict[k])
    if mydict[k]<10:
            break
