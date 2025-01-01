number_count = int(input("Nechta son kiritmoqchisiz: "))

numbers = [int(input(f"{i + 1}-sonni kiriting: ")) for i in range(number_count)]

valid_numbers = [num for num in numbers if num % 2 == 1 and num % 3 == 0]

if valid_numbers:
    print("✅ Quyidagi sonlar toq va 3 ga bo'linadi:")
    print(" ".join(map(str, valid_numbers)))
else:
    print("❌ Toq va 3 ga bo'linadigan son topilmadi.")