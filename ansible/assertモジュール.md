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