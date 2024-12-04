with open('input1.txt') as f:
    lines = f.read().splitlines()
    pairs = [line.split() for line in lines]
    pairs = [[int(s) for s in p] for p in pairs]
    c1 = [p[0] for p in pairs]
    c2 = [p[1] for p in pairs]
    c1 = sorted(c1)
    c2 = sorted(c2)
    s = 0
    for i in range(len(c1)):
        s += abs(c1[i] - c2[i])
        
    # print(s) # pt 1 solution 

    s2 = 0
    
    for i in range(len(c1)):
        s2 += c1[i] * c2.count(c1[i])
    print(s2) # pt 2 solution

