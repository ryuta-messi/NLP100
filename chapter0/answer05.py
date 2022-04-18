from typing import List


def n_gram(n, sentence: List[str]):
    return list(zip(*[sentence[i:] for i in range(n)]))


# list(zip(*[['I', 'am', 'an', 'NLPer'],['am', 'an', 'NLPer']])) -> [('I', 'am'), ('am', 'an'), ('an', 'NLPer')]
if __name__ == "__main__":
    str = "I am an NLPer"
    words_bi_gram = n_gram(2, str.split())
    char_bi_gram = n_gram(2, str)

    print(words_bi_gram)
    print(str.split())
