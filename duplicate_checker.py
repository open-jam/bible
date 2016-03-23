answers = {}

with open('README.md') as f:
    for line in f:
        if line.__contains__('\t*') is True:
            answer = line.split('\t*')[1]
            if answers.has_key(answer) is True:
                print 'duplicate answer', answer
                answers[answer] += 1
            else:
                answers[answer] = 1