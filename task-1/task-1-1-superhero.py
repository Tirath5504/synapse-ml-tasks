""" Task 1.1 of Synapse """

def main():
    
    jumbled_superheroes = ["DocToR_sTRAngE", "sPidERmaN", "MoON_Knight", "caPTAIN_aMERIca", "hULK"]
    indices, decoded_names = [], []

    for index, name in enumerate(jumbled_superheroes):
        indices.append(index)
        decoded_names.append(jumbled_superheroes[index].lower().replace("_", " "))

    name_lengths = list(map(lambda name: len(name), decoded_names))

    indices.sort(key= lambda index: name_lengths[index])

    i = 1

    print("Phase 5 kickoff list :")
    for index in indices:
        print(f"{i}. {decoded_names[index].title()}")
        i += 1

if __name__ == "__main__":
    main()