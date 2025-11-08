import heapq
goal=(1,2,3,4,5,0,7,8,6)
def manhattern(state):
    dist=0
    for i,val in enumerate(state):
        gr,gc=divmod(val-1,3)
        r,c=divmod(i,3)
        dist+=abs(gr-r)+abs(gc-c)
    return dist
def moves(state):
    i=state.index(0)
    r,c=divmod(i,3)
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    for dr,dc in dirs:
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:
            new=list(state)
            new[i],new[nr*3+nc]=new[nr*3+nc],new[i]
            yield tuple(new)
def a_star(start):
    pq=[(manhattern(start),0,start,[])]
    visited=set()
    while pq:
        f,g,state,path=heapq.heappop(pq)
        if state in visited:
            continue 
        visited.add(state)
        if state==goal:
            return path+[state]
        for nxt in moves(state):
            if nxt not in visited:
                heapq.heappush(pq,(g+1+manhattern(nxt),g+1,nxt,path+[state]))
    return None
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
path = a_star(start)
if path:
    print("Steps to solve:", len(path) - 1)
    for s in path:
        print(s[0:3])
        print(s[3:6])
        print(s[6:9], "\n")
else:
    print("No solution found (unsolvable puzzle).")