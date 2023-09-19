# Originality Ditection

## 概要

このリポジトリは [ES Harmony](https://es-harmony.vercel.app/) ( [git repository](https://github.com/lovelovetrb/ES_Harmony) ) 内の AI と人間の判定を行う AI モデルを利用するためのインターフェースを格納したリポジトリです。

主な機能としては ES Harmony 用に ES 文章をハイライトするための文章パースプログラムとなっています。

副次的な機能として、別に頒布しているモデルを読み込むことで、ES の質問文と回答一文から文章がどれだけ人間らしいかを判定することができます。

## 使い方

1. AI と人間の ES 文章をクラスタリングするタスクに特化したモデルを以下のリンクからダウンロードし、展開します。

   [ダウンロードリンク](https://www.dropbox.com/scl/fo/l2nl14cemund13xy0xzmb/h?rlkey=ba2kfqnnaymnk8je43z4tlxi9&dl=1)

2. Python の仮想環境を作成し、お使いの python パッケージマネージャーでこのパッケージをインストールします。

> #### pip
>
> ```
> pip install git+https://github.com/arara1930/originality_ditection.git
> ```

> #### rye
>
> ```
> rye add --git https://github.com/arara1930/originality_ditection.git originality_ditection
> ```

> #### poetry
>
> ```
> poetry add git+https://github.com/arara1930/originality_ditection.git
> ```

3. 以下、サンプルコードを参考に判定を行って見てください！

[サンプルコード](https://github.com/arara1930/originality_ditection/blob/main/detector_sample.py)

## 作成

- Mizuki Baba (Twitter -> [@lovelovetrb](https://twitter.com/lovelovetrb) )

- Kouhei Arasawa (Twitter -> [@kouhei0414dra](https://twitter.com/kohei0414dra) )

## License

The source code is licensed MIT. The website content is licensed CC BY 4.0,see LICENSE.
