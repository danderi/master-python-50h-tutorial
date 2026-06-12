# Your code here
def sequence_of_words(words):
    aux = sorted(words.split(","))
    wrd = ""
    for i in aux:
        if i == aux[-1]:
            wrd += i
        else:
            wrd += i+","
    return wrd

print(sequence_of_words("without,hello,bag,world"))