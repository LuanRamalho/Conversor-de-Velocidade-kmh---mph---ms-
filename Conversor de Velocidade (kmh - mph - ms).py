import tkinter as tk
from tkinter import ttk

def converter():
    try:
        # Obtém o valor inserido pelo usuário
        km_h = float(entry_kmh.get())
        # Converte para m/s e mph
        m_s = km_h / 3.6
        mph = km_h / 1.609
        
        # Exibe os resultados
        label_result_ms.config(text=f"{m_s:.2f} m/s")
        label_result_mph.config(text=f"{mph:.2f} mph")
    except ValueError:
        label_result_ms.config(text="Erro: valor inválido!")
        label_result_mph.config(text="")

# Configura a janela principal
root = tk.Tk()
root.title("Conversor de Velocidade")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#1e90ff")  # Fundo azul

# Título
title = tk.Label(root, text="Conversor de Velocidade", font=("Arial", 18, "bold"), bg="#1e90ff", fg="white")
title.pack(pady=10)

# Entrada para o valor em km/h
frame_input = tk.Frame(root, bg="#1e90ff")
frame_input.pack(pady=10)
label_kmh = tk.Label(frame_input, text="Digite a velocidade (km/h):", font=("Arial", 12), bg="#1e90ff", fg="white")
label_kmh.pack(side="left", padx=5)
entry_kmh = ttk.Entry(frame_input, font=("Arial", 12))
entry_kmh.pack(side="left", padx=5)

# Botão para converter
btn_converter = tk.Button(root, text="Converter", command=converter, font=("Arial", 12, "bold"), bg="yellow", fg="orangered")
btn_converter.pack(pady=10)

# Resultados
frame_results = tk.Frame(root, bg="#1e90ff")
frame_results.pack(pady=10)
label_result_ms = tk.Label(frame_results, text="0.00 m/s", font=("Arial", 14), bg="#1e90ff", fg="white")
label_result_ms.pack(pady=5)
label_result_mph = tk.Label(frame_results, text="0.00 mph", font=("Arial", 14), bg="#1e90ff", fg="white")
label_result_mph.pack(pady=5)

# Inicia o loop da aplicação
root.mainloop()
