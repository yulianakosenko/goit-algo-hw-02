# Завдання 3: Перевірка симетричності дужок (необов'язкове)
def check_brackets(sequence):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in sequence:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return "Несиметрично"
            stack.pop()
    return "Симетрично" if not stack else "Несиметрично"

print("\n--- ПЕРЕВІРКА ДУЖОК ---")
tests = [
    "(){[1](1+3)(){}}",
    "(23(2-3);",
    "(11}"
]

for test in tests:
    print(f"{test}: {check_brackets(test)}")
