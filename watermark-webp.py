from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(image_path, output_path, watermark_text=" ©YourCustomText"):
    image = Image.open(image_path).convert("RGBA")
    width, height = image.size
    
    watermark = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)
    
    try:
        font = ImageFont.truetype("arial.ttf", int(width / 12))
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    step_x = text_width * 1
    step_y = text_height * 2
    
    for x in range(-step_x, width, step_x):
        for y in range(-step_y, height, step_y):
            draw.text((x + 2, y + 2), watermark_text, fill=(0, 0, 0, 20), font=font)
            draw.text((x, y), watermark_text, fill=(255, 255, 255, 50), font=font)
    
    watermarked_image = Image.alpha_composite(image, watermark)
    
    watermarked_image.convert("RGB").save(output_path, "WEBP")
    
input_folder = "input"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".webp"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        add_watermark(input_path, output_path)
        print(f"Watermarked {filename} and saved to {output_path}")