# hello idon

---
1. startproject
   1. pip install django~=3.2
   2. django-admin startproject _helloidol ._
   3. python manage.py runserver
2. startapp _playground_
   1. Terminal
      1. python manage.py startapp **playground**
   2. _helloidon_/settings.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보 전달: urls -> views -> (models -> ) -> templates
   - 코드 작성: (models -> ) views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
   2. urls
      1. _/playgound/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/hello.html
4. helloidol/
   1. urls, _playgournd/urls_
      1. _playground/_ => _hello/_ -> _say_hello()_
      1. _playground/_ => _hello_html/_ -> _say_hello()_html()_