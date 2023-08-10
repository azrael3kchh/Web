# 安裝模組
$pip install django 
# 查看版本
$python -m django --version
# 移到指定路徑位置
! cd /content/drive/MyDrive/"Colab Notebooks"/Web #這段無法執行，似乎預設路徑就是暫存路徑
# 開發專案
$ django-admin startproject mysite
# 移至專案位置
$ cd mysite
$ python manage.py runserver
# 若想更换服务器的监听端口，可用以下
$ python manage.py runserver 8080

