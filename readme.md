# 编写你的第一个 Django 应用，第 1 部分¶
## 安裝模組
```python
$pip install django
```
## 查看版本
```python
$python -m django --version
```
## 創建項目 開發專案
```python
$ django-admin startproject mysite
```
## 用于开发的简易服务器¶
移到指定路徑位置
```python
$ cd azrael3kchh/Web/mysite/mysite
$ python manage.py runserver
# 若想更换服务器的监听端口，可用以下
$ python manage.py runserver 8080
```
## 创建投票应用
```python
$ python manage.py startapp polls
```
# 编写你的第一个 Django 应用，第 2 部分¶

```python
$ python manage.py migrate
```
