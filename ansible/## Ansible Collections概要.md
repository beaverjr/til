## Ansible Collections概要
- 2.9
    - Issues, プルリク, CIの管理が煩雑
    - モジュールのbugfixをAnsibleのリリースサイクルに合わせる必要がある
- 2.10
    - モジュール類をCollectionという単位で外へ
    - リリースの加速

 ### Collectionsの特徴
 - Collectionごとにリポジトリで管理
 - モジュールだけでなく、Roleやフィルターなどをパッケージング可能
 - Ansible galaxyから配布が可能

## ベンダー体験談
- モジュールの増加はAnsibleをpowerfulに
- Galaxy user guide
- Galaxy developer guide
- 継続したメンテナンス体制

## 気軽にpip install ansibleを実行して、Ansible Towerでエラーが起きた話
- ansible lintをインストールすると同時にansible coreも入る
- virtualenvを利用

## 本当にあった怖い話 Ansible SaaS運用編
- include_varsでの読み込み
- 共有OS環境が自動化に向いていない
- 変数の定義箇所が多すぎる

## やらかしlineinfile 〜冪等性が失われた日、そしてreplaceへ〜
- ファイルを丸ごと置き換えられないケースで利用
- 不揃いの環境の特定のパラメータ変更
- 変換対象が複数あるならreplaceモジュール

## タグの継承を知らずにやらかした話
- タグの継承
- --list-tags --list-tasks

## whenはifとは微妙に違う
- blockに対するwhenは途中のタスク中全てに個別反応
- 思い込み厳禁