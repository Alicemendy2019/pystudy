def hello(whom):
    message = 'Hello' + str(whom)
    print(message)

def myfnc(prm1,prm2,prm3):
    return f'prm1:{prm1},prm2:{prm2},prm3:{prm3}'

def myfnc2(prm1,prm2,*args):
    return f'prm1:{prm1},prm2:{prm2},other:{args}'

def myfnc3(prm1,prm2,**args):
    return f'prm1:{prm1},prm2:{prm2},other:{args}'

def myfnc4(prm1,*args,**kwargs):
    return f'prm1:{prm1},args:{args},kwargs:{kwargs}'

hello('ame')
print(myfnc(1,2,3))
print(myfnc(prm3=3,prm1=1,prm2=2))
#unpack
print(myfnc(*'123'))
print(*'123')
data = {'prm1':'1','prm2':'2','prm3':'3'}
print(myfnc(**data))
data = {'prm1':'1','prm2':'2','prm3':'3','prm4':'4','prm5':'5'}
print(myfnc2(1,2,3,4,5))
print(myfnc3(**data))
data2 = [1,2,3,4,5]
# print(myfnc4(1,*data2,**data))
print(__name__)
