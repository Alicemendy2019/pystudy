def hellomsg_generator():
    namelist = ['abe','kasai','ono']
    counter = 0
    length = len(namelist)
    value = None
    while True:
        if value:
            namelist.append(str(value))
            length += 1
            counter = length - 1
        value = yield 'hello ' + namelist[counter]
        counter += 1
        if counter % length == 0:
            counter = 0


hmg = hellomsg_generator()
print(hmg.__next__())
print(hmg.send('fujimoto'))
print(hmg.__next__())
print(hmg.__next__())
print(hmg.__next__())
print(hmg.__next__())
print(hmg.__next__())
print(hmg.__next__())

print("""
throw method
    yield式によって実行が中断した箇所で
    引数に指定した例外を発生させる
    何らかの理由からジェネレータイテレータに対して
    例外を発生させる必要が生じたときに使う。
    このとき、発生させた例外をジェネレータイテレータ内部で処理して、
    実行を続けると、yield式によって次の値が呼び出した側に返送される。
    yield式に到達しなければ、StopIteration例外が発生する。
close method
    yield式によって実行が中断した箇所で
    GeneratorExit例外を発生させる
    ジェネレータ関数のコード末尾に達するよりも前に、
    ジェネレータイテレータが削除される事態が発生した際に自動的に呼び出される。
    主にジェネレータイテレータ内部で使用しているリソースを解放するのに使える。
    リソースを使用するコードをtry文で囲み、
    finally節にリソースを解放するコードを記述しておくことで、
    ジェネレータイテレータが利用するリソースを安全に解放できる
""")
print(dir(hmg))

def sampgen():
    counter = 0
    while True:
        try:
            yield counter
            counter += 1
        except TypeError as e:
            break
        except Exception as e:
            print(e)
            counter += 1
        finally:
            print('fin')

print("""
実はGeneratorExit例外は、
上の2つのexcept節では捕捉されない
（これはGeneratorExit例外がBaseExceptionクラスから派生するクラスで、
Exceptionクラス以下の通常の例外クラス階層には含まれていないからだ）。
よって、closeメソッドが呼び出されて、
ジェネレータイテレータ内部でGeneratorExit例外が発生すると、
それが処理されないまま、finally節が実行され、そこで同じ例外が再発生する。
closeメソッドがこれをうまく処理してくれるので、
呼び出し側では例外が発生しないようになっている。
""")

mygen = sampgen()
print(next(mygen))
print(mygen.throw(NameError,'name error'))
# print(mygen.throw(TypeError,'type error'))

next(mygen)
del mygen
print('hello')
print("""
通常の例外処理の流れに従ってfinally節だけで実行されて、
そこで最後にGeneratorExit例外が再発生する。
closeメソッドがうまくこれを処理してくれるので、
例外は呼び出し側には伝えられることなく、
実行が次の行に移り、「hello」と表示される。
""")
