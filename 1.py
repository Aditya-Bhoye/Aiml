import heapq
def a_star(graph,heuristics,start,goal):
    priority_queue=[(0,start)]
    g_cost={start:0}
    parent={start:None}
    while priority_queue:
        current_cost,current_node=heapq.heappop(priority_queue)
        if current_node==goal:
            path=[]
            while current_node:
                path.append(current_node)
                current_node=parent[current_node]
            return path[::-1],g_cost[goal]
        for neighbour,cost in graph[current_node]:
            new_cost=g_cost[current_node]+cost
            if neighbour not in g_cost or new_cost<g_cost[neighbour]:
                g_cost[neighbour]=new_cost
                priority=new_cost+heuristics[neighbour]
                heapq.heappush(priority_queue,(priority , neighbour))
                parent[neighbour]=current_node
    return None,float("inf")
graph = {
    "Delhi": [("Agra", 233), ("Jaipur", 273)],
    "Agra": [("Gwalior", 120), ("Kanpur", 290)],
    "Jaipur": [("Kota", 252), ("Delhi", 273)],
    "Gwalior": [("Indore", 484)],
    "Kanpur": [("Lucknow", 90)],
    "Kota": [("Indore", 340)],
    "Lucknow": [],
    "Indore": []
}
heuristics = {
    "Delhi": 240,
    "Agra": 240,
    "Gwalior": 350,
    "Kanpur": 500,
    "Jaipur": 0,
    "Kota": 250,
    "Indore": 400,
    "Lucknow": 600
}
path,cost=a_star(graph,heuristics,"Delhi","Kota")
print("Best Path:", path)
print("Total Cost (km):", cost)
