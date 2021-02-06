## フィルター

https://docs.ansible.com/ansible/2.9_ja/user_guide/playbooks_filters.html

### 抽出
- selectattr('age', 'gt', 30)
- SQLlike
- 2.10だとlistいらない
- 該当なしだと空のリスト
- map 特定のattribute(カラム)も指定できる

### 結合
- combine マージ、新しいキーの追加
- ドキュメント見つつ

### 正規表現
- regex_search

### パス操作
- path_join /あるなしの意識する必要ない
- ansible utils parse cli

### 試行錯誤に便利
- ansible-console
debugger