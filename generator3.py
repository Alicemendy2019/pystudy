print('ジェネレータ式とは、ジェネレータ関数を簡潔に記述するための記法')

genexp = (x for x in range(4))
print(type(genexp))
print(list(genexp))

def samegen():
    yield from range(4)

genexp2 = samegen()
print(type(genexp2))
print(list(genexp2))

evenGene = lambda x,y:(z for z in range(x,y) if z % 2 == 0)
print(type(evenGene(0,5)))
print(list(evenGene(0,5)))

print("""
「yield from 式」のような形で記述する。
このとき「式」を評価した結果は
反復可能オブジェクトまたはイテレータである必要がある。
""")

def samgene2():
    yield from [1,2,3,4]
    print('fin')
