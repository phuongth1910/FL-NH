import matplotlib.pyplot as plt
# Đọc nội dung từ file log
log_file_path = "ket-qua.log"
with open(log_file_path, "r") as log_file:
    log_data = log_file.readlines()

# Lọc dữ liệu từ log
avg_test_acc_data = []
for line in log_data:
    if "avg_test_acc" in line:
        avg_test_acc_data.append(line)

# Trích xuất giá trị từ pfl_avg_test_acc
extracted_data = []
for line in avg_test_acc_data:
    data_start = line.find("{") + 1
    data_end = line.find("}")
    data_str = line[data_start:data_end]
    pairs = data_str.split(", ")
    data_dict = {}
    for pair in pairs:
        key, value = pair.split(": ")
        data_dict[key.strip("'")] = float(value)
    extracted_data.append(data_dict)

print(extracted_data)

# pfl_test_acc_values = [extracted_data['validclass'] for round_data in extracted_data]
# Tạo danh sách chứa giá trị validclass từ từng từ điển trong extracted_data
test_acc_values = [round_data['labeldist'] for round_data in extracted_data]

# Tạo danh sách các vòng lặp
rounds = list(range(1, len(test_acc_values) + 1))
print(rounds)

# Vẽ đồ thị
plt.plot(rounds, test_acc_values, marker='o', linestyle='-')
plt.xlabel('Round')
plt.ylabel('avg_test_acc')
plt.title('GM')
plt.grid(True)
plt.show()

