# Proyecto de Autenticación con FastAPI y OAuth2

Este proyecto es un ejemplo completo de autenticación usando **FastAPI** y **OAuth2**. Implementa varios endpoints, incluyendo uno para la generación de tokens de acceso y otro para obtener información de perfil del usuario autenticado. También contiene funciones de ayuda para manejar y verificar contraseñas y tokens.

## Descripción

Este proyecto simula un sistema de autenticación básico usando **JWT (JSON Web Tokens)**. Incluye:
- Generación de tokens de acceso (`/token`)
- Rutas protegidas para usuarios autenticados (`/users/profile` y `/users/me/`)
- Simulación de una base de datos de usuarios y manejo de contraseñas con **bcrypt**

## Características

- **FastAPI** como framework principal
- **OAuth2** con el flujo de contraseña (Password Flow) para autenticación de usuarios
- **JWT** para la creación y verificación de tokens de acceso
- Verificación de contraseñas encriptadas con **bcrypt**
- **Dotenv** para la configuración de variables de entorno

## Estructura del Proyecto

- `main.py`: Define los endpoints y la lógica principal de autenticación.
- `Models.py`: Contiene los modelos de datos (User, UserInDB, Token, TokenData).
- `Users.py`: Simula una base de datos de usuarios.
- `utils.py`: Funciones auxiliares para la autenticación y manejo de tokens, contraseñas, y verificación de usuarios.

## Endpoints Principales

1. **/token** (POST): Obtiene un token de acceso.
2. **/token2** (POST): Similar a `/token`, pero usa una lógica diferente para crear el token.
3. **/users/profile** (GET): Muestra el perfil del usuario autenticado.
4. **/users/me/** (GET): Muestra la información del usuario actual.
5. **/users/me/items/** (GET): Muestra los ítems propios del usuario autenticado.

