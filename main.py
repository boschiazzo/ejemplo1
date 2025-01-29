import plotly.graph_objects as go

# Datos de ejemplo
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
temperaturas = [22, 24, 19, 21, 23]
horas = ["10:00", "12:30", "08:45", "14:15", "16:00"]  # Hora de medición

# Convertir horas a valores numéricos
hora_numerica = [10, 12.5, 8.75, 14.25, 16]  # Convertir "HH:MM" en horas decimales

# Crear la figura
fig = go.Figure()

# Agregar la temperatura al eje Y principal
fig.add_trace(go.Scatter(
    x=dias,
    y=temperaturas,
    mode="lines+markers",
    name="Temperatura (°C)",
    yaxis="y1"
))

# Agregar la hora al segundo eje Y
fig.add_trace(go.Scatter(
    x=dias,
    y=hora_numerica,
    mode="lines+markers",
    name="Hora de Medición",
    yaxis="y2",
    line=dict(dash="dot", color="red")
))


#NEW COMMENT : This is the third commit



# Configurar los ejes
fig.update_layout(
    title="Temperatura y Hora de Medición",
    xaxis=dict(title="Día"),

    # Configuración del eje Y principal
    yaxis=dict(
        title=dict(text="Temperatura (°C)", font=dict(color="blue")),
        tickfont=dict(color="blue"),
        side="left",
        position=0  # Mantiene el eje pegado a la izquierda
    ),

    # Configuración del eje Y secundario (moverlo un poco a la derecha)
    yaxis2=dict(
        title=dict(text="Hora de Medición", font=dict(color="red")),
        tickfont=dict(color="red"),
        overlaying="y",
        side="left",  # Sigue en la izquierda
        position=0.05,  # Lo movemos un poco a la derecha
        tickvals=[8, 10, 12, 14, 16],  # Valores del eje secundario
        ticktext=["08:00", "10:00", "12:00", "14:00", "16:00"]  # Mostrar etiquetas en formato hora
    )
)

# Mostrar el gráfico
fig.show()
