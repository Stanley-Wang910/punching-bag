def solve():
    input = list(map(int, input().split()))
    n = input[0]
    m_len = input[1]
    moves = input[2 : 2 + m_len]
    arr = [False] * (n + 1)
    arr[0] = False

    for i in range(1, n + 1):
        for j in range(m_len):
            if i - moves[j] >= 0 and arr[i - moves[j]] == 0:
                arr[i] = True
                break
    if arr[n] == True:
        print("Stan wins")
    else:
        print("Ollie wins")


solve()


import sys


def bachets_game():
    for line in sys.stdin:
        # Split the input line into a list of integers
        numbers = list(map(int, line.split()))

        if not numbers:
            break

        n = numbers[0]  # stones
        m = numbers[1]  # number of moves
        moves = numbers[2:]  # list of possible moves

        arr = [0] * (n + 1)
        arr[0] = 0

        for i in range(1, n + 1):
            for move in moves:
                if i - move >= 0 and arr[i - move] == 0:
                    arr[i] = 1
                    break

        if arr[n] == 1:
            print("Stan wins")
        else:
            print("Ollie wins")


if __name__ == "__main__":
    bachets_game()
