## type hinting

'''
def list_avg(sequence):
    return sum(sequence) / len(sequence)

list_avg(123)

'''
## this gives us error when we run the code but no error while typing it

## this is because we havent specified that sequence must be a list

## type hinting done properly
def list_avg1(sequence: list) -> float:         # here we have hinted that sequence is type list and return value is type float
    return sum(sequence) / len(sequence)

list_avg1([1, 2, 3, 4, 5])
print(list_avg1)