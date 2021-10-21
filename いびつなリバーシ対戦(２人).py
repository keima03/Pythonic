# Aランクレベルアップメニュー STEP: 8 いびつなリバーシ対戦（２人）  # AとB　石があれば途中が空白でも自分の石に変えられる
#https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_pincerattack_step8/edit?language_uid=python3
def rv(Y,X,Q):
    d=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    L[Y][X] = q[Q]
    
    for i in range(8):
        y,x,dL=Y,X,[]
        while 1:
            y += d[i][0]
            x += d[i][1]
            if -1 < y < H and -1 < x < W:
                dL.append([y,x])
                if L[y][x] == '#':
                    break
                if L[y][x] == q[Q]:
                    for j,k in dL[:-1]:
                        L[j][k] = q[Q] 
                    break             
            else:
                break
q = {0:'A',1:'B'}
H, W, N = map(int, input().split())
L = [list(input()) for i in range(H)]
P = [[int(x) for x in input().split()] for i in range(N*2)]
for i,v in enumerate(P):
    v.append(i % 2)
_ = [rv(dy,dx,Q) for dy,dx,Q in P]
re = [print(''.join(i)) for i in L]