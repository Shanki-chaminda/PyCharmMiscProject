talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter loats:"))

total_lots = (talents * 20 * 32)+(pounds * 32) + lots

total_grams = total_lots * 13.3

kilograms = int(total_grams // 100)
grams = total_grams % 100

print(f"\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:2f} grams.")