import os
from PIL import Image

folder = r"f:\Projetos_Teste\Mapa_Imob\SOTM_SITE\docs\assets\img\Cidade"
max_width = 1600

for filename in os.listdir(folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        filepath = os.path.join(folder, filename)
        try:
            with Image.open(filepath) as img:
                # Manter proporção
                if img.width > max_width:
                    w_percent = (max_width / float(img.width))
                    h_size = int((float(img.height) * float(w_percent)))
                    img = img.resize((max_width, h_size), Image.Resampling.LANCZOS)
                
                print(f"Comprimindo: {filename}")
                img.save(filepath, "JPEG", optimize=True, quality=80)
        except Exception as e:
            print(f"Erro ao processar {filename}: {e}")

print("Processo concluído!")
