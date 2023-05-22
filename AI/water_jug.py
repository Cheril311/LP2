from collections import deque

def solve(jug1,jug2,target):
    
    initial = (0,0)
    actions = [
        ('Fill Jug1',lambda state: (jug1,state[1])),
        ('Fill Jug2',lambda state: (state[0],jug2)),
        ('Empty Jug1', lambda state: (0,state[1])),
        ('Empty Jug2', lambda state: (state[0],0)),
        ('Pour Jug1 to Jug2', lambda state: (max(0,state[0]+state[1]-jug2),min(state[0]+state[1],jug2))),
        ('Pour Jug2 to Jug1', lambda state: (min(state[0]+state[1],jug1),max(0,state[0]+state[1]-jug1)))
    ]
    
    queue = deque()
    queue.append((initial,[]))
    visited = set()
    
    while queue:
        curr,path = queue.popleft()
        
        if curr[0]==target or curr[1]==target:
            return path
        
        for action,func in actions:
            new = func(curr)
            if new not in visited:
                queue.append((new,path+[(action,new)]))
                visited.add(new)
    return None

k = solve(4,3,2)
print('Initial State:',(0,0))
for i,j in k:
    print(i,':',j)
print('Goal state: ', k[-1][1])
