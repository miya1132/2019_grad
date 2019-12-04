## データベース作成
```
$ docker-compose exec db bash
# mysql -u root -p
mysql> create database 2019_grad_db;
``` 

コンテナに移動
$ docker-compose exec app bash


## git コマンド

### 初期設定(※developのクローン作成)
```
git clone -b develop https://github.com/miya1132/iju-app.git
```

### リモートブランチをチェックアウト
```
git branch -r
git fetch --prune
git checkout -b feature/IJU-APP-001 origin/feature/IJU-APP-001
```

### 作業開始
```
git checkout develop
git pull origin develop
git checkout -b feature/IJU-APP-001
```

### 作業中
```
git add .
git commit -a -m "IJU-APP-001対応　※簡易的に対応内容を記入"
```

### 作業完了
```
git push -u origin feature/IJU-APP-001
```

### developマージン
```
git checkout develop
git pull origin develop
git checkout feature/IJU-APP-001
git merge develop
```

### リモートブランチのpull
```
git branch -r
git fetch --prune
git checkout -b feature/IJU-APP-001 origin/feature/IJU-APP-001
```

## docker-compose コマンド
