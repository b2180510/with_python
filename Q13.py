import MeCab

def print_words_and_results(raw_text: str = 'すもももももももものうち'):
    togger = MeCab.Tagger()
    parse = togger.parse(raw_text)
    print(parse)

def print_morpheme(raw_text: str = 'すもももももももものうち'):
    togger = MeCab.Tagger()
    parse = togger.parse(raw_text)
    nouns = [line for line in parse.splitlines() if "名詞" in line.split()[-1]]
    for str in nouns:
        print(str.split())

if __name__ == '__main__':
    print_words_and_results() #Q1.3.1
    print_morpheme() #Q1.3.2
