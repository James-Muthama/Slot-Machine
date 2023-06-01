import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
    for column in columns:
        symbol_to_check = column[line]
        if symbol != symbol_to_check:
            break
    else:
        winning_lines.append(line + 1)
        winnings += values[symbol] * bet

    return winnings, winning_lines


def bet_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter amount that is greater than 0")
        else:
            print("Enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter number of lines you want to place bet on (1 -" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Enter a number of lines")

    return lines


def get_bet():
    while True:
        bet = input(f"Enter amount you want to place on per line? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a number")
    return bet


def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Your don't have enough money to place that bet, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}")

    slot = bet_slot_machine(ROWS, COLS, symbol_count)

    print_slot_machine(slot)

    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_value)

    print(f"You won ${winnings}.")
    print(f"You won on line:", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        input1 = input("Press enter to anything to play or 'q' to quit")
        if input1 == 'q':
            break

        balance += game(balance)

        print(f"You left with ${balance}")


main()
