##Django初体験:)
**djangoproject.jp**のチュートリアルでお勉強

http://www.djangoproject.jp


**Djangoのデプロイ**

http://docs.djangoproject.jp/en/latest/howto/deployment/index.html

http://tatabox.hatenablog.com/entry/2013/02/10/213359

admin画面のがまともに表示されないのは，/static/admin/（エイリアス）のパスが通ってなくて，
cssのロードに失敗しているため．httpd.confでエイリアスを設定する．
http://cloverrose.hateblo.jp/entry/2012/05/08/004635
