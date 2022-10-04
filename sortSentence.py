class Solution:
    def sortSentence(self, s: str) -> str:
         sortedWord = [0] * len(s.split())
         sortSentence= " "
         for i in s.split():
            index = int(i[-1])
            Word = i[:-1]
            sortedWord[index-1] = Word
        
        
         return sortSentence.join(sortedWord)
