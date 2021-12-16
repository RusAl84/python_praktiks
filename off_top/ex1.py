import random


def gen_list(n):
    l = []
    for i in range(0, n):
        l.append(random.randrange(1, 10) * -1)
        l.append(random.randrange(1, 10) )
    return l

def get_min_n_el(l):
    min_n_el=0
    for item in l:
        if item < 0:
            min_n_el=item
    for item in l:
        if item < 0:
            if min_n_el < item:
                min_n_el = item
    return min_n_el

def main():
    l=[]
    l = gen_list(5)
    print(l)
    print(get_min_n_el(l))

if __name__ == '__main__':
    main()