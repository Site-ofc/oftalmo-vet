import os
from PIL import Image

def optimize_image(input_path, output_path, max_width=1920):
    with Image.open(input_path) as img:
        # Converter para RGB se necessário (ex: de PNG com transparência para JPG/WebP)
        if img.mode in ("RGBA", "P") and not output_path.endswith('.png'):
            img = img.convert("RGB")
        
        # Redimensionar se for muito larga
        if img.width > max_width:
            ratio = max_width / float(img.width)
            new_height = int(float(img.height) * float(ratio))
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # Salvar como WebP com boa qualidade
        if output_path.endswith('.webp'):
            img.save(output_path, "WEBP", quality=85, method=6)
        else:
            img.save(output_path, quality=90, optimize=True)

images_to_optimize = {
    'capa.png': 'capa.webp',
    'foto1_fachada.jpg': 'fachada.webp',
    'foto2_recente.jpg': 'recepcao.webp',
    'foto3_owner.jpg': 'corredor.webp',
    'foto4_streetview.jpg': 'consultorio.webp',
    'mascote_oftalmovet.png': 'mascote.png' # Manter PNG para transparência
}

os.makedirs('/home/ubuntu/oftalmovet/assets', exist_ok=True)

for src, dest in images_to_optimize.items():
    src_path = os.path.join('/home/ubuntu/oftalmovet', src)
    dest_path = os.path.join('/home/ubuntu/oftalmovet/assets', dest)
    if os.path.exists(src_path):
        print(f"Otimizando {src} -> {dest}")
        optimize_image(src_path, dest_path)
