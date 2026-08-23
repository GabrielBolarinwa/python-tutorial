print("Credit Card Validator")
credit_card = input("Enter your credit card number: ")
credit_card = credit_card.replace("-", "")
credit_card = credit_card.replace(" ", "")
credit_card = credit_card[::-1]

sum_of_odd_digits = 0
sum_of_even_digits = 0

for num in credit_card[::2]:
    sum_of_odd_digits += int(num)

for num in credit_card[1::2]:
    num = int(num) * 2
    if num >= 10:
        sum_of_even_digits += (1 + (num % 10))
    else:
        sum_of_even_digits += num

total = sum_of_odd_digits + sum_of_even_digits
print(total)

if total % 10 == 0:
    print("Your credit card is valid")
else:
    print("Your credit card is not valid")
