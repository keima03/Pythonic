#Aランクレベルアップメニュー  STEP: 9 FINAL問題 いびつなリバーシ対戦

def rv(Q,Y,X):
    d=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    L[Y][X] = Q
    
    for i in range(8):
        y,x,dL=Y,X,[]
        while 1:
            y += d[i][0]
            x += d[i][1]
            if -1 < y < H and -1 < x < W:
                dL.append([y,x])
                if L[y][x] == '#':
                    break
                if L[y][x] == Q:
                    for j,k in dL[:-1]:
                        L[j][k] = Q 
                    break             
            else:
                break

H, W, N ,n= map(int, input().split())
L = [list(input()) for i in range(H)]
P = [[int(x) for x in input().split()] for i in range(n)]
_ = [rv(Q,dy,dx) for Q,dy,dx in P]
re = [print(''.join(str(j) for j in i)) for i in L]
