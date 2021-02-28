# つまずき Ansible 【Part32】凡ミスTOP5

## listを指定しているはずがdictと言われる
- syntaxcheck okでもエラーになってしまう
- pythonのメソッドとして呼ばれる
- 地雷変数
- 止むを得ず指定しなければならない時は囲む
https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#referencing-key-value-dictionary-variables

## モジュール間違い 
- モジュール名から疑う(例:interfaceの場合もinterfacesの場合もある)

## パラメータ
- パラメータ名違い
- パラメータがとりうる値が選択肢にない

## フィルター
- 閉じかっこ

## インデント
- syntax-checkはエディタが便利

## 全般
- エラーメッセージ最初と最後両方を見てみる