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
### 起動
```
# foregroundで起動
docker-compose up
docker-compose up --build

# backgroundで起動
docker-compose up -d
docker-compose up -d --build
```

### 停止
```
# foregroundで起動していた場合
Ctr + C

# backgroundで起動していた場合
docker-compose stop

# 停止＆削除（コンテナ・ネットワーク）
docker-compose down

# 停止＆削除（コンテナ・ネットワーク・イメージ）
docker-compose down --rmi all

# 停止＆削除（コンテナ・ネットワーク・ボリューム）
docker-compose down -v
```

### コンテナ・イメージの全削除
```
docker-compose down --rmi all
```

### キャッシュなしビルド
```
docker-compose build --no-cache
```

### コンテナに入る
```
docker exec -it grad_db bash  
```


### MySQLパスワード変更
```
# docker exec -it grad_db bash
> mysql -u root -p
> パスワードをVdwKsbe7rgM3で入る

mysql> use mysql
mysql> update mysql.user set password=password('2019_grad') where user = 'root';
mysql> flush privileges;
```
