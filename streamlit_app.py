import streamlit as st
import random

# Función para generar un ejercicio de cinemática
def generar_ejercicio():
    v0 = random.randint(5, 30)  # velocidad inicial en m/s
    a = random.randint(1, 10)   # aceleración en m/s²
    t = random.randint(1, 10)   # tiempo en segundos
    # Fórmula de la posición final: x = v0 * t + (1/2) * a * t²
    x = v0 * t + (0.5 * a * t ** 2)
    return v0, a, t, x

# Título de la aplicación
st.title("Ejercicios de Cinemática")

# Generar un ejercicio
v0, a, t, respuesta_correcta = generar_ejercicio()

# Mostrar el ejercicio
st.subheader("Ejercicio:")
st.write(f"Un objeto se mueve con una velocidad inicial de **{v0} m/s** y una aceleración de **{a} m/s²** durante **{t} segundos**.")
st.write("Calcula la posición final del objeto.")

# Input para la respuesta del usuario
respuesta_usuario = st.number_input("Tu respuesta (en metros):", step=1.0)

# Botón para verificar la respuesta
if st.button("Verificar respuesta"):
    if respuesta_usuario == respuesta_correcta:
        st.success("¡Correcto! La posición final es efectivamente {:.2f} metros.".format(respuesta_correcta))
    else:
        st.error("Incorrecto. La posición final correcta es {:.2f} metros.".format(respuesta_correcta))

# Opción para generar un nuevo ejercicio
if st.button("Generar nuevo ejercicio"):
    st.experimental_rerun()
