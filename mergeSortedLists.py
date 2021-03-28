# import pdb
# pdb.set_trace
def mergeLists(coll1, coll2):
    n = len(coll1)
    m = len(coll2)
    total_n = n + m
    i = 0
    j = 0
    merged_collection = []

    while(i < n and j < m):
        import pdb
        pdb.set_trace
        if(coll1[i] > coll2[j]):
            merged_collection.append(coll2[j])
            j += 1
        elif(coll1[i] < coll2[j]):
            merged_collection.append(coll1[i])
            i += 1
        else:
            merged_collection.append(coll1[i])
            i += 1
            j += 1

    return merged_collection + coll1[i:] + coll2[j:]


def readInput():
    collections = []
    for i in range(0, 2):
        print("collection_{}".format(i + 1))
        collection = []

        curr_number = int(input('Enter a number: '))
        last_number = curr_number - 1

        while (curr_number > last_number):
            collection.append(curr_number)
            last_number = curr_number
            curr_number = int(input('Enter a number: '))
        collections.append(collection)

    print(collections)
    return collections
    # print(mergeLists(collections[0], collections[1]))


if __name__ == "__main__":

    collections = readInput()
    print(mergeLists(collections[0], collections[1]))
    # c1 = [2, 5, 7, 10, 14, 15]
    # c2 = [1, 6, 7, 8]
    # print(mergeLists(c1, c2))
