
import json
pc = [
    {"name":"hardware","description":""},
    {"name":"software","description":""},
    {"name":"communication","description":""}
]

hardware = [
    {"name":"memory","description":""},
    {"name":"CPU","description":""},
    {"name":"HDD","description":""},
    {"name":"cable","description":""},
    {"name":"storage","description":""},
    {"name":"electric bord","description":""}
]

software = [
    {"name":"Operation System","description":""},
    {"name":"middleware","description":""},
    {"name":"application","description":""},
    {"name":"development tool","description":""},
    {"name":"programing lunguage","description":""}
]

with open('pc.txt','w') as f:
    json.dump(pc,f,indent=2)

with open('pc.txt','r') as f:
    data = json.load(f)

# print(data)
# print(data[0])
data[0]['child'] = hardware
data[1]['child'] = software
# print(data[0])
with open('pc2.txt','w') as f:
    json.dump(data,f,indent=2)

with open('pc2.txt','r') as f:
    data = json.load(f)

Operation_System = [
    {"name":"カーネル","description":""},
    {"name":"シェル","description":""},
    {"name":"API","description":""}
]

middleware = [
    {"name":"データベース","description":""},
    {"name":"Web","description":""},
    {"name":"AP","description":""},
    {"name":"バックアップ","description":""},
    {"name":"ジョブ運用","description":""},
    {"name":"監視","description":""},
    {"name":"高可用性クラスタ","description":""}
]

development_tool = [
    {"name":"エディタ","description":""},
    {"name":"Cient","description":""},
    {"name":"IDE","description":""},
    {"name":"CIツール","description":""},
    {"name":"テスト","description":""},
    {"name":"環境","description":""},
    {"name":"DB設計","description":""},
    {"name":"DBクライアント","description":""},
    {"name":"キーバインド","description":""},
    {"name":"コード","description":""},
    {"name":"文章入力補助","description":""},
    {"name":"エクスプローラー","description":""},
    {"name":"コンソール","description":""},
    {"name":"検索","description":""},
    {"name":"Excel補助","description":""},
    {"name":"chat","description":""},
    {"name":"タスク管理","description":""},
    {"name":"メール","description":""},
    {"name":"ブラウザ","description":""},
    {"name":"Bash","description":""}
]

programing_lunguage = [
    {"name":"C","description":""},
    {"name":"C++","description":""},
    {"name":"C#","description":""},
    {"name":"Java","description":""},
    {"name":"Javascript","description":""},
    {"name":"python","description":""},
    {"name":"ruby","description":""},
    {"name":"julia","description":""},
    {"name":"VB","description":""},
    {"name":"VBA","description":""},
    {"name":"PHP","description":""},
    {"name":"HTML","description":""},
    {"name":"CSS","description":""},
    {"name":"Objective-c","description":""},
    {"name":"Swift","description":""},
    {"name":"ABAP","description":""},
    {"name":"Rust","description":""},
    {"name":"BluePrint","description":""},
    {"name":"Shell","description":""},
    {"name":"TypeScript","description":""},
    {"name":"HDL","description":""}
]

data[1]['child'][0] = Operation_System
data[1]['child'][1] = middleware
data[1]['child'][3] = development_tool
data[1]['child'][4] = programing_lunguage

# print(data[0])
with open('pc3.txt','w',encoding='shift_jis') as f:
    json.dump(data,f,indent=2,ensure_ascii=False)

with open('pc3.txt','r') as f:
    data = json.load(f)

def ggg(iterable):
    while True:
        if '__iter__' in dir(iterable):
            print('if')
            for n in iterable:
                yield n
        else:
            print('else')
            yield 'au'
dd = ggg(data)
# print(type(data))
# print(dd)
print(next(dd))
print(next(dd))
print(next(dd))
print(next(dd))
# for n in data:
#     print(n)
