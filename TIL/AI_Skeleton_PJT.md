## 1. 단순 선형 회귀 모델 구현

```python
$ python -m venv venv
$ source venv/Scripts/activate
(venv)
$ pip install tensorflow==2.0.0
$ pip install matplotlib scikit-learn tqdm scipy numpy tensorflow-gpu==2.0.0
```

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from models.linear_model import LinearModel
```

```python
# 데이터 불러오기
train_data = np.load(".\\datasets\\linear_train.npy")
test_x = np.load(".\\datasets\\linear_test_x.npy")
```

```python
# tf 형식에 맞게 변환
x_data = np.expand_dims(train_data[:,0], axis=1)
y_data = train_data[:,1]
```

```python
# 모델 생성
model = LinearModel(num_units=1)
```

```python
# 최적화 함수, 손실함수와 모델 바인딩 (학습 준비)
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
			  loss=tf.keras.losses.MSE,
			  metrics=[tf.keras.metrics.MeanSquaredError()])
```

```python
# 모델 학습
model.fit(x=x_data, 
		  y=y_data, 
		  epochs=10, 
		  batch_size=32)
```

```python
# 모델 테스트
prediction = model.predict(x=test_x,
    					   batch_size=None)
```

```python
# 결과 시각화
plt.scatter(x_data, y_data, s=5, label="train data")
plt.scatter(test_x,prediction,s=5,label="prediction data")
plt.show()
```

```python
# 모델 정리
model.summary()
```



## 2. 이미지 캡셔닝 configuration

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--caption_file_path', type=str, default='.\\datasets\\images\\results.csv')

config = parser.parse_args()

if config.caption_file_path:
    print('get_path_caption(' + config.caption_file_path + ')')
```

```python
from datetime import datetime
import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


# Req. 2-2	세팅 값 저장
def save_config():
	pass
```



## 3. 이미지 캡셔닝 데이터 전처리

```python
def get_path_caption():
    csv_data = np.loadtxt('../datasets/captions.csv', delimiter='|', dtype=np.str)
    csv_data = np.delete(csv_data, 0, 0)

    image_name = []
    comment = []
    for row in csv_data:
        img = row[0].strip('\"')
        image_name.append(img)
        comm = row[-1].strip(',').strip()
        comment.append(comm)
        
    return [image_name, comment]
	result = {}
    for row in csv_data:
        comment = row[-1].strip(',').strip()
        if bool(result.get(row[0])) == False:
            result[row[0]] = [comment]
        else:
            result[row[0]].append(comment)
    return result
```

```python
def dataset_split_save(dataset):
    train_x, test_x, train_y, test_y = train_test_split(dataset[0], dataset[1], shuffle=False)
```

```python
np.savez('../datasets/test_dataset.npz', x=test_x, y=test_y)
np.savez('../datasets/train_dataset.npz', x=train_x, y=train_y)
```

```python
def get_data_file(inp):
    if inp != 'train_x' and inp != 'test_x' and inp != 'train_y' and inp != 'test_y':
        return print('제대로 입력하셈')
    if inp[:4] == 'test':
        data = np.load('../datasets/test_dataset.npz')
        if inp[-1] == 'x':
            return print(data['x'])
        else:
            return print(data['y'])
    else:
        data = np.load('../datasets/train_dataset.npz')
        if inp[-1] == 'x':
            return print(data['x'])
        else:
            return print(data['y'])
```

```python
def get_data_file(inp):
    if inp != 'train' and inp != 'test':
        return print('제대로 입력하셈')
    data = np.load(f'{inp}_dataset.npz')

    result = {}
    img = data['x']
    comment = data['y']
    img_stan = img[0]
    idx = 1
    del_list = [0]

    while img != []:
        if idx >= len(img):
            break
        if img[idx] == img_stan:
            del_list.append(idx)
            idx += 1
        else:
            del_list.append(idx)
            com_list = []
            for com in comment[:idx]:
                com_list.append(com)
            result[img[idx]] = com_list
            img = np.delete(img, del_list, 0)
            comment = np.delete(comment, del_list, 0)
            img_stan = img[0]
            idx = 1
            del_list = [0]
    return result
```

```python
def sampling_data(rate):
    img, com = get_path_caption()
    
    dataset = []
    for i in range(len(img)):
        dataset.append(img[i] + ', ' + com[i])
    
    return np.random.choice(dataset, size=int(len(img) * float(rate) / 100), replace=False).tolist()
```

```python
import csv
import numpy as np
from sklearn.model_selection import train_test_split

dataset_split_save(get_path_caption())
print('train, test')
res = get_data_file(input())
print('size?')
sampling_data(input())
```



## 4. 데이터 시각화

```python
from config import config
from data import preprocess
from utils import utils

# config 저장
utils.save_config()

# 이미지 경로 및 캡션 불러오기
image_info = preprocess.get_path_caption()

# 전체 데이터셋을 분리해 저장하기
preprocess.dataset_split_save(image_info)

# 저장된 데이터셋 불러오기
print('train 또는 test 를 입력해주세요')
dataset_dict = preprocess.get_data_file(input())

# 데이터 샘플링
# if config.do_sampling:
dataset_sampling = preprocess.sampling_data(input())

# 이미지와 캡션 시각화 하기
utils.visualize_img_caption(dataset_sampling)
```

```python
def visualize_img_caption(dataset):
	img, com = '', ''
	for data in dataset:
		for s in range(len(data)):
			if data[s] == '|':
				img = data[:s]
				com = data[s+1:]
		addr = imread(f'./datasets/images/{img}')

		plt.imshow(addr)
		plt.title(f'<start>{com}<end>')
		plt.show()
```