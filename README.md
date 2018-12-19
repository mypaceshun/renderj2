# pyrender

jinja2を使った簡単なテンプレートレンダー
パッケージングの練習に利用


# 使い方

``` console
# pyrender --vars vars.yml template.j2
```

上記のように実行すると、Jinja2の形式で書かれた`tempalte.j2`を
`vars.yml`の変数を用いてレンダリングします。

結果は標準出力に出力されます。

ファイル出力する機能はそのうち追加予定。


[Jinja2公式ドキュメント](http://jinja.pocoo.org/docs/2.10/templates/)

# 開発

## Require
  * python3 (venvを利用)
  * docker (rpmパッケージのビルドに利用)

## テスト

``` console
$ make test
```

`make lint`で`flake8`を走らせることもできる

## ビルド

``` console
$ make rpm
```

`docker`を立ち上げ`docker`内で`rpm-build`を実行。
生成されたrpmパッケージは`./product/RPMS`ディレクトリ内に置かれる。
