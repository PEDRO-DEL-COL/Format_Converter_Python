import os
import ffmpeg

# Definição das pastas
input_folder = r'C:\Users\pedro\Documents\AI_Training\input'
output_folder = r'C:\Users\pedro\Documents\AI_Training\output'

# Garante que as pastas existem
os.makedirs(output_folder, exist_ok=True)

def converter_mkv_para_mov(input_filename):
    input_path = os.path.join(input_folder, input_filename)
    output_filename = os.path.splitext(input_filename)[0] + ".mov"  # Mantém o nome, troca a extensão
    output_path = os.path.join(output_folder, output_filename)

    if not os.path.exists(input_path):
        print(f"Erro: O arquivo {input_path} não foi encontrado!")
        return

    try:
        ffmpeg.input(input_path).output(output_path).run(overwrite_output=True)
        print(f"Conversão concluída: {output_path}")
    except ffmpeg.Error as e:
        print(f"Erro durante a conversão: {e}")

# Converte todos os arquivos .mkv na pasta input
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".mkv"):
        converter_mkv_para_mov(filename)
