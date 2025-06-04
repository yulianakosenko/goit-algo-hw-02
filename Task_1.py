# Завдання 1: Система обробки заявок
import queue
import time
import random

request_queue = queue.Queue()
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Заявка #{request_id}"
    request_queue.put(request)
    print(f"Створено: {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється: {request}")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Демонстрація роботи
print("--- СИСТЕМА ОБРОБКИ ЗАЯВОК ---")
for _ in range(5):
    generate_request()
    time.sleep(0.5)

for _ in range(6):
    process_request()
    time.sleep(0.5)