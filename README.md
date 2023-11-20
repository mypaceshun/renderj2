# pyrender

jinja2を使った簡単なテンプレートレンダー
パッケージングの練習に利用

``` console
$ renderj2 --help
Usage: renderj2 [OPTIONS] TEMPLATE_FILE

  Rendre Jinja2 tempalte

Options:
  -v, --varsfile PATH  vars file path for jinja2
  -o, --output PATH    output file
  --loglevel LVL       Either CRITICAL, ERROR, WARNING, INFO or DEBUG
                       [default: INFO]
  -h, --help           Show this message and exit.
  -V, --version        Show the version and exit.
```

# 使い方

``` console
# renderj2 --vars vars.yml template.j2
```

上記のように実行すると、Jinja2の形式で書かれた`tempalte.j2`を
`vars.yml`の変数を用いてレンダリングします。

レンダリング結果はデフォルトで標準出力に出力されます。
`--output` オプションを指定することで指定のファイルに出力することも可能です。

[Jinja2公式ドキュメント](http://jinja.pocoo.org/docs/2.10/templates/)

# 開発

## Require

  * python3
  * Poetry

## テスト

``` console
$ poetry poe test
```

## ビルド

``` console
$ poetry build
```
