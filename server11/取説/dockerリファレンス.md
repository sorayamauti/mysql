# Dockerの使い方

---
## インストール
- CentOS7系の場合
 $ sudo dnf install -y device-mapper-persistent-data lvm2
 $ sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
 $ sudo dnf install -y --nobest docker-ce docker-ce-cli
 $ sudo usermod -aG docker $USER
 $ sudo systemctl enable docker
 $ sudo systemctl start docker

- ついでにpython3も
 $ sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
 $ sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
 $ sudo ln -s /bin/python3.6 /bin/python3
 $ sudo ln -s /bin/pip3.6 /bin/pip

---
## 基本操作  
- Dockerイメージの入手  
 $ docker pull イメージ名
 $ docker pull イメージ名:タグ
 DockerイメージはDocker hubからダウンロードされる
 タグをつけるとバージョンを指定できる

- ローカルサーバ上に保管しているイメージの一覧  
 $ docker images

- Dockerコンテナの生成と起動  
 $ docker run --name コンテナ名 -h ホスト名 -i -t イメージ名 /bin/bash
 -i コンテナ起動時に標準入力を受け付ける
 -t 仮想端末をコンテナに割り当てる
 -h ホスト名

- コンテナ一覧の確認
 $ docker ps
 $ docker ps -a
 -a 停止中のコンテナも含めてすべて表示

- Dockerコンテナをバックグラウンドで実行
 $ docker run -d --name ～省略～

- バックグラウンドで稼働するコンテナへの接続
 $ docker attach コンテナ名
 exitで抜けるとコンテナが停止する

- バックグラウンドで稼働するコンテナへの接続
 $ docker exec -it コンテナ名 /bin/bash
 exitで抜けてもコンテナは停止しない（/bin/bashが止まるだけ）ip a

- コンテナのコミット（イメージをローカルに保存）
 $ docker commit コンテナID イメージ名：タグ
   ※DockerHubを利用する場合 ユーザ名/イメージ名：タグ

- Docker Hubへのログイン
 $ docker login -u=ユーザ名 -p=パスワード
 ※オプションを指定しなくてもよい

- Docker Hubへコンテナイメージをpush
 $ docker push ユーザ名/イメージ名：タグ

- Docker Hubへのログアウト
 $ docker logout

- コンテナの削除
 $ docker rm コンテナID
 $ docker rm -f コンテナ名
 -f 稼働中のコンテナの強制削除

- ホストＯＳからのコンテナ停止  
 $ docker stop コンテナ名

- 停止しているコンテナの起動  
 $ docker start コンテナ名

- コンテナ情報の取得  
 $ docker inspect コンテナ名

- Dockerイメージの削除
 $ docker rmi イメージ名
 $ docker rmi -f イメージ名
 -f イメージを利用中のコンテナが存在しても削除

- コンテナ停止時に自動的にコンテナを廃棄させるように起動
 $ docker run --rm --name ～省略～

- ホストOSのディレクトリをコンテナに見せる
 $ mkdir -p /share/hostdir
 $ docker run -v /hostdir:/コンテナのディレクトリ --name ～省略～

- ホストOSのディレクトリを書き込み不可でコンテナに見せる
 $ mkdir -p /share/hostdir
 $ docker run -v /hostdir:/コンテナのディレクトリ:ro --name ～省略～

- コンテナ間のボリューム共有
 $ docker run -v /コンテナAのディレクトリ --name コンテナA  ～省略～
 $ docker run --name コンテナB --volumes-from コンテナA　～省略～

- データ専用コンテナの作成
 $ docker pull busybox:latest
 $ docker run -v /data001 --name data_container -it busybox /bin/sh
 $ docker run --name コンテナ名 --volumes-from data_containar ～省略～

- ポートフォワーディングの指定  
 $ docker run -p ホストのポート番号：コンテナのポート番号   ～省略～

- 他のコンテナのネットワーク情報を取得（コンテナ間通信のため）
 $ docker run --link 接続するコンテナ名：エイリアス ～省略～


---
## Dockerイメージの自動ビルド　Dockerfile

- Dockerfileの最初に書く内容
 $ vi Dockerfile
  FROM イメージ名：タグ名
  MAINTAINER イメージ作成者の情報（名前、メールアドレス、所属など）

- Dockerfileを使ったイメージのビルド
 $ docker build -t イメージ名：タグ /Dockerfileを保存しているディレクトリ
 $ docker images

- Dockerfileの中でインストールや設定をする
  FROM イメージ名：タグ名
  RUN yum install -y httpd\         # Shell形式
                     php\
                     php-mbstring
  RUN ["adduser","inoue"]           # Exec形式

- 処理を実行する際のカレントディレクトリを指定する
  WORKDIR ディレクトリ

- 環境変数を定義する
  ENV http_proxy=http://xxx.xx.xx.xx:8080 \
      AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxx \
      mydir=/home/tmp
  WORKDIR $mydir

- ホストLinuxのファイルをコンテナにコピーする
  COPY ホストLinuxのPATH コンテナのPATH
  ADD ホストLinuxのPATH コンテナのPATH
  ※COPYは単純なコピー、ADDはコピー元にURLを指定できたりアーカイブの展開ができる

- コンテナの公開するポートを指定する
  EXPOSE ポート番号

- 実行ユーザの指定
  USER ユーザ名

- ボリュームの作成
  VOLUME　パス

- コンテナ起動時に自動実行するコマンドの指定
  CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
  ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]
  ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]

  ※CMDもENTRYPOINTもどちらも自動起動するが、通常はENTRYPOINTを使う
  ※Shell形式、Exec形式の両方が利用できるが、通常はExec形式を使用する


---
## 複数コンテナの一括管理　docker-compose
※バージョンによって設定が異なります

- CentOS7におけるdocker-composeのインストール
 $ sudo pip install docker-compose

- docker-compose.ymlの作成
 $ mkdir プロジェクト名
 $ vi docker-compose.yml

- docker-compose.ymlの書き方
　※公式doc https://docs.docker.com/compose/compose-file/#reference-and-guidelines

  version: '3'                # versionの指定・version3はDocker1.13以降のみ対応
  services:                   # サービス（コンテナ）の構成
    webserver:                # コンテナ名
      image: centos:latest    # Dockerイメージの指定
      tty: true               # docker runの-tオプション
      stdin_open: true        # docker runの-iオプション
      ports:                  # docker runの-pオプション
        - 80:8080
        - 22:22
      volumes:                # docker runの-vオプション
        - /data:/data     
      volumes_from:           # docker runの--volumes_fromオプション
        - data_container
      environment:            # 環境変数の定義
        SECRET: "abcdef"

    linebot:
      build: ./linebot        # Dockerfileによるイメージのビルド・Dockerfileのパスを指定
      env_file:               # コンテナ実行時に作成する環境変数のコンフィグ
        - ./web.env
      command: ["echo", "hi"] # コンテナ起動時に実行するコマンド
      entrypoint:             # コンテナ起動時に実行するサービス
        - /usr/sbin/httpd
        - -D
        - FOREGROUND

- コンテナの一括生成・起動
 $ cd YAMLがあるディレクトリ
 $ docker-compose up      # フォアグラウンド
 $ docker-compose up -d   # バックグラウンド

- コンテナの個別起動
 $ cd YAMLがあるディレクトリ
 $ docker-compose run コンテナ名

- コンテナの一括停止
 $ docker-compose stop

- コンテナの一括起動
 $ docker-compose start
 
- コンテナの一括削除
 $ docker-compose rm
 $ docker-compose rm -f
 $ docker-compose rm -fs 
 -f y/n無し
 -s コンテナ停止