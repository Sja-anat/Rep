torn_1=[7,6,5,4,3,2,1]
torn_2=[0,0,0,0,0,0,0]
torn_3=[0,0,0,0,0,0,0]

torn=[torn_1,torn_2,torn_3]

print(torn)

def flytt(t_fra,t_til,t_mellom,t_stor):
    if t_stor == 1:
        t_fra[t_fra.index(1)], t_til[t_til.index(0)] = t_til[t_til.index(0)], t_fra[t_fra.index(1)]
        print(torn)
    else:
        flytt(t_fra,t_mellom,t_til,t_stor-1)
        t_fra[t_fra.index(t_stor)], t_til[t_til.index(0)] = t_til[t_til.index(0)], t_fra[t_fra.index(t_stor)]
        print(torn)
        flytt(t_mellom,t_til,t_fra,t_stor-1)

flytt(torn_1,torn_3,torn_2,7)