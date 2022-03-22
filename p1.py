def astarAlgo(startNode,stopNode):
    g={}
    parents={}
    open_set=set(startNode)
    closed_set=set()
    g[startNode]=0
    parents[startNode]=startNode
    
    while len(open_set)>0:
        
        n=None
        
        for v in open_set:
            if n==None or g[n]+heuristic(n)>g[v]+heuristic(v):
                n=v
                
        
        if n==stopNode or graphNodes.get(n)==None:
            pass
        
        else:
            
            for (m,weight) in getNeighbours(n):
                
                if m not in closed_set and m not in open_set:
                    open_set.add(m)
                    g[m]=g[n]+weight
                    parents[m]=n
                    
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                        
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
                            
        if n==None:
            
            print("Path doesn't exist!!!!")
            return None
        
        
        if n==stopNode:
            path=[]
            
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
                
                
            path.append(startNode)
            path.reverse()
            
            print("Path exists and it is {}".format(path))
            return path
        
        
        open_set.remove(n)
        closed_set.add(n)
        
    print("Path doesn't exist!!!!")
    return None

def getNeighbours(n):
    
    if graphNodes[n]!=None:
        return graphNodes[n]
    
    else:
        return None
    
#Path exists
# def heuristic(n):
    
#     H_dist={
#         "A":10,
#         "B":8,
#         "C":5,
#         "D":7,
#         "E":3,
#         "F":6,
#         "G":5,
#         "H":3,
#         "I":1,
#         "J":0
#     }
    
#     return H_dist[n]

# graphNodes={
    
#     "A":[("B",6),("F",3)],
#     "B":[("C",3),("D",2)],
#     "C":[("D",1),("E",5)],
#     "D":[("C",1),("E",8)],
#     "E":[("I",5),("J",5)],
#     "F":[("G",1),("H",7)],
#     "G":[("I",3)],
#     "H":[("I",2)],
#     "I":[("E",5),("J",3)]
   
# }

# astarAlgo("A","J")


#Path doesn't exist
def heuristic(n):
    
    H_dist={
        "A":1,
        "B":2,
        "C":3,
        "D":4,
        "E":5,
        "F":0
    }
    
    return H_dist[n]

graphNodes={
    
    "A":[("B",1)],
    "B":[("C",5),("D",4)],
    "C":[("E",6),("E",5)],
    "D":[("E",8)],
    "F":[("E",3)],
   
}

astarAlgo("A","F")
