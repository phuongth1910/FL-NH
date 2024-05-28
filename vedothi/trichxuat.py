import re

# Dữ liệu đã cho
log_data = """
2024-03-28 14:34:56,344 - Round:11 - Active clients:[46 49 22 58 41 98 62 29 30 51]:
2024-03-28 14:35:01,579 -  Training time:5.233 seconds
2024-03-28 14:35:14,158 -  Testing time:12.567 seconds
2024-03-28 14:35:14,158 -  avg_test_acc: {'uniform': 0.334199994802475, 'validclass': 0.334199994802475, 'labeldist': 0.334199994802475}
2024-03-28 14:35:14,159 -  pfl_avg_test_acc: {'uniform': 0.20923000127077102, 'validclass': 0.2798089310526848, 'labeldist': 0.6763922333717346}
2024-03-28 14:35:14,159 - Round:12 - Active clients:[17 41 92 14 68 31 89 15 21 60]:
2024-03-28 14:35:21,171 -  Training time:7.009 seconds
2024-03-28 14:35:33,871 -  Testing time:12.689 seconds
2024-03-28 14:35:33,872 -  avg_test_acc: {'uniform': 0.321399986743927, 'validclass': 0.321399986743927, 'labeldist': 0.321399986743927}
2024-03-28 14:35:33,872 -  pfl_avg_test_acc: {'uniform': 0.21417000368237496, 'validclass': 0.31509559154510497, 'labeldist': 0.6849632501602173}
# Các dòng log khác ở giữa
"""

# Tìm tất cả các khớp với avg_test_acc
matches = re.findall(r'avg_test_acc: (.+)', log_data)

# Lọc ra giá trị avg_test_acc từ các kết quả khớp
avg_test_acc_values = [eval(match)['uniform'] for match in matches]

# In ra giá trị avg_test_acc
print(avg_test_acc_values)
