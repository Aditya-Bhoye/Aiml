from collections import deque 
def bfs(maze,start,goal):
    rows,cols=len(maze),len(maze[0])
    queue=deque([start])
    visited=set([start])
    parent={start:None}
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        x,y=queue.popleft()
        if (x,y)==goal:
            path=[]
            cur=goal
            while cur is not None:
                path.append(cur)
                cur=parent[cur]
            return path[::-1]
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and maze[nx][ny]==0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                parent[(nx,ny)]=(x,y)
                queue.append((nx,ny))
    return None
maze=[
    [0,1,1,1,1],
    [0,0,0,0,1],
    [1,1,1,0,1],
    [0,0,0,0,0],
    [1,0,0,0,1]
]
start=(0,0)
goal=(4,1)
path=bfs(maze,start,goal)
print("Shortest Path:", path)
print("Steps:", len(path)-1 if path else "No path found")
