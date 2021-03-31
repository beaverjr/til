# JAWS-UG朝会 #19
## VPC Reachability Analyzer使って人生が変わった話
### とりあえず設定みる派
- ルートテーブル
- セキュリティグループ
- ネットワークACL
- iptables

### コマンド試す派
- ping、traceroute、tcpdump...

- LambdaとかGlueの調査は辛かった

### VPC Reachability Analyzer
- Sorce~Destが表示される
- 接続できない場合は間違ってそうな箇所を表示してくれる

## SSMセッションマネージャーを使って人生を変えたい話
- RSH → SSH
- 最近はSSHポート変えても攻撃リスクあるのでIP制限必須
- SSMを使うことで攻撃者の入り口をなくす

## 運営をやって人生が変わった話