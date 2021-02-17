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
Molecule will skip tasks which are tagged with either molecule-notest or notest. With the tag molecule-idempotence-notest tasks are only skipped during the idempotence action step.
