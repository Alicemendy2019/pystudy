itesub = """イテレータ・・・「データの流れを表現するオブジェクト」
                それが持つ　__NEXT__メソッドやNEXT関数にそれを渡すと次の値を取り出せるもの
                    反復可能オブジェクトの１つと考えれる
        """
iterasub = """
イテラブル（反復可能）オブジェクト・・・「要素を1度に1つずつ返せるオブジェクト」
            ex.リスト、文字列、タプル、辞書、集合"""

print(itesub)
print(iterasub)

list1 = ["data1","data2","data3","data4","data5"]
strings1 = "strings_`data"

# リストでは要素すべてがメモリに存在し、イテレータではメモリに値が存在する必要はない
# リストには次の要素を取り出すためにイテレータを得る必要がある__iter__
inlist = [1,2,3,4,5,6,7,8,9]
iterator = iter(inlist) # list反復用のイテレータを取得

print(iterator.__next__())
print(iterator.__next__())
print(next(iterator))
print(next(iterator))

subsc = """
イテレータは以下2つのメソッドを持つ
__iter__ #  イテレータ自体を戻り値とする
__next__ #  次の要素を取り出す

イテラブルオブジェクトは以下のメソッドを持つ
__iter__ #  そのオブジェクトが持つ要素を反復するためのイテレータを返す
"""
print(subsc)


mapsub = """
        map関数　・・・　map関数は、リストの各要素に対して、
        一定の処理を加えて得られた結果を要素とするイテレータを戻り値とする。
        """
print(mapsub)

res = map(lambda x:x * x ,inlist)
print(inlist)
print(next(res))
print(next(res))
print(list(res))
filsub = """
    filter関数・・・map関数と同様にリストに何らかの処理を適用して、
    その結果を基に新たなイテレータを作成する関数としてはfilter関数もある
    filter関数は、関数とリスト（反復可能オブジェクト）を引数に取り、
    その関数にリストの各要素を渡して、
    その結果が真となるものだけを要素とするイテレータを戻り値とする。
         """
print(filsub)
res = filter(lambda x:x % 2 == 0,inlist)
print(next(res))
print(next(res))
print(list(res))

print("__next__と__iter__があればイテレータである")
ro = range(3)
print(ro)
print("__next__" in dir(ro))
print("__iter__" in dir(ro))
print("イテレータではなくイテラブルなのでイテレータを取り出す")
riterator = ro.__iter__()
print(riterator)
print(riterator.__next__())
print(next(riterator))


class cntUpIte:
    def __init__(self,limit=5):
        self.limit = limit
        self.counter = -1
    def __iter__(self):
        print('__iter__ method called')
        return self
    def __next__(self):
        print('__next__ method called')
        self.counter += 1
        if self.counter >= self.limit:
            raise StopIteration()
        return self.counter

myiterator = cntUpIte()
print(myiterator)
print(type(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(myiterator.__iter__())
print(myiterator.__next__())
print(myiterator.__next__())
# print(myiterator.__next__())

myiterator2 = cntUpIte(10)
print(list(myiterator2))

myiterator3 = cntUpIte(3)
for no in myiterator3:
    print(no)
