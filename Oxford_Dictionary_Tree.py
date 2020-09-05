class Trie:
    '''Fields: data'''
    def __init__(self, data):
        '''Set the data to the given data.
        To start with an empty tree, pass the empty dictionary, {}.'''
        self.data = data

    def __repr__(self):
        return 'Trie({})'.format(self.data)

    def __eq__(self, other):
        return isinstance(other, Trie) and \
            self.data == other.data
        
    def add(self, word):
            if self.data == {}:
                if len(word) > 0:
                    self.data[word[0]] = Trie({})
                    self.data[word[0]].add(word[1:])
                else:
                    self.data[""] = None
                    
            else:
                keyList = list(self.data.keys())
                if word ==  "":
                    self.data[word] = None
                elif word[0] in keyList:
                    self.data[word[0]].add(word[1:])
                else:
                    self.data[word[0]] = Trie({})
                    self.data[word[0]].add(word[1:])
        
    def readfile(self, filename):
        f = open(filename, "r")
        for x in f:
            if (x[-1] == "\n"):
                self.add(x[:len(x)-1])
            else:
                self.add(x)
        return None
    
    def dump(self):
            listOfWords = []
            trieList = self.data.keys()
            for key in trieList:
                if key != "":
                    for rest in self.data[key].dump():                
                        listOfWords.append(key+rest)
                else:
                    listOfWords.append('')
            listOfWords.sort()
            return listOfWords
            


sample1 = Trie({'a': Trie({'': None,
                           'n': Trie({'': None,
                                      'd': Trie({'': None})})}),
                'w': Trie({'a': Trie({'s': Trie({'': None}),
                                      'x': Trie({'': None}),
                                      'y': Trie({'': None})}),
                           'i': Trie({'n': Trie({'': None})})})})

sample2 = Trie({})
for word in ['a', 'an', 'and', 'was', 'wax', 'way', 'win']:
    sample2.add(word)
