class LoggerData:
    def __init__(self, filepath):
        self.logfile = open(filepath, 'r')

        self.data = self.logfile.read()
        self.clear_data = self.data
        for i in ',.?!':
            self.clear_data = self.clear_data.replace(i, '')

        split_data = self.clear_data.split()
        self.words = {word: 0 for word in split_data}
        for word in split_data:
            self.words[word] += 1

        letters_data = self.clear_data.replace(' ', '').replace('\n', '')
        self.letters = {letter: 0 for letter in letters_data}
        for letter in letters_data:
            self.letters[letter] += 1
        
        self.lines = self.data.count('\n') + 1
        self.most_long = max(map(lambda x: len(x), self.words))

    def words_frequency(self):
        for word in sorted(self.words):
            print( f"{' ' * (self.most_long - len(word))}{word}: {'*' * self.words[word]}")

    def letters_frequency(self):
        for letter in sorted(self.letters):
            print( f"{' ' * (self.most_long - 1)}{letter}: {'*' * self.letters[letter]}")

    def info(self):
        print('________________________________________________________________')
        print('Raw data:')
        print('________________________________________________________________')
        print(self.data)
        print('________________________________________________________________')
        print(f'Number of lines: {self.lines}')
        print('________________________________________________________________')
        print('Words frequency:')
        self.words_frequency()
        print('________________________________________________________________')
        print('Letters frequency:')
        self.letters_frequency()
        print('________________________________________________________________')


logdata = LoggerData('log')
logdata.info()
