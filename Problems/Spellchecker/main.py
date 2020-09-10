dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()
misspelled = [word for word in words if word not in dictionary]
if len(misspelled) == 0:
    print("OK")
else:
    for word in misspelled:
        print(word)
