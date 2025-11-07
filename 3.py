def depth_first_search(graph,start,goal):
    visited=set()
    order=[]
    path=[]
    def dfs(node):
        if node in visited:
            return False
        visited.add(node)
        order.append(node)
        path.append(node)
        if node==goal:
            return True
        for neighbour in graph[node]:
            if dfs(neighbour):
                return True
        path.pop()
        return False
    dfs(start)
    return order,path
graph={
    "Camp": ["Forest", "River"],
    "Forest": ["Cave", "Clearing"],
    "Clearing": ["Tower"],
    "River": ["Waterfall"],
    "Cave": ["Treasure Room"],
    "Tower": ["Treasure Room"],
    "Waterfall": [],
    "Treasure Room": []
}
starting= "Camp"
goal= "Waterfall"
order,path=depth_first_search(graph,starting,goal)
for step,node in enumerate(order,start=1):
    print(f"{step}.{node}")
if goal and path[-1]== goal:
    print("\n Treasure to path "," -> ".join(path))
