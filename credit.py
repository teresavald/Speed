"""
Program to determine whether a provided credit card number is valid according to Luhn's algorithm
@by: Teresa Valdez
"""

def check_len(number):
    """
    Determine if length of number is valid
    :param number: Credit card number
    :return: String with card type if valid
    """
    if len(number) == 15 and number[0]+number[1] in ("34", "37"):
        card = "AMEX"
    elif any([len(number) == 16, len(number) == 13]) and number[0] == "4":
        card = "VISA"
    elif len(number) == 16:
        card = "MASTERCARD"
    else:
        card = "INVALID"

    return card


def luhns_algorithm(digits):
    """
    :param digits: Array of ints from card number
    :return: Boolean value if card number is valid or not
    """
    luhns = []
    digits.reverse()
    for i in range(1, len(digits), 2):
        luhns.append(digits[i-1])
        step1 = digits[i] * 2
        if len(str(step1)) > 1:
            step2 = int(str(step1)[0]) + int(str(step1)[1])
            luhns.append(step2)
        else:
            luhns.append(step1)
    if len(digits) % 2 != 0:
        luhns.append(digits[len(digits)-1])

    if sum(luhns) % 10 == 0:
        return True
    else:
        return False


number = input("Number: ")
card = check_len(str(number))

if card is not "INVALID":
    luhns_result = luhns_algorithm([int(d) for d in str(number)])
    if luhns_result:
        print(card)
    else:
        print("INVALID")
else:
    print("INVALID")
