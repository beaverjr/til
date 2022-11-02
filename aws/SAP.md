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