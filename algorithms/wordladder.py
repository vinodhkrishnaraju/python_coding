# To check if strings differ by 
# exactly one character 

def isadjacent(a, b): 
    count = 0
    n = len(a) 

    # Iterate through all characters and return false 
    # if there are more than one mismatching characters 
    for i in range(n): 
        if a[i] != b[i]: 
            count += 1
        if count > 1: 
            break

    return True if count == 1 else False

# A queue item to store word and minimum chain length 
# to reach the word. 
class QItem(): 

    def __init__(self, word, len): 
        self.word = word 
        self.len = len

# Returns length of shortest chain to reach 
# 'target' from 'start' using minimum number 
# of adjacent moves. D is dictionary 
def shortestChainLen(start, target, D): 

    # Create a queue for BFS and insert 
    # 'start' as source vertex 
    Q = [] 
    item = QItem(start, 1) 
    Q.append(item) 

    while( len(Q) > 0): 

        curr = Q.pop() 

        # Go through all words of dictionary 
        for it in D: 

            # Process a dictionary word if it is 
            # adjacent to current word (or vertex) of BFS 
            temp = it 
            if isadjacent(curr.word, temp) == True: 

                # Add the dictionary word to Q 
                item.word = temp 
                item.len = curr.len + 1
                Q.append(item) 

                # Remove from dictionary so that this 
                # word is not processed again. This is 
                # like marking visitedited 
                D.remove(temp) 

                # If we reached target 
                if temp == target: 
                    return item.len

D = [] 
D.append("poon") 
D.append("plee") 
D.append("same") 
D.append("poie") 
D.append("plie") 
D.append("poin") 
D.append("plea") 
start = "toon"
target = "plea"
print "Length of shortest chain is: %d" \ 
        % shortestChainLen(start, target, D) 
        
# This code is contributed by Divyanshu Mehta        


class Solution:
    
    
    def isOneWord(self, w1, w2):
        one = False
        for i,val in enumerate(w1):
            if val != w2[i]:
                if one:
                    return False
                one = True
        return one
    
    def bfs(self, start, end, dictV):
        q = [start]
        q_order = 0
        added = 1
        visited = {}
        lev = 1
        end_found = False
        while q_order < len(q):
            lenn = len(q)
            c = 0
            while c < added:
                cur = q[q_order]
                for i,val in enumerate(dictV):
                    if val not in visited and self.isOneWord(val, cur):
                        q.append(val)
                        visited[val] = 1
                        if val == end:
                            end_found = True
                c+=1
                q_order+=1
            added = len(q) - lenn
            if added>0:
                lev+=1
            if end_found:
                return lev
        return 0
            
        
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        if start==end:
            return 1
        dictV.append(end)
        return self.bfs(start, end, dictV)


