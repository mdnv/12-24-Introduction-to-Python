income = int(input("Введите ваш ежемесячный доход (сом): "))
expenses = float(input("Введите ваши ежемесячные расходы (сом): "))

balance = income - expenses
print(f"Ваш остаток бюджета: {balance} сом")

message = ["Вы в плюсе!", "Ваши расходы превышают доходы!"][balance < 0]
print(message)