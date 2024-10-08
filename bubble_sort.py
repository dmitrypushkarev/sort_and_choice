# Алгоритм
# Сначала сравниваются первые два элемента списка.
# Если первый элемент больше, они меняются местами.
# Если они уже в нужном порядке, оставляем их как есть. Затем переходим к следующей паре элементов,
# сравниваем их значения и меняем местами при необходимости.
# Этот процесс продолжается до последней пары элементов в списке.
import random

nums = [random.randint(-100, 100) for _ in range(20)]
print("before sort = ", nums)
swapped = True
j = 0
while swapped:
    swapped = False
    j += 1
    print("*****")
    for i in range(len(nums) - j):
        print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
print("after sort = ", nums)
