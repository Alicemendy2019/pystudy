def mygenerator():
    var = yield 1
    print("var" , var)
    var = yield 2
    print("var" , var)
    var = yield 3
    print("var" , var)

mg = mygenerator()
print(mg)
dirmg = dir(mg)
for mgmethod in dirmg:
    print(mgmethod)
    # print(mg.mgmethod())

print(dirmg)
print("__iter__" in dir(mg))
print("__next__" in dir(mg))

print(next(mg))
# print(next(mg))
print(mg.__next__())
# print(mg.__next__())
print(mg.send("test"))

def countupgene(limit=5):
    counter = 0
    while True:
        if counter >= limit:
            break
        yield counter
        counter += 1

def ts():
    pass
cug = countupgene(3)
print("__iter__" in dir(cug))
print("__next__" in dir(cug))
