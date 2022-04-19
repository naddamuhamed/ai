import queue as Q

def bfs(graph,snode,goal):
    v=[]
    q=[]
    v.append(snode)
    q.append(snode)

    while q:
        # if q[0] is goal:
        #     return v
        ver=q.pop(0)
        if ver == goal:
            return v
        # if ver not in v:
        #     v.append(ver)



        for child in graph[ver]:
            if child not in v:
             v.append(child)
             q.append(child)
            #  break
        # else: q.pop()

    # return v
def dfs(graph,snode,goal):
    v = []
    q = []
    v.append(snode)
    q.append(snode)

    while q:
        
        ver = q.pop()
        if ver == goal:
            return v
        # if ver not in v:
        #     v.append(ver)

        for child in graph[ver]:
            if child not in v:
                v.append(child)
                q.append(child)
                break

    return v
def dfs2( visited,graph, node,goal):
    

    if node not in visited:
        # print (node)
        visited.append(node)
        if visited[len(visited)-1] is goal:
            print(visited) 
            return
        for neighbour in graph[node]:
            dfs2(visited, graph, neighbour,goal)
    
def ucs(graph,snode,goal):
    q=Q.PriorityQueue()
    v=[]
    q.put((0,[snode]))
    v.append(snode)
    while q:
        n=q.get()
        curr=n[1][len(n[1])-1]
        if goal in n[1]:
            return n[1],n[0]
            # print("path: "+str(n[1])+" cost: "+str(n[0]))
            # break
        cost=n[0]
        for child in graph[curr]:
            if child not in v:
                v.append(child)
                temp=n[1][:]
                temp.append(child)
                q.put((cost+graph[curr][child],temp))
def ucs2(graph,snode,goal):
    q=[]
    q.append((0,[snode]))
    while q:
        n=q.pop(0)
        curr=n[1][len(n[1])-1]
        if goal in n[1]:
            print("path: "+str(n[1])+" cost: "+str(n[0]))
            break
        cost=n[0]
        for child in graph[curr]:
            temp=n[1][:]
            temp.append(child)
            q.append((cost+graph[curr][child],temp))
        q.sort()

def gbfs(graph,snode,goal):
    ex = []
    q = [snode]
    while q:
        curr = q.pop(0)

        if curr not in ex:
            ex.append(curr)
            if curr == goal:
                print("goal reached")
                break
            n = graph[curr]
            n.sort(key=lambda a: a[1])
            q = n.pop(0)
        # q.sort()
    return ex
def GBFS(graph, startNode, goalNode):
    priorityQueue = Q.PriorityQueue()
    priorityQueue.put((graph[startNode], startNode))
    path = []

    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current)

        if current == goalNode:
            # print("goal reached")
            break

        # priorityQueue = Q.PriorityQueue()

        for i in graph[current]:
            if i[0] not in path:
                priorityQueue.put((i[1], i[0]))

    return path
def Astar(  graph,heuristics,startNode, goalNode):
    priorityQueue = Q.PriorityQueue()
    distance = 0
    path = []

    priorityQueue.put((heuristics[startNode] + distance, [startNode, 0]))

    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current[0])
        distance += int(current[1])

        if current[0] == goalNode:
            break

        # priorityQueue = Q.PriorityQueue()

        for i in graph[current[0]]:
            if i not in path:
                priorityQueue.put((heuristics[i] + graph[current[0]][i] + distance, [i, graph[current[0]][i] + distance]))

    return path
    
def astar(graph,heuristics,startNode, goalNode):
    p_q,visited=Q.PriorityQueue(),{}
    p_q.put((heuristics[startNode],0,startNode,[startNode]))
    visited[startNode]= heuristics[startNode]
    while not p_q.empty():
        (h,cost,vertex,path)=p_q.get()
        if vertex==goalNode:
            return h,path
        for nextnode in graph[vertex]:
            curr=cost+graph[vertex][nextnode]
            h=curr+heuristics[nextnode]
            if not (nextnode in visited ):
                visited[nextnode]=h
                p_q.put((h,curr,nextnode,path+[nextnode]))



