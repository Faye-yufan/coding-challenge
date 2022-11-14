# This algorithm is a simple iteration and recursion process. 

# I will be using the following algorithm to write the python code for this problem:

# 1.) iterate through all the elements in strArr. Set maximum traffic value as zero at each iteration.

# 2.) get the node from elements

# 3.) get all the adjacent nodes of the node from step 2.

# 4.) iterate through the adjacent nodes

# 5.) add the value of current adjacent node to traffic

# 6.) get all the unvisited adjacent nodes of current node and repeat from step 4 until all the nodes are visited.

# 7.) update the value of maximum traffic.

# 8.) add the value of node from step 2 and maximum traffic value to a string.

# 9.) sort the string according to node values.

# 10.) return the string.

 

# Python program:

# Let's implement the algorithm step by step in code:
# 1.) iterate through all the elements in strArr. Set maximum traffic value as zero at each iteration.

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0

# 2.) get the node from elements

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0
#         nodes=elements.split(":")[0]

# 3.) get all the adjacent nodes of the node from step 2.

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0
#         nodes=elements.split(":")[0]
#         adj = adjacentNodes(nodes, strArr) #adjacentNodes() will be defined in the end

# 4.) iterate through the adjacent nodes

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0
#         nodes=elements.split(":")[0]
#         adj = adjacentNodes(nodes, strArr)
#         for currentNode in adj:
#             visited = [nodes]
#             traffic = 0

 

# 5.) add the value of current adjacent node to traffic

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0
#         nodes=elements.split(":")[0]
#         adj = adjacentNodes(nodes)
#         for currentNode in adj:
#             visited = [nodes]
#             traffic = 0
#             visited.append(currentNode)
#             traffic += int(currentNode)

# 6.) get all the unvisited adjacent nodes of current node and repeat from step 4 until all the nodes are visited.

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0
#         nodes=elements.split(":")[0]
#         adj = adjacentNodes(nodes, strArr)
#         for currentNode in adj:
#             visited = [nodes]
#             traffic = 0
#             visited.append(currentNode)
#             traffic += int(currentNode)
#             traffic, visited = addTrafficToCurrentNode(traffic, currentNode, visited) #this function will be implemented in #the end

# 7.) update the value of maximum traffic.

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0
#         nodes=elements.split(":")[0]
#         adj = adjacentNodes(nodes)
#         for currentNode in adj:
#             visited = [nodes]
#             traffic = 0
#             visited.append(currentNode)
#             traffic += int(currentNode)
#             traffic, visited = addTrafficToCurrentNode(traffic, currentNode, visited, strArr)
#             if maxTraffic<traffic:
#                 maxTraffic = traffic

# 8.) add the value of node from step 2 and maximum traffic value to a string.

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0
#         nodes=elements.split(":")[0]
#         adj = adjacentNodes(nodes, strArr)
#         for currentNode in adj:
#             visited = [nodes]
#             traffic = 0
#             visited.append(currentNode)
#             traffic += int(currentNode)
#             traffic, visited = addTrafficToCurrentNode(traffic, currentNode, visited, strArr)
#             if maxTraffic<traffic:
#                 maxTraffic = traffic
#         strMax.append(f"{nodes}:{maxTraffic}")

# 9.) sort the string according to node values.

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0
#         nodes=elements.split(":")[0]
#         adj = adjacentNodes(nodes, strArr)
#         for currentNode in adj:
#             visited = [nodes]
#             traffic = 0
#             visited.append(currentNode)
#             traffic += int(currentNode)
#             traffic, visited = addTrafficToCurrentNode(traffic, currentNode, visited, strArr)
#             if maxTraffic<traffic:
#                 maxTraffic = traffic
#         strMax.append(f"{nodes}:{maxTraffic}")
#     strMax = sorted(strMax, key = lambda x: int(x.split(":")[0]))
#     strMax = ",".join(strMax)

# 10.) return the string.

# def cityTraffic(strArr):
#     strMax = []
#     for elements in strArr:
#         maxTraffic = 0
#         nodes=elements.split(":")[0]
#         adj = adjacentNodes(nodes, strArr)
#         for currentNode in adj:
#             visited = [nodes]
#             traffic = 0
#             visited.append(currentNode)
#             traffic += int(currentNode)
#             traffic, visited = addTrafficToCurrentNode(traffic, currentNode, visited, strArr)
#             if maxTraffic<traffic:
#                 maxTraffic = traffic
#         strMax.append(f"{nodes}:{maxTraffic}")
#     strMax = sorted(strMax, key = lambda x: int(x.split(":")[0]))
#     strMax = ",".join(strMax)
#     return strMax
 

# adjacentNodes() function:
# This function taked a node value and strArr as argument and returns the adjacent nodes of given node from strArr

 

# def adjacentNodes(node, strArr):
#     for elements in strArr:
#         if(elements.split(":")[0]==node):
         
#             return elements.split(":")[1][1:-1].split(",")

 

# addTrafficToCurrentNode() function:
# This function takes the value of traffic, visited node list, current node, and strArr as arguments. It add the value of all nodes connected in the path containing the current node using a recursion algorithm. It then returns the value of traffic and visited node list.

# def addTrafficToCurrentNode(traffic, currentNode, visited, strArr):
#     for x in adjacentNodes(currentNode, strArr):
#         if x not in visited:
#             traffic += int(x)
     
#             visited.append(x)
#             traffic, visited = addTrafficToCurrentNode(traffic, x, visited, strArr)
#     return traffic,visited

 

def cityTraffic(strArr):
    strMax = []
    for elements in strArr:
        maxTraffic = 0
        nodes=elements.split(":")[0]
        adj = adjacentNodes(nodes, strArr)
        for currentNode in adj:
            visited = [nodes]
            traffic = 0
            visited.append(currentNode)
            traffic += int(currentNode)
            traffic, visited = addTrafficToCurrentNode(traffic, currentNode, visited, strArr)
            if maxTraffic<traffic:
                maxTraffic = traffic
        strMax.append(f"{nodes}:{maxTraffic}")
    strMax = sorted(strMax, key = lambda x: int(x.split(":")[0]))
    strMax = ",".join(strMax)
    return strMax

def addTrafficToCurrentNode(traffic, currentNode, visited, strArr):
    for x in adjacentNodes(currentNode, strArr):
        if x not in visited:
            traffic += int(x)
     
            visited.append(x)
            traffic, visited = addTrafficToCurrentNode(traffic, x, visited, strArr)
    return traffic,visited

def adjacentNodes(node, strArr):
    for elements in strArr:
        if(elements.split(":")[0]==node):
            return elements.split(":")[1][1:-1].split(",")


strArr = ["1:[5]", "4:[5]", "3:[5]", "5:[1,4,3,2]", "2:[5,15,7]", "7:[2,8]", "8:[7,38]", "15:[2]", "38:[8]"]
print(cityTraffic(strArr))

# Output:
# 1:82,2:53,3: 80,4:79,5:70,7:46,8:38,15:68,38:45
