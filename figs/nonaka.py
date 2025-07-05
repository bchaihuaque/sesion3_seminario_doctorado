import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(10, 8))

# Dibujar líneas del cuadrante
ax.axhline(0.5, color='black', linewidth=2)
ax.axvline(0.5, color='black', linewidth=2)

# Definir posiciones y textos
cuadrantes = {
    "SOCIALIZACION": (0.25, 0.75, ["• Comunicación cara a cara", "• Experiencia compartida"], "Empatizando"),
    "EXTERIORIZACION": (0.75, 0.75, ["• Desarrollo de conceptos para comunicar"], "Expresando"),
    "INTERIORIZACION": (0.25, 0.25, ["• Incorporación al conocimiento personal"], "Incorporando"),
    "COMBINACION": (0.75, 0.25, ["• Combinación de conocimiento explícito"], "Conectando"),
}

# Añadir textos
for titulo, (x, y, bullets, verbo) in cuadrantes.items():
    ax.text(x, y + 0.1, titulo, ha='center', va='center', fontsize=14, weight='bold', color='navy')
    for i, bullet in enumerate(bullets):
        ax.text(x, y - 0.02 * i, bullet, ha='center', va='center', fontsize=12, color='black')
    ax.text(x, y - 0.08 * len(bullets), verbo, ha='center', va='center', fontsize=11, style='italic', color='slategray')

# Flechas de conversión
arrow_style = dict(arrowstyle='->', color='royalblue', linewidth=2)
ax.annotate('', xy=(0.5, 1.0), xytext=(0.25, 0.85), arrowprops=arrow_style)
ax.annotate('', xy=(1.0, 0.5), xytext=(0.85, 0.75), arrowprops=arrow_style)
ax.annotate('', xy=(0.5, 0.0), xytext=(0.75, 0.15), arrowprops=arrow_style)
ax.annotate('', xy=(0.0, 0.5), xytext=(0.15, 0.25), arrowprops=arrow_style)

# Etiquetas de los ejes
ax.text(0.5, 1.05, "Tácito", ha='center', fontsize=14, weight='bold')
ax.text(0.5, -0.08, "Explícito", ha='center', fontsize=14, weight='bold')
ax.text(-0.08, 0.5, "Tácito", va='center', rotation='vertical', fontsize=14, weight='bold')
ax.text(1.05, 0.5, "Explícito", va='center', rotation='vertical', fontsize=14, weight='bold')

# Espiral en el centro
spiral = patches.Arc((0.5, 0.5), 0.15, 0.15, theta1=0, theta2=360, color='black')
ax.add_patch(spiral)

# Formato general
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Fuente
ax.text(1.02, 0.05, "Fuente: Modelo SECI – Nonaka y Takeuchi", rotation=90, fontsize=9, va='bottom')

plt.tight_layout()
plt.show()
