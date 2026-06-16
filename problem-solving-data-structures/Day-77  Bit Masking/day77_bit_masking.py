# ==========================================================
# Author      : Saloni Tiwari
# Topic       : Bit Masking
# Day         : 77
# Description : Basic Bit Masking operations.
# ==========================================================

number = 5

print("Original Number:")

print(number)

# Set Bit at Position 1
set_bit = number | (1 << 1)

print("\nSet Bit 1:")

print(set_bit)

# Clear Bit at Position 2
clear_bit = number & ~(1 << 2)

print("\nClear Bit 2:")

print(clear_bit)

# Toggle Bit at Position 1
toggle_bit = number ^ (1 << 1)

print("\nToggle Bit 1:")

print(toggle_bit)

# Check Bit at Position 2
check_bit = number & (1 << 2)

print("\nIs Bit 2 Set?")

print(bool(check_bit))