# TODO's generales

- [x] Hacer una página que permita  registrar nuevos pacientes
- [x] Hacer una página que permita actualizar el registro de un paciente
- [x] Añadir las funcionalidades de peso:
    - Que te muestre si bajaste o subiste de peso
    - ⬆ con la grasa, músculo, etc
    - Indicar si estás en los valores recomendados

## Página de registro

- Debe de tener campos para los datos básicos del usuario + su estado de peso inicial.
- Estos datos deben tener un botón de submit que guarde el registro en mongo

## Página de actualización

- Debe de tener inicialmente una tabla que muestre todos los usuarios registrados 
    (Tal vez solo nombre y fecha del ultimo registro)
- Una selectbox que contenga los nombres de los pacientes
- Una vez seleccionado el nombre en ⬆, debe poder introducir los nuevos datos de peso
- debe tener un boton de modificar que cree un nuevo registro de fecha.
- Al presionar el boton de modificar, debe desplegar en la parte inferior
    una comparación entre  el último registro (antes del ingresado) y el 
    registro recién ingresado