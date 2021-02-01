## 20210131
モジュール一覧をざっと見

- assertモジュール
thatパラメータが必須
https://docs.ansible.com/ansible/2.9_ja/modules/assert_module.html#assert-module

```
- name: Check return value
      assert:
        that: "'usage:' in result.stderr"
```

## 20210201
- コマンドの実行結果に期待する文字列が含まれるか (taskの実行結果をregisterで変数に保存し、出力結果に特定の文字列が含まれるかを確認)
- thatパラメータに定義した条件に合致するか判定し、合致しない場合にタスクを失敗させる
- whenとの違い