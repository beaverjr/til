IAMロール
(タグ"DIV"に"APP"を含むもの)
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeSessions",
                "ssm:GetConnectionStatus",
                "ssm:DescribeInstanceProperties",
                "ec2:describeInstances"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:instance/*"
            ],
            "Condition": {
                "StringLike": {
                    "ssm:resourceTag/DIV": [
                        "APP"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession"
            ],
            "Resource": [
                "arn:aws:ssm:*:*:session/${aws:username}-*"
            ]
        }
    ]
}
```


■CLI
タグがついているインスタンス
```
% aws ssm start-session \
--target タグがついているインスタンスIDを指定

Starting session with SessionId: セッションID
sh-4.2$
```

タグが付いていないインスタンス
```
% aws ssm start-session \
--target タグがついていないインスタンスIDを指定

An error occurred (AccessDeniedException) when calling the StartSession operation: User: ユーザ is not authorized to perform: ssm:StartSession on resource: インスタンスID
```

■コンソール
タグがついていないインスタンスに接続を試みると同様のエラー
User: ユーザ is not authorized to perform: ssm:StartSession on resource: インスタンスID

### Windowsでも同様