""" Task 1.3 """

def exploded_chains(lst):

    for l in lst:
        for i, ele in enumerate(l):
            if i < len(l) - 3:
                if ele == l[i+1] - 1 and ele == l[i+2] - 2:
                    l.remove(l[i])
                    l.remove(l[i])
                    l.remove(l[i])

    return lst
    
def main():

    encoded_lists = [ 
        [1, 2, 3, 4, 6],
        [5, 7, 8, 9, 15],
        [12, 14, 16, 18],
        [10, 11, 12, 13, 16, 17, 18, 20]
    ]

    print(exploded_chains(encoded_lists))

if __name__ == "__main__":
    main()