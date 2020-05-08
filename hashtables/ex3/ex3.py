def intersection(arrays):

    storage = dict()
    # list that will hold intersections
    result = []

    #iterating over the arrays list
    for i, nums in enumerate(arrays):
        #then iterate over each list within the arrays list
        for j in nums:
            # if an item has an instance in the hash table, and the index is > 1, increase the storage count
            if storage.get(j) != None and i > 0:
                # pass the number as a key, then increase the count by 1
                storage[j] = storage[j] + 1
            #otherwise if there is no record of that number in the dictionary and index is one (aka still iterating on first array)
            elif storage.get(j) is None and i == 0:
                #set initial count to 1
                storage[j] = 1
            else:
                continue

    # iterating over each hash table entry
    for num in storage:
        # if the storage length is equal to the array length
        if storage[num] == len(arrays):
            # append num to the result
            result.append(num)


    return result




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
