class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Enter amount to add: "))
        self._balance += amount
        print(f"New balance: {self._balance}")

    def _kill(self):
        self._balance = 0
        print("Balance has been reset to 0.")

    def __jackpot(self):
        self._balance *= 10
        print(f"Jackpot! New balance: {self._balance}")

    def _merge_balance(self, other):
        if isinstance(other, Bank):
            self._balance += other._balance
            print(f"Merged balance: {self._balance}")

    def __str__(self):
        return f"{self._name}: {self._balance}"

# Example usage
if __name__ == "__main__":
    my_account = Bank("MyAccount", 100)
    other_account = Bank("OtherAccount", 100)

    print(my_account)
    my_account.moneyX()
    my_account._kill()
    my_account._Bank__jackpot()  # Accessing private method
    my_account._merge_balance(other_account)
    print(my_account)


class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value + other.value)
        return Calculator(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value - other.value)
        return Calculator(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value * other.value)
        return Calculator(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value / other.value)
        return Calculator(self.value / other)

    def __str__(self):
        return str(self.value)



if __name__ == "__main__":
    calc1 = Calculator(50000)
    calc2 = Calculator(25000)

    print(calc1 + calc2)
    print(calc1 - calc2)
    print(calc1 * calc2)
    print(calc1 / calc2)
