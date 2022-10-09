class Quiz:
    def __init__(self,question,a,b,c,d,correct):
        self._question=question
        self._a=a
        self._b=b
        self._c=c
        self._d=d
        self._correct=correct
    #getters
    def getquestion(self):
        return self._question  
    def getanswers(self):
        return self._a +' '+ self._b +' '+ self._c  
    def getcorrect(self):
        return self._correct
    #setters
    def setQuestion(self,question): 
        self._question=question
    def setanswers(self,a,b,c):
        self._a=a
        self._b=b
        self._c=c
    def setCorrect(self,correct):
        self._correct=correct
    #print Question as string
    def __str__(self):
        print(self._question,"\n 1.",self._a,"\n 2.",self._b,"\n 3.",self._c,"\n 4.",self._d)
        return ""
#Quick Test
    #Question1=Quiz("what","a","b","c","d",4)
    #print(Question1)