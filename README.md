<!-- pip install djangorestframework -->
<!-- pip install requests -->
## 视图函数（根据id get数据）
<!-- cmd终端get -->
In [37]: import requests

In [38]: url = 'http://127.0.0.1:8000'

In [39]: r = requests.get(url + '/1')

In [40]: r.json()

Out[40]: [{'id': 1, 'name': 'ipad', 'weight': '20', 'size': '10', 'type': 1}]

## 视图类（根据分页 get数据）
<!-- cmd终端get -->
In [37]: import requests

In [38]: url = 'http://127.0.0.1:8000'

In [39]: r = requests.get(url + '/?page=1')

In [40]: r.json()

Out[40]:

[{'id': 1, 'name': 'ipad', 'weight': '20', 'size': '10', 'type': 1},
 {'id': 2, 'name': '华为', 'weight': '10', 'size': '5', 'type': 1}]

<!-- cmd终端post -->
In [37]: import requests

In [38]: url = 'http://127.0.0.1:8000'

In [39]: data = {
    ...:     'name': 'MyPhone', 'weight': '123G', 'size': '123*123', 'type': 1
    ...: }

In [40]: r = requests.post(url, data=data)