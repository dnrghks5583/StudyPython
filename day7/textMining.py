import numpy as np

class TextMininig :

    __txt = ''
    __uniqueList = []
    __tfList = []
    __idfList = []
    __tf_IdfList = []

    def __init__(self, txt) :
        self.__txt = txt

    def __makeUniqueList(self):     # 과일이 

        temp = []
        for sentence in self.__txt :
            [temp.append(term) for term in sentence.split(' ')]

        self.__uniqueList = set(temp)
        self.__uniqueList = list(self.__uniqueList)
        self.__uniqueList.sort()

    def __printUniqueList(self) :
        print(self.__uniqueList)

    def __tf(self, doc, term) :
        return doc.count(term)
    
    def __makeTfList(self) :

        for sentence in self.__txt:
            temp = []
            [temp.append(self.__tf(sentence, term)) for term in self.__uniqueList]
            self.__tfList.append(temp)
        
    def __df(self, term) :
    
        cnt = 0
        for sentence in self.__txt :
            temp = sentence.count(term)
            if temp > 1 :
                temp = 1
            cnt += temp
        return cnt

    def __idf(self, term) :
        df_ = self.__df(term)
        return np.log(len(self.__txt)/(df_ + 1))

    def __makeIdfList(self) :
        self.__idfList = [self.__idf(term) for term in self.__uniqueList]

    def __tf_Idf(self) :
        [self.__tf_IdfList.append(np.array(termFrequency) * np.array(self.__idfList)) for termFrequency in self.__tfList]
    
    def run(self) :     # 실행
        self.__makeUniqueList()
        self.__makeTfList()
        self.__makeIdfList()
        self.__tf_Idf() 

    def __printList(self, temp) :
        [print(f'{e:1.3}', end = '  ') for e in temp]
        print()

    def printResult(self) :

        print('Unique List')
        self.__printUniqueList()
        print()

        for i in range(1, len(self.__txt) + 1) :
            print(f'------------------- document {i} -------------------') 
            self.__printList(self.__tf_IdfList[i - 1])
            print()
