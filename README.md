Intern-app-django

Prosta plikacja servera do logowania. Korzysta z
Django i Django REST framework.

Udostępnia cztery endpointy:

	I: /login/: email + haslo; zwraca: token
	II: /register/: Email, username, haslo; zwraca: token
	III: /users/me/: Pobranie aktualnie zalogowanego użytkownika
	    wymaga autoryzacji przy pomocy otrzymanego tokena
	IV: /users/: Pobieranie wszystkich użytkowników
	    wymaga autoryzacji przy pomocy otrzymanego tokena



Wymagania:

- Python 3.5.2
- pip

Instalacja(Linux):

	I: git clone https://github.com/marcinSuw/intern-app-django.git
	II: cd intern-app-django
	III: pip install -r requirements.txt
	IV: python manage.py runserver   


Testy:

- python manage.py test

Testowane endpointy:
 - /login/: test metoda [POST] poprawne dane oraz niepoprawne
 - /register/: test metoda [POST] poprawne dane oraz niepoprawne
 - /users/me/: test metoda [GET] pobranie danych o zalogowanym użytkowniku z autoryzacją oraz bez
 - /users/: test metoda [GET] pobranie listy uzytkowników z autoryzacją oraz bez

Przykładowy test:

    #sample test
    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

Zbudowane z:
    - Django
    - Django REST framework

Autor
Marcin Suwała
