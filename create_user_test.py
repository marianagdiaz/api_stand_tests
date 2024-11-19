import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    print(user_response.status_code)
    print(user_response.json())
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

def negative_assert_symbol(first_name):
    user_body_negative = get_user_body(first_name)
    response_negative = sender_stand_request.post_new_user(user_body_negative)
    print(response_negative.status_code)
    print(response_negative.json())
    assert response_negative.status_code == 400
    assert response_negative.json()["code"] == 400
    assert response_negative.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."

def negative_assert_no_first_name(user_body):
    response_negative_no_first_name = sender_stand_request.post_new_user(user_body)
    print(response_negative_no_first_name.status_code)
    print(response_negative_no_first_name.json())
    assert response_negative_no_first_name.status_code == 400
    assert response_negative_no_first_name.json()["code"] == 400
    assert response_negative_no_first_name.json()["message"] == "No se han aprobado todos los parámetros requeridos"

def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

test_create_user_2_letter_in_first_name_get_success_response()

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert('Aaaaaaaaaaaaaaa')

test_create_user_15_letter_in_first_name_get_success_response()

def test_create_user_1_letter_in_first_name():
    negative_assert_symbol('A')

test_create_user_1_letter_in_first_name()

def test_create_user_16_letter_in_first_name():
    negative_assert_symbol('Аааааааааааааааа')

test_create_user_16_letter_in_first_name()


def test_create_user_has_special_symbol_in_first_name_():
    negative_assert_symbol("\"№%@\",")

test_create_user_has_special_symbol_in_first_name_()

def test_create_user_has_numbers_in_first_name():
    negative_assert_symbol('123')

test_create_user_has_numbers_in_first_name()


def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_first_name(user_body)

test_create_user_no_first_name_get_error_response()

def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body('')
    negative_assert_no_first_name(user_body)

test_create_user_empty_first_name_get_error_response()

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    print(response.status_code)

test_create_user_number_type_first_name_get_error_response()



