def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    storage = dict()
    # store values as keys and index corresponding as values

    for i in range(length):
        y = storage.get(limit-weights[i])
        if y != None:
            #return tuple with the correct indices
            return (i, y)
        else:
            storage[weights[i]] = i

    print(storage)

    return None

    # for i, weight in enumerate(weights):
    #     if limit - weight in storage:
    #         return ([storage[limit-weight], i])
    #         break
    #     storage[weight] = i
    # return ([])


    # for i, weight in enumerate(weights):
    #     n = limit - weight
    #     if n not in storage:
    #         storage[weight] = i
    #     else:
    #         return [storage[n], i]
