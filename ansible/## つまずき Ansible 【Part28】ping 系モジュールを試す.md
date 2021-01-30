## pingモジュール
Ansible --- SSH ---> [Linux]

## win_pingモジュール
Ansible -- WinRM --> [Windows]
windows相手にpingモジュール使うとpythonエラー

## ios_pingモジュール(NW向け)
Ansible --- [ios] --- ICMP ---> [dest先]
Ansible -> iosではない
ios -> dest
iosのpingコマンドを生成して実行
destが必須
net_pingモジュールも大体一緒(ベンダーまとめて抽象化)

## icmp(手元でpingコマンド)
現状commandモジュールでやるしかない(はず) なんかあれば教えてくださいとのこと
デフォルトだと回数無限だから処理が戻らない -c local