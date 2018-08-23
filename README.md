Intern-app-django

Prosta plikacja servera do logowania. Korzysta z
Django i Django REST framework.

Udostępnia cztery endpointy:

	I: Logowanie
		metoda: POST
	 	endpoint: `/login/`
		przykładowy json:
		{
			"email": "test@gmail.com",
			"password": "12345678",
		}
	  	zwraca:
		{
			token: TOKEN
		}
	II: Rejestracja
		metoda: POST
		endpoint: `/register/`
		przykładowy json:
		{
			"email": "test@gmail.com",
			"username": "test",
			"password": "12345678",
			"password2": "12345678"
		}
		zwraca:
		{
			token: TOKEN
		}

	III: Pobranie aktualnie zalogowanego użytkownika
		metoda: GET + Autoryzacja ( JWT TOKEN )
		endpoint: `/users/me/`
		zwraca:
		{
    		"username": "test",
    		"email": "test@gmail.com"
		}
	IV: Pobieranie wszystkich użytkowników
		metoda: GET + Autoryzacja ( JWT TOKEN )
		endpoint: `/users/`
		zwraca:
		[
    		{
    		    "email": "test1@gmail.com",
    		    "username": "test1"
    		},
    		{
    		    "email": "test2@gmail.com",
    		    "username": "test2"
    		}
		]

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
