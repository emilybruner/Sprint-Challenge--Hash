def has_negatives(a):
    storage = dict()
    result = list()

    for num in a:
        # check if the number has a matching value in the hash table
        if storage.get(abs(num)):
            # check to see if the sum adds up to 0
            if (storage.get(abs(num)) + num) == 0:
                # if the values match, append to result
                result.append(abs(num))

        else:
            # otherwise if no value is found, pass in the number as the new key
            storage[abs(num)] = num


    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
