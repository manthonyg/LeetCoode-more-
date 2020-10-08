def longest(areaCodes, numbers):

  # Naive solution
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

  # Trie solution
    class Trie():
        def __init__(self,value=None):
            self.children = {}
            self.isEnd = False
            self.value = value

        def setChild(self,x):
            self.children.setdefault(x,Trie(x))

        def getChild(self,x):
            return self.children.get(x,None)

    # Input all areaCodes into a Trie
    root = Trie()
    for code in areaCodes:
        node = root
        for c in code:
            node.setChild(c)
            node = node.getChild(c)
        node.isEnd = True
    
    answer = []
    
    # Start looking for all matching prefixes
    for number in numbers:
        node = root
        prefix = ''
        path = ''
        for n in number:
            if node.getChild(n):
                path += n
                node = node.getChild(n)
                if node.isEnd:
                    prefix = path
            else:
                if prefix:
                    answer.append(prefix)
                break
    print(answer)

    # following code prints the entire Trie
    # node = root
    # toPrint = list(node.children.values())
    # print(toPrint)
    # while len(toPrint)>0:
    #     curr = toPrint.pop(0)
    #     print(curr.value)
    #     if curr.children:
    #         toPrint += list(curr.children.values())
            
        

            
        


longest(["213", "21358", "1234", "12"], ["21349049","1204539492","123490485904"])

     
