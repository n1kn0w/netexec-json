# Exemples

## --users (parsing structuré par utilisateur)

```sh
nxc smb 10.4.10.10 -u jaime.lannister -p cersei --users --json | jq -c 'select(.data.username) | .data'
```

## --shares (parsing structuré par share)

```sh
nxc smb 10.4.10.10 -u jaime.lannister -p cersei --shares --json | jq -c 'select(.data.share) | .data'
```

## --pass-pol (snapshot complet de la password policy)

```sh
nxc smb 10.4.10.10 -u jaime.lannister -p cersei --pass-pol --json | jq 'select(.data.domain) | .data'
```
