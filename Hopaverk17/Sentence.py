class Sentence():
    def __init__(self,word):
        self.word = word

    def get_first_word(self):
        splitt = self.word.split()
        first = splitt[0]
        return first

    def get_all_words(self):
            word = self.word.split()
            return word

    def replace(self,index,new_word):
        word = self.word.split()
        try:
            word[index] = new_word
            self.word = " ".join(word)
        except IndexError:
            pass


sent = Sentence('Here we have a longer sentence')
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(2, "find")
print(sent.get_all_words())
sent.replace(10,"bla")
print(sent.get_all_words())

assert str(sent.get_all_words()) == "['Here', 'we', 'find', 'a', 'longer', 'sentence']"