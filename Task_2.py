# Завдання 2: Перевірка на паліндром
from collections import deque

def is_palindrome(input_string):
    cleaned = ''.join(filter(str.isalnum, input_string)).lower()
    d = deque(cleaned)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Приклади
print("\n--- ПЕРЕВІРКА НА ПАЛІНДРОМ ---")
examples = ["racecar", "A man a plan a canal Panama", "hello", "Was it a car or a cat I saw"]
for ex in examples:
    result = "є паліндромом" if is_palindrome(ex) else "не є паліндромом"
    print(f"\"{ex}\" -> {result}")
