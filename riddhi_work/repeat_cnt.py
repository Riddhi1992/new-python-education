# WAP which takes string or list and give you result, how many times a single element repeat in string or list.

import collections


def repeat(values):
    if type(values) == list:
        result = []
        for val in range(0, len(values)):
            if type(values[val]) == str and len(values[val]) > 1:
                x = list(collections.Counter(values[val]).elements())
                for y in range(0, len(x)):
                    result.append(x[y])
            else:
                result.append(values[val])
        final_result = collections.Counter(result)
        return final_result

        # for key, count in final_result.iteritems():
        #     return key, count
    else:
        return "User input should be a list type, not a number."


repeat([1, 2, 'riddhipatel', 22, 33, 22, 22])

# repeat(-1)
