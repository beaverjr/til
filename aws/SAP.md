## IAM 外部ID
https://dev.classmethod.jp/articles/iam-role-externalid/

## Amplify
- AWS Amplify は Web フロントエンド、モバイルアプリの開発を加速させるために作られたプラットフォーム
- AWS を⽤いたサーバーレスなバックエンドの構築するための CLI や、バックエンドと接続するためのクライアントライブラリ、Web サイトのホスティングの仕組みを持つ

### Amplify CLI を使ったバックエンドの構築
#### API カテゴリ (GraphQL / REST API)
- API カテゴリには GraphQL と REST の２種類のタイプが存在
- GraphQLを選択した場合、AWS AppSync と統合された API を構築
- REST を選択した場合、Amazon API Gateway、AWS Lambda と統合された APIを構築

#### Authentication カテゴリ
- Amazon Cognito と統合されたカテゴリ

#### Prediction カテゴリ
- Amazon が提供する 各AI/ML サービスと統合されたカテゴリ

E2E テスト (Cypress)

## SSM
### マネージドインスタンスにするために
- エージェントの導入
- SSM APIへのアウトバウンド経路の確保
- IAMロール付与

### リソース把握
- ダッシュボード
    - SSM Explorer
    - SSM OpsCenter
    - コンプライアンス
- SSMインベントリ
https://d1.awsstatic.com/webinars/jp/pdf/services/20200212_AWSBlackBelt_SystemsManager_0214.pdf
マルチアカウント/マルチリージョンのダッシュボード
Athena, QuickSightを用いて
マルチアカウント/マルチリージョン横断分析も


## クロスアカウントアクセス
- STS
- AD
- フェデレーティッドユーザー
    - フェデレーティッドユーザーは、AWS アカウントを持たないユーザー (またはアプリケーション) です。
    - フェデレーティッドユーザーのロール
        ロールを使用することで、フェデレーティッドユーザーに一定の期間にわたり AWS リソースへのアクセス権を付与できます。
        これは、Microsoft Active Directory、LDAP、Kerberos などの外部サービスで認証できる AWS 以外のユーザーが存在する場合に役立ちます。

## Amazon Kinesis
## DynamoDB
グローバルテーブル
DynamoDB ストリーム

AWS アカウントを信頼された署名者とする CloudFront behavior を作成

##　CFn
mappings conditions

Redshiftはリアルタイムではない
AWS Data Pipeline

Cognito
- ユーザーブール
- IDプール

AWS OpsWorks
Amazon Timestream


計画
検出

評価とプロファイリング
データの要件と分類
優先順位付け
ビジネスロジックとインフラストラクチャの依存関係


設計

詳細な移行計画
作業量の見積もり
セキュリティとリスクの評価

構築
変換

ネットワークトポロジー
移行
デプロイ
検証
移行

パイロットテスト
サポートへの移行
リリース管理
カットオーバーと廃止

実行
運用

スタッフのトレーニング
モニタリング
インシデント管理
プロビジョニング
最適化

モニタリング駆動型の最適化
継続的インテグレーションと継続的デプロイ
Well-Architected フレームワーク


### コスト管理のベストプラクティス
- 特定のグループまたはチームのみに、選択した AWS リソースのデプロイを許可する
- 環境ごとにポリシーを作成する
- リソースのインスタンス化時にタグを必須にする
- タグ付けをモニタリングし、不適切なタグのインスタンスについてアラート送信またはシャットダウンを実行する
- CloudWatch を使用して、請求がしきい値に達したときにアラートを送信する
- AWS またはパートナーのツールを使用して支出を分析する


Redis：高可用性
Memcached：可用性は高くない

ElasticBeanstalk
削除保護はAutoScalingでは機能しない

ElastiCache
キャッシュ戦略



Lambda関数は15分後にタイムアウト
AWS Batchは負荷の高いコンピューティングを効率的に行うためのサービス
必要なリソースを自動的にプロビジョンし、ジョブが終了するとリソースを終了