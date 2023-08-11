# 编写你的第一个 Django 应用，第 1 部分¶
<<<<<<< HEAD
__安裝模組__
(ˋ)$pip install django (ˊ)
**查看版本**
```python
$python -m django --version
```
** 移到指定路徑位置**
! cd /content/drive/MyDrive/"Colab Notebooks"/Web #這段無法執行，似乎預設路徑就是暫存路徑
##用于开发的简易服务器¶
**開發專案**
```python
$ django-admin startproject mysite
```
**移至專案位置**
```python
 - cd mysite
- $ python manage.py runserver
 ```
- **若想更换服务器的监听端口，可用以下**
```python
- $ python manage.py runserver 8080
 ```

# 编写你的第一个 Django 应用，第 2 部分

**尝试一下 Django 为你创建的各种 API**
```python
$ python manage.py shell
 ```

默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。请执行以下命令：
=======
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
>>>>>>> 3c086f21d26fbde5919e256974eec7bdea924b38
