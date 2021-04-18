## 20210409
Laravel

composer: 
Composer は、PHP のプロジェクトが必要とするライブラリやパッケージを管理する「ライブラリ依存管理ツール」です。 その PHP プロジェクトで必要なパッケージ(ライブラリ)は何かを列挙すると、それらを自動的にインストールしてくれる機能を持ちます。

Laradockとは
公式ウェブサイトには、Laravel(PHP)のプロジェクトをDocker上で動作させるためのワンダフルな環境とあります。 A full PHP development environment for Docker.


Laravelのディレクトリ構成
https://codezine.jp/article/detail/11231?p=3


Laravelのルーティング登録では、URLに変数を埋め込むことができます。これを「ルートパラメータ」といい、ルーティングパターンに以下の記述をします。

"/…/{パラメータ名}"

googleにリダイレクト
Route::redirect("/google", "https://www.google.com/");


HTMLコードを記述したファイルを別に用意しておきます。このファイルのことを「テンプレート」と呼びます。一方で、PHP側でそのテンプレートに埋め込むデータを用意しておきます。テンプレートエンジンはそれらを統合してHTMLレスポンスを生成する仕組みです。