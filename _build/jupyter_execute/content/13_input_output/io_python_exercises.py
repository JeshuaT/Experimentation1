#!/usr/bin/env python
# coding: utf-8

# # Python exercises: Decimal versus binary notation

# ### Exercise 1. Convert a binary number to a decimal number
# 
# To convert a binary number to a decimal value you can use the int function as shown in the example below. Write python code that converts an 8-bit binary number (provided  by the user as a string of eight zeros and ones) to a decimal value and print this value using a loop. Check the result by comparing the value to the table provided in today's lessons.
# 
# > **Hint** To convert an 8-bit binary number to a decimal value, first assign each bit a weight based on its position in the binary number. The rightmost bit, or least significant bit, has a weight of 1, the next bit to the left has a weight of 2, the next bit has a weight of 4, and so on.
# >
# > Next, determine the decimal value of each bit by multiplying its weight by its value (1 for a 1 and 0 for a 0). For example, if the binary number is 11011011, the decimal value of the rightmost bit is 1 (1 * 2^0), the decimal value of the next bit is 2 (1 * 2^1), the decimal value of the next bit is 0 (0 * 2^2), and so on.
# >
# > Finally, add up the decimal values of each bit to find the total decimal value of the binary number. In the example above, the total decimal value is 128 + 64 + 0 + 16 + 8 + 0 + 2 + 1 = 219.
# 

# In[33]:


# Get the binary number from the user
binary_number = input("Enter an 8-bit binary number: ")

# Convert the binary number to a decimal value
# write your own code here (that replaces the line below)
decimal_value = int(binary_number, 2)

# Print the decimal value
print(decimal_value)


# ### Exercise 2. Convert a decimal number to a binary number
# 
# Let's now do the opposite. To convert a decimal number to a binary value you can use the format function (the bin function also works but uses a different notation). Write python code that converts a decimal number (provided via by the user) to an 8-bit binary number  and print this value using a loop. Check the result by comparing the value to the table provided in today's lessons.
# 
# > **Hint** To convert a decimal value to an 8-bit binary number, first divide the decimal value by 2 and take the remainder. The remainder will be the rightmost bit of the binary number, with a value of either 0 or 1.
# >
# >Next, divide the quotient of the previous step by 2 and take the remainder. This remainder will be the next bit to the right in the binary number. Repeat this process until the quotient becomes 0, resulting in an 8-bit binary number.
# >
# > For example, to convert the decimal value 13 to an 8-bit binary number, we first divide 13 by 2 and take the remainder, which is 1. The quotient is 6. We then divide 6 by 2 and take the remainder, which is 0. The quotient is 3. We repeat this process until the quotient becomes 0, resulting in the binary number 1101. We then add zeros before the until we have 8-bits: 00001101.

# In[ ]:


# Get the decimal number from the user
decimal_value = input("Enter a decimal value between 0 and 255: ")

# Convert the decimal value to a binary value
# write your own code here (that replaces the line below)
binary_number_s = format(int(decimal_value),'08b')

# Print the binary value
print(binary_number_s)

