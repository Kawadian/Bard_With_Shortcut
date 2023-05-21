# Bard_With_Shortcut

このコードはiPhoneの「ショートカット」アプリを使用することを前提としています。他の方法は試したことがないので悪しからず。<br>
ショートカットのリンクは↓<br>
https://www.icloud.com/shortcuts/1660d6f7736e4c4eadb159746030328f
<br>
GoogleのBardをiPhoneの「ショートカット」アプリ経由で実行することができる簡単なPythonスクリプトです。<br>
bardapiモジュールが必要です。以下のコマンドでインストールしてください。<br>
```
pip install bardapi
```

また、使用するためにはBardのtokenが必要になります。無料です。<br>
まずBardの公式ページ（ https://bard.google.com ） に行きます。
<br>
次にデベロッパーツールを開きます。
Elements、Console、・・・と続いてると思うので、その中のApplicationを押し、<br>
Cookies、https://bard.google.com の順に行きます。<br>
「__Secure-1PSID」という名前があると思うので、そこのValueをコピーします。<br>
これでtokenの取得は完了です。<br>
これをiPhone側のショートカットにて先ほどのtokenをペーストします。<br>
あとはpythonファイルを実行して、ショートカット内のURLを実行しているサーバーアドレスに書き換えれば完了です。


やりたいこと<br>
・Bardは同時に回答が3つ生成されるので、それぞれの回答を全部出すのもアリかなとは思う。<br>
Bardからの出力を見れば分かると思いますが、単純なので実装はそこまで難しくないと思います。<br>
・セキュリティ的にガバガバすぎる<br>
これ単体では到底外部に公開できないので、あくまで試してみる用です。気が向いたらちゃんとしたものを作ろうかなと思います。<br>
