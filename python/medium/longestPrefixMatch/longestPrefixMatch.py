def longest(areaCodes, numbers):
  # answer = []
  # areaCodes.sort(key=len,reverse = True)
  # for number in numbers:
  #   for code in areaCodes:
  #     if number.startswith(code):
  #       answer.append(code)
  #       break;
  # print(areaCodes)
  # print(answer)
  # return answer
    class Trie():
        def __init__(self,value=None):
            self.children = {}
            self.isEnd = False
            self.value = value

        def setChild(self,x):
            self.children.setdefault(x,Trie(x))

        def getChild(self,x):
            return self.children.get(x,None)
    root = Trie()
    for code in areaCodes:
        node = root
        for c in code:
            node.setChild(c)
            node = node.getChild(c)
        node.isEnd = True
    
    
    # node = root
    # toPrint = list(node.children.values())
    # print(toPrint)
    # while len(toPrint)>0:
    #     curr = toPrint.pop(0)
    #     print(curr.value)
    #     if curr.children:
    #         toPrint += list(curr.children.values())
            
        

            
        


longest(["213", "21358", "1234", "12"], ["21349049","1204539492","123490485904"])

     
