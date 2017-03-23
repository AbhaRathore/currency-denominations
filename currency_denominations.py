import math

amount = eval(input("Enter the amount:"))
amount_in_cent = amount * 100
dollar_count = amount_in_cent // 100
remaining_cents = amount_in_cent % 100

quarter_count = remaining_cents // 25
remaining_cents %= 25

dimes_count = remaining_cents // 10
remaining_cents %= 10

nickles_count = remaining_cents // 5
remaining_cents %= 5

pennies = remaining_cents

print("Your amount", amount, "consists of:\n ", dollar_count, "Dollars, ", quarter_count, "Quarters, ",
      dimes_count, "Dimes, ", nickles_count, "Nickles, and", pennies, "Pennies")

