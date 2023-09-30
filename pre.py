with open('data.txt', 'r') as f:
    lines = f.readlines()
    with open('dataset.txt', 'x') as n:
        for line in lines:
            for sentence in line.split('. '):
                n.write(sentence)
                n.write('\n')

sentences = []
with open('dataset.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if(len(line) > 3):
            sentences.append(line)

with open('dataset_new.txt', 'x') as n:
    for line in sentences:
        n.write(line)
