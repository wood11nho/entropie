from math import log2
def update_probabilities(index):
    sum = 0
    for i in range(len(probabilities)):
        if i != index:
            sum += probabilities[i]
    for i in range(len(probabilities)):
        if i != index:
            upd_prob[i] = probabilities[i] / sum


out = open(r"input.txt", "r")
Input = out.read()
Input = Input.replace("%", " ")
Input = Input.replace(",", " ")
probabilities = [float(x) / 100 for x in Input.split()]
entropy = 0
for p in probabilities:
    entropy += p * log2(1 / p)
print(f"Entropia este {round(entropy, 2)} biti")

entropy_if_same_p = 0
even_prob = 1 / 26
for i in range(26):
    entropy_if_same_p = entropy_if_same_p + even_prob * log2(1 / even_prob)
print(f"Entropia daca toate literele ar avea aceeasi frecventa ar fi {entropy_if_same_p} biti")


upd_prob = [0] * 26
min_entropy = [10, 0]
max_entropy = [0, 0]
for i in range(len(probabilities)):
    update_probabilities(i)
    entropy_1 = 0
    for p in upd_prob:
        if p != 0:
            entropy_1 += p * log2(1 / p)
    if entropy_1 > max_entropy[0]:
        max_entropy = [entropy_1, chr(ord('a') + i)]
    elif entropy_1 < min_entropy[0]:
        min_entropy = [entropy_1, chr(ord('a') + i)]
    upd_prob = [0] * 26
    print(round(entropy_1, 4), chr(ord('a') + i))
print(f"Entropia maxima este {round(max_entropy[0], 4)} cand se elimina litera {max_entropy[1]}")
print(f"Entropia minima este {round(min_entropy[0], 4)} cand se elimina litera {min_entropy[1]}")