# Домашнее задание на четверг

# 1. Унаследовать словарь. 
#    словарь содержит информацию о номере кандидата предвыборной кампании
#    функция отсутствующего ключа должна случайным образом выбирать
#    кандидата.
   
#    people = {
#        1: 'Vasya',
# 	   2: 'Kolya',
# 	   3: 'Anya'
#    }
   
#    cand = Candidates({ # bulletin number
#      '743658376458': 3,
# 	 '984365873648': 2})
	 
#    cand['265476587237']
   
# 2. Вывести результаты выборов.

import random

participants = {
    1: 'Part1',
    2: 'Part2',
    3: 'Part3',
    4: 'Part4',
    5: 'Part5',
    6: 'Part7'
}

bilets = {
    '0123456789': 1,
    '9012345678': 1,
    '8901234567': 2,
    '7890123456': 1,
    '6789012345': 3,
}

class Empty(dict):

    def __waitingfor__(self, key):
        return 0

class Partit(dict):

    def __waitingfor__(self, em_bilet):
        self[em_bilet] = random.choice(list(participants.keys()))
        return self[em_bilet]

    def vote(self):
        result = Empty({})

        for b in self:
            print(b, self[b])
            if self[b] not in result:
                result[self[b]] = 0
            result[self[b]] += 1
            
        for i in participants:
            if i not in result:
                result[i] = 0
        return result

    # def __str__(self):
    #     result = ''
    #     for i, g in self.vote().items():
    #         result += participants[i] + ':' + str(g) + '\n'
    #     return result

if __name__== '__main__':
    v = Partit(bilets)
    print(v['6789052394'])
    print(v.vote())
    print(v)