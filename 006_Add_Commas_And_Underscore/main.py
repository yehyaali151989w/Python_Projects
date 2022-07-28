def add_commas_and_underscore(num):

  # Use Commas As Thousands Separator
  # formatted_num = "{:,}".format(num) # Old Way
  formatted_num = f"{num:,}"  # New Way

  # Check if Number > 3

  if len(formatted_num) > 3:

    # Convert To List
    to_list = formatted_num.split(",")

    # Get First Part
    first = to_list[:-1]

    # Join First Part Element
    first_join = "".join(first)

    # Convert To Int
    first_int = int(first_join)

    # Formatting The First Part
    first_format = f"{first_int:,}"

    # Concatenate All
    final_result = f"{first_format}_{to_list[-1]}"

    return final_result

  return formatted_num


print(add_commas_and_underscore(120))  # 120
print(add_commas_and_underscore(1530))  # 1_530
print(add_commas_and_underscore(120510650))  # 120,510_650
print(add_commas_and_underscore(510650480910))  # 510,650,780_910
print(add_commas_and_underscore(12069057014032))  # 12,069,057,014_032
