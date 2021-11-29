text = open("D:\lab4.txt", "r+")
stop_words = ['або', 'но', 'до',  'потім',   'для', 'на', 'по',  'от',  'без', 'над', 'під', 'за', 'при',  ]

words = text.read().split()
words_number = 0
stop_words_number = 0

for word in words:
    words_number += 1

    if word in stop_words:
        stop_words_number += 1

water_percentage = stop_words_number / words_number

print(water_percentage * 100)