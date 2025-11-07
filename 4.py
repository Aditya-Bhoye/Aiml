from heapq import heappop, heappush
def a_star(maze,start,goal):
    rows,cols=len(maze),len(maze[0])
    def heuristic(a,b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])
    open_set=[]
    heappush(open_set,(0+heuristic(start,goal),0,start))
    parent={start:None}
    g_cost={start:0}
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    while open_set:
        _,cost,(x,y)=heappop(open_set)
        if (x,y) ==goal:
            path=[]
            cur=goal
            while cur is not None:
                path.append(cur)
                cur=parent[cur]
            return path[::-1]
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and maze[nx][ny]==0:
                new_cost=cost+1
                if (nx,ny) not in g_cost or new_cost<g_cost[(nx,ny)]:
                    g_cost[(nx,ny)]=new_cost
                    parent[(nx,ny)]=(x,y)
                    f_cost=new_cost+heuristic((nx,ny),goal)
                    heappush(open_set,(f_cost,new_cost,(nx,ny)))
    return None 
maze = [
    [0,1,1,1,1],
    [0,0,0,0,1],
    [1,1,1,0,1],
    [0,1,0,0,0],
    [1,0,0,0,1]
]
start = (0, 0)
goal = (4, 1)
path = a_star(maze, start, goal)
print("Shortest Path:", path)
print("Steps:", len(path)-1 if path else "No path found")