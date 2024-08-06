from fake_math import divide as fake_div
from true_math import divide as true_div


print(f"результат школьного деления 69 на 3: {fake_div(69, 3)}")
print(f"результат школьного деления 3 на 0: {fake_div(3, 0)}")
print(f"результат нормального деления 49 на 7, а не этих ваших:{true_div(49, 7)}")
print(f"результат нормального деления 15 на 0, а не этих ваших:{true_div(15, 0)}")
