sentence = "apple banana apple orange banana apple"
split_sentence = sentence.split(" ")
fruits = {}
for fruit in split_sentence:
    if fruit not in fruits:
        fruits[fruit] = 1
    else:
        fruits[fruit] += 1
for key, value in fruits.items():
    print(f"{key} : {value}")