#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu

# Date: Nov. 23, 2022
# a programs that adds the numbers
# the user inputs for a given amount of numbers


def main():
    # variables
    counter = 0
    sum_of_nums = 0
    sum_displayed = ""

    # exception handling
    try:
        # getting user input as an int
        amount_of_nums = int(input("How many numbers do you want to add? "))

    # user didn't input an integer
    except Exception:
        print("Invalid input! Please enter a whole number!")

    # user input is an integer
    else:
        # user input is negative
        if amount_of_nums < 0:
            print("Invalid input! Please enter a whole number!")

        # user input is whole
        else:
            while counter < amount_of_nums:
                # exception handling
                try:
                    # gets what number the user wants to add
                    user_num = int(input("Enter the number you would like to add: "))

                # user didn't input an integer
                except Exception:
                    print("Invalid input! Please enter a whole number!")

                # user input is an integer
                else:
                    counter += 1
                    sum_of_nums += user_num

                    # user num is not the last number to be added
                    if counter != amount_of_nums:
                        sum_displayed += f"{user_num} + "
                        continue

                    # user num is the last number to be added
                    else:
                        sum_displayed += f"{user_num} = {sum_of_nums}"
                        print(sum_displayed)


if __name__ == "__main__":
    main()
