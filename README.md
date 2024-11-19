# 🚀 API User Tests

Este proyecto es un conjunto de pruebas automatizadas diseñado para validar el comportamiento de una API de creación de usuarios. Aquí evaluamos tanto los escenarios exitosos como los casos límite, asegurándonos de que la API maneje correctamente datos válidos e inválidos.

El objetivo es garantizar la integridad del sistema al recibir diferentes entradas para el campo `firstName`, cumpliendo con las reglas establecidas por el servidor.

---

## 📌 Tecnologías Utilizadas

- **Python 3.x**: Lenguaje principal para desarrollar las pruebas.
- **Requests**: Biblioteca para realizar solicitudes HTTP.
- **Pytest**: Framework para ejecutar y gestionar las pruebas automatizadas.
- **Pycharm**: Entorno de desarrollo integrado (IDE) utilizado para escribir y depurar el código.

---

## 📂 Estructura del Proyecto

El proyecto consta de los siguientes módulos:

1. **`sender_stand_request`**: Define funciones clave para interactuar con la API, como:
   - `post_new_user(user_body)`: Envía una solicitud POST para crear un nuevo usuario.
   - `get_users_table()`: Obtiene la tabla actual de usuarios registrados.
   
2. **`data`**: Contiene una plantilla básica para el cuerpo de la solicitud (`user_body`) con los campos necesarios para la creación de un usuario.

3. **Funciones de prueba**: Se agrupan en dos categorías principales:
   - **Pruebas positivas**: Validan entradas válidas aceptadas por la API.
   - **Pruebas negativas**: Verifican que la API rechace entradas inválidas con mensajes de error apropiados.

---

## ⚙️ Configuración de la API

El servidor de la API requiere que los datos enviados cumplan las siguientes reglas para el campo `firstName`:
- Debe contener solo letras del alfabeto latino.
- La longitud debe estar entre **2 y 15 caracteres**.

---

## 🔍 Detalles de las Pruebas

### Función `get_user_body(first_name)`
Esta función toma un valor para el nombre (`firstName`) y crea un diccionario basado en la plantilla de usuario (`data.user_body`). Este diccionario se utiliza en todas las pruebas.

**Ejemplo de uso:**

user_body = get_user_body("John")

✅ Pruebas Positivas
Estas pruebas validan que la API funcione correctamente al recibir datos válidos.

Nombres válidos de longitud mínima y máxima:

## 2 caracteres:

def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

## 15 caracteres:

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

## Resultados esperados:

Código de respuesta: 201
Respuesta contiene un token de autenticación (authToken).
El usuario se registra correctamente en la tabla.

## ❌ Pruebas Negativas
Estas pruebas aseguran que la API maneje adecuadamente entradas inválidas.

Casos Evaluados:

## Nombres demasiado cortos (1 carácter):

def test_create_user_1_letter_in_first_name():
    negative_assert_symbol("A")

## Nombres demasiado largos (16 caracteres):

def test_create_user_16_letter_in_first_name():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

## Nombres con caracteres especiales:

def test_create_user_has_special_symbol_in_first_name():
    negative_assert_symbol("\"№%@\",")

## Nombres numéricos:

def test_create_user_has_numbers_in_first_name():
    negative_assert_symbol("123")

## Campo firstName ausente:

def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_first_name(user_body)

## Campo firstName vacío:

def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_first_name(user_body)

## Tipo de dato incorrecto (int en lugar de str):

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400

## Resultados esperados:

Código de respuesta: 400
Mensaje de error específico:

## Nombre inválido:

{
  "code": 400,
  "message": "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."
}
## Campo ausente:

{
  "code": 400,
  "message": "No se han aprobado todos los parámetros requeridos"
}
