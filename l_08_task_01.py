# Урок 8, задача №1
# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество
# различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def count_substring(s):
    hashes = set()
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring and substring != s:
                hash_ = hashlib.sha1(substring.encode('utf-8')).hexdigest()
                hashes.add(hash_)
    return len(hashes)


print(count_substring('papa'))
print(count_substring('sova'))
