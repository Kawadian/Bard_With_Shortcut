# Bard_With_Shortcut
GoogleのBardをiPhoneの「ショートカット」アプリ経由で実行することができる簡単なPythonスクリプトです。<br>
使用するためにはBardのtokenが必要になります。無料です。<br>
まずBardの公式ページ（ https://bard.google.com ） に行きます。
<br>
次にデベロッパーツールを開きます。
Elements、Console、・・・と続いてると思うので、その中のApplicationを押し、<br>
Cookies、https://bard.google.com の順に行きます。<br>
「__Secure-1PSID」という名前があると思うので、そこのValueをコピーします。<br>
これでtokenの取得は完了です。<br>
これをiPhone側のショートカットにて先ほどのtokenをペーストします。<br>
あとはpythonファイルを実行して、ショートカット内のURLを実行しているサーバーアドレスに書き換えれば完了です。
