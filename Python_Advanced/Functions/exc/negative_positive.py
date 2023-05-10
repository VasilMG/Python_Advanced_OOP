
def stronger(*args):
    positive = [int(x) for x in args[0] if int(x) >0]
    negative = [int(y) for y in args[0] if int(y) < 0]
    if sum(positive) > abs(sum(negative)):
        message = "The positives are stronger than the negatives"
    else:
        message = "The negatives are stronger than the positives"
    return sum(negative), sum(positive), message

negative_sum,positive_sum, the_message =  stronger(input().split())
print(negative_sum)
print(positive_sum)
print(the_message)

