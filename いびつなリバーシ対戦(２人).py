# Aランクレベルアップメニュー STEP: 8 いびつなリバーシ対戦（２人）  
def rv(Q,Y,X):
    L[Y][X] = q[Q]
    for h,i in [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]:
        y,x,P=Y,X,[]
        while 1:
            y += h
            x += i
            if -1 < y < H and -1 < x < W:
                P.append([y,x])
                if L[y][x] == '#':
                    break
                if L[y][x] == q[Q]:
                    for j,k in P[:-1]:
                        L[j][k] = q[Q] 
                    break             
            else:
                break
q = {0:'A',1:'B'}
H, W, N = map(int, input().split())
L = [list(input()) for i in range(H)]
_ = [rv(Q,dy,dx) for Q,dy,dx in [[i % 2]+[int(x) for x in input().split()] for i in range(N*2)]]
re = [print(''.join(i)) for i in L]
