# for i in range(3):
#     for j in range(3):
#         a = i * 2
#         b = j * 3
#         c = a + b
#         # print(f"第{i + 1}")
#         # print(f"a = {a}")
#         # print(f"b = {b}")
#         # print(f"c = {c}")
#         # print()

# list = ["A", "B", "C"]
# for i in range(3):
#     for j in list:
#         print(j * i)

list2 = [{'B':8}, {'B':9}, {'B':10}]
print([i['B'] for i in list2]) #[i['B'] for i in list2]會產生列表

list1 = [{"A":1}, {"A":2}, {"A":3}]
s = [i['A'] for i in list1]
print(1 in [i['A'] for i in list1])
print(4 in [i['A'] for i in list1])

print(s.index(2))