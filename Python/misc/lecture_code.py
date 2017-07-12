class OurClass(): 
    def __init__(self, name, location, size=0): 
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []
        if self.size >= 20: 
            self.at_capacity = True
        else: 
            self.at_capacity = False

    def __len__(self):
        return len(self.questions_asked)

    def __str__(self):
        our_class_string = '{}, location: {}'
        return our_class_string.format(self.name, self.location)

    def __eq__(self, other):
        return self.name == other.name and self.location == other.location

    def add_question_asked(self, question): 
        self.questions_asked.append(question)
    
    def add_class_members(self, num): 
        self.size += num

        if self.size >= 20: 
            print('Capacity Reached!!')
            self.at_capacity = True

    def check_if_at_capacity(self): 
        return self.at_capacity


from collections import Counter

class ReportCreator():
    def __init__(self):
        self.vocabulary = set()
        self.master_counts_dict = Counter(sentences=0, words=0, characters=0)

    def create_reports(self, file_paths):
        for file_path in file_paths:
            self.create_report(file_path)

    def create_report(self, file_path):
        counts_dict = Counter(sentences=0, words=0, characters=0)
        with open(file_path) as txt_file:
            for line in txt_file:
                self._update_counts(line, counts_dict)
            self.master_counts_dict += counts_dict
        return counts_dict

    def _update_counts(self, line, counts_dict):

        def update_words(word):
            counts_dict['words'] += 1
            self.vocabulary.add(word)
            return ''

        word = ''
        for char in line:
            counts_dict['characters'] += 1
            if char in '?.!':
                counts_dict['sentences'] += 1
            elif char == ' ':
                word = update_words(word)
            else:
                word += char.lower()
        update_words(word)

    def __len__(self):
        return len(self.vocabulary)
