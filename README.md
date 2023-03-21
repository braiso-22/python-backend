# python-backend
Una prueba usando python como backend con FastAPI

## Empezando

Para empezar a usar este proyecto, primero debes clonarlo en tu ordenador.

```bash
$ git clone https://github.com/braiso-22/python-backend
$ cd python-backend
```

Después tienes que instalar  las dependencias necesarias para el proyecto.

```bash
$ conda env create -f env.yaml fastapi
```

Puedes activar el entorno con el siguiente comando.

```bash
$ conda activate fastapi
```

## Ejecutando el proyecto

Para ejecutar el proyecto, debes ejecutar el siguiente comando.

```bash
$ uvicorn main:app --reload
```

Aparecera un mensaje de que está corriendo sobre http://127.0.0.1:8000
