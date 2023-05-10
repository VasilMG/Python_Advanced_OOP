class vowels:
    vowel_chars = "eyuioa"
    def __init__(self, text):
        self.text = text
        self.indx = 0

    def __iter__(self):
        return self
    # with generator --> return(x for x in self.text if x in self.vowels_chars)

    def __next__(self):
        while self.indx < len(self.text):
            if self.text[self.indx].lower() not in self.vowel_chars:
                self.indx += 1
                continue
            value_to_return = self.text[self.indx]
            self.indx += 1
            return value_to_return

        raise StopIteration
