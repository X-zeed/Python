a=int(input())
b=int(input())
if a<=20000 and b<=20000:
    dic={
        '1000':0,
        '500':0,
        '100':0,
    }
    dic2={
        '1000':0,
        '500':0,
        '100':0,
    }
    dic['1000']+=int(a/1000)
    a-=dic['1000']*1000
    dic['500']+=int(a/500)
    a-=dic['500']*500
    dic['100']+=int(a/100)
    a-=dic['100']*100  
    dic2['1000']+=int(b/1000)
    b-=dic2['1000']*1000
    dic2['500']+=int(b/500)
    b-=dic2['500']*500
    dic2['100']+=int(b/100)
    b-=dic2['100']*100
    if a!=0 or b!=0:
        print("Input Error")
    else:
        print(dic['1000'] + dic2['1000'])
        print(dic['500'] + dic2['500'])
        print(dic['100'] + dic2['100'])
else:
    print("Input Error")