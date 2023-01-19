# 준비
* serviceaccount와 token생성
```shell
name="developer"
namespace=default
token_name=$(kubectl -n $namespace get serviceaccount $name -o jsonpath='{.secrets[].name}')
token=$(kubectl -n $namespace get secret/$token_name -o jsonpath='{.data.token}' | base64 --decode)
```
* kubeconfig에 context, user추가
```yaml
apiVersion: v1
kind: Config
clusters:
  - name: rancher-desktop
    cluster:
      server: https://127.0.0.1:6443
      certificate-authority-data: ...
      insecure-skip-tls-verify: false
users:
  - name: developer
    user:
      token: $token
contexts:
  - name: developer
    context:
      cluster: rancher-desktop
      name: developer
      user: developer
```

# 실행방법
```shell
python main.py
```
