
## Ansible 3.0.0
2021/2/16あたりリリース
https://docs.ansible.com/ansible/devel/roadmap/COLLECTIONS_3_0.html
https://tekunabe.hatenablog.jp/entry/2020/12/14/ansible300

## ポイント
- セマンティックバージョニングになる
- Ansible 2.10 の次は 2.11 ではなく 3.0.0
- Ansible 2.10 で ansible の基本機能と基本モジュールは ansible-base という名前だったが、ansible-core という呼び方に変わる
- 2.10系をベース 3入れても現状2.10になる。Ansible 3 is based on Ansible-Base 2.10
- porting guide https://docs.ansible.com/ansible/devel/porting_guides/porting_guide_3.html
- 入ってくるcollectionが違う

- Playbook実行は基本的なやつは特に問題ない (要検証)