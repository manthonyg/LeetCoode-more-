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
    def __init__(self):
      self.children = {}
      self.isEnd = False

    def setChild(self,x):
        self.children.setdefault(x,Trie())

    def getChild(self,x):
        return self.children.get(x,None)
    
