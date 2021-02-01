## 20210129
### vagrant driverの時の書き方

```
dependency:
  name: galaxy
lint: |
  set -e
  yamllint .
  ansible-lint
driver:
  name: vagrant
  provider:
    name: libvirt
platforms:
  - name: centos7
    box: generic/centos7
provisioner:
  name: ansible
verifier:
  name: ansible
```

## 20210201

```
tags:
    - molecule-idempotence-notest
```