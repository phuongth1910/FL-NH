# About FedNH - Ha Phuong

- [ ]  Chạy CML bộ dữ liệu Braintumor-Cifar10-TinyImageNet với các model Resnet, ConvCifar, Model trên kaggle.
⇒ Sau đó so sánh các kết quả accuracy, thời gian trainning (tính theo số round), … | đồ thị
⇒ Trích ra các confusion matrix tương ứng
- [ ]  Chạy FedNH với bộ dữ liệu Braintumor + Cifar10 + TinyImageNet
⇒ So sánh ưu điểm & nhược điểm.
⇒ Ứng dụng được vào trong hệ thống như nào (bệnh viện, …)
- [ ]  Vẽ confusion matrix trên từng client trong FedNH và đánh giá tại sao model kia có độ chính xác cao như vậy?

# Xử lý dữ liệu hàm transform biến đổi ảnh đầu vào:

```jsx
# data augmentation
image_size = (224,224)
train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(), # tăng cường dữ liệu
    transforms.RandomVerticalFlip(), # tăng cường dữ liệu
    transforms.RandomRotation(10),
    transforms.Resize(image_size),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

test_transform = transforms.Compose([
    transforms.Resize(image_size),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
```

- **`mean`**: Đại diện cho giá trị trung bình của từng kênh màu (R, G, B) trong tập dữ liệu huấn luyện.
- **`std`**: Đại diện cho độ lệch chuẩn của từng kênh màu (R, G, B) trong tập dữ liệu huấn luyện

Dữ liệu có được tăng cường so với bộ dữ liệu ban đầu.

# Về Model thu thập trên kaggle

Hiện tại chưa thấy gì đặc biệt

```jsx
class MyModel(nn.Module):
    def __init__(self,num_classes):
        super(MyModel,self).__init__()
        
        self.conv1 = nn.Conv2d(3,32,kernel_size=4,stride=1,padding=0)
        self.bn1 = nn.BatchNorm2d(32)
        
        self.conv2 = nn.Conv2d(32,64,kernel_size=4,stride=1,padding=0)
        self.bn2 = nn.BatchNorm2d(64)
        
        self.conv3 = nn.Conv2d(64,128,kernel_size=4,stride=1,padding=0)
        self.bn3 = nn.BatchNorm2d(128)
        
        self.conv4 = nn.Conv2d(128,128,kernel_size=4,stride=1,padding=0)
        self.bn4 = nn.BatchNorm2d(128)
        
        self.pool = nn.MaxPool2d(kernel_size=3, stride=3)
        self.pool2= nn.MaxPool2d(kernel_size=3, stride=2)
        
        self.fc1 = nn.Linear(6*6*128,512)
        self.fc2 = nn.Linear(512,num_classes)
        
        self.flatten = nn.Flatten()
        self.relu = nn.ReLU() 
        self.dropout = nn.Dropout(0.5)
        
        
        
        
    def forward(self,x):
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.pool(x)
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.pool(x)
        x = self.relu(self.bn3(self.conv3(x)))
        x = self.pool2(x)
        x = self.relu(self.bn4(self.conv4(x)))
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
```

****Chi tiết trong kaggle.ipynb code ****

Trên kaggle chạy là cứ khi nào accuracy model không tăng thì nó bỏ cái model đó luôn, chỉ lấy model trả về acc cao nhất, dẫn đến acc cuối rất cao.

Khi mà qua khoảng 5-7 epoch mà accuracy không tăng nữa thì nó lấy model cuối cùng đó.

⇒ **Vấn đề:** Model tổng hợp không khái quát được toàn bộ dữ liệu mà chỉ có accuracy cao nhất đối với tập valid thôi

⇒ Nhưng cũng chưa rõ tại sao cho vào FedNH nó cũng trả về accuracy rất là cao? —> WHY?

```
git add . ':(exclude)data/*'
```