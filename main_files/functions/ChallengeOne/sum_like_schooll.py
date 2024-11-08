from itertools import zip_longest

# this is other test here


def sum_like_in_school(number_1, number_2, base=10):
    digits_zipped = zip_longest(
        reversed(str(number_1)), reversed(str(number_2)), fillvalue=0
    )
    carry = 0
    result = ""
    for digit_1, digit_2 in digits_zipped:
        sum_of_two_digits = int(digit_1) + int(digit_2) + carry
        if sum_of_two_digits >= base:
            carry = 1
            result = str(sum_of_two_digits % base) + result
        else:
            carry = 0
            result = str(sum_of_two_digits) + result
    return int(result)


print(sum_like_in_school(1564, 587, 10))
