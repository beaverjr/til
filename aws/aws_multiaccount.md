## 20210408
AWS Well-Architected フレームワークより

- すべてのユーザーやシステムが認証情報を共有しない
- ユーザーアクセス権は、パスワード要件やMFAの強制などのベストプラクティスを実践した上で、最小権限で与えられるべき
- AWSのサービスに対するAPIコールなど、プログラムによるアクセスを、AWS Security Token Serviceなどが発行する、権限が制限された一時的な認証情報を使用して実行