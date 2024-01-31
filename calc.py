pie_made_of = [
    "Мука",
    "Сахар",
    "Масло",
    "Яблоки",
    "Корица",
    "Ваниль",
    "Соль",
    "Вода",
    "Яйца",
    "Молоко",
    "Сода",
    "Разрыхлите",
]
quantities = [100, 50, 75, 200, 5, 5, 2, 100, 50, 100, 1, 1]

import matplotlib.pyplot as plt

plt.pie(quantities, labels=pie_made_of, autopct="%1.1f%%")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
