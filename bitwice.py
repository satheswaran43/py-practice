# Bitwise AND (&):
# Compares corresponding bits of two operands.
# If both bits are 1, the resulting bit is 1; otherwise, it's 0.
# Example: 5 & 3 (binary 101 & 011) results in 001, which is decimal 1.

# Bitwise OR (|):
# Compares corresponding bits of two operands.
# If at least one bit is 1, the resulting bit is 1; otherwise, it's 0.
# Example: 5 | 3 (binary 101 | 011) results in 111, which is decimal 7.

# Bitwise XOR (^):
# Compares corresponding bits of two operands.
# If exactly one bit is 1, the resulting bit is 1; otherwise, it's 0.
# Example: 5 ^ 3 (binary 101 ^ 011) results in 110, which is decimal 6.

# Bitwise NOT (~):
# Inverts all the bits of a single operand.
# This is equivalent to -(x + 1).
# Example: ~5 (binary ~101) results in -(5 + 1), which is -6.

# Left Shift (<<):
# Shifts the bits of the left operand to the left by the number of positions specified by the right operand.
# Effectively multiplies the number by 2 raised to the power of the shift amount.
# Example: 5 << 2 (binary 101 << 2) results in 10100, which is decimal 20.

# Right Shift (>>):
# Shifts the bits of the left operand to the right by the number of positions specified by the right operand.
# Effectively divides the number by 2 raised to the power of the shift amount (integer division).
# Example: 5 >> 2 (binary 101 >> 2) results in 001, which is decimal 1.
# Note: Bitwise operators in Python exclusively work on integer types. The result of a bitwise operation is always an integer.

