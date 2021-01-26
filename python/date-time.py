#20210126 
#モジュールは Python の定義や文が入ったファイルです。ファイル名はモジュール名に接尾語 .py がついたものになります。
import datetime

now = datetime.datetime.today()
#now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d"))
