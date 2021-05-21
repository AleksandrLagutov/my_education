with open('dataset_24465_4.txt', 'r') as inf, open('out.txt', 'w') as outf:
    inp_list = inf.readlines()
    for line in inp_list[::-1]:
        outf.write(line)
