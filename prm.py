
num_elements = int(input())


input_list = []
for _ in range(num_elements):
    input_list.append(input())


sorted_list = sorted(input_list, key=lambda x: x[-2])

print(sorted_list)
