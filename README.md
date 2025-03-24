# Watermark WebP

A simple Python script to add a watermark to `.webp` images. The script scans an `input` folder for images, applies a diagonal watermark, and saves the processed images to an `output` folder.

## Features

- Supports `.webp` format
- Adds a diagonal watermark text across the entire image
- Includes a subtle shadow for better visibility
- Automatically processes all images in the `input` folder
- Saves the output in the `output` folder

## Requirements

Make sure you have Python installed along with the required dependencies:

```bash
pip install pillow
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Booth-Ashley/Watermark-WebP.git
cd watermark-webp
```

2. Place your `.webp` images inside the `input` folder.

3. Run the script:

```bash
python watermark.py
```

4. The watermarked images will be saved in the `output` folder.

## Customization

You can modify the following parameters in the script to better suit your needs:

### Watermark Text

- **Change the watermark text** by modifying the `watermark_text` parameter in the script:
  ```python
  watermark_text = " ©YourCustomText"
  ```

### Font Size

- **Adjust the font size** by changing the division factor in:
  ```python
  font = ImageFont.truetype("arial.ttf", int(width / 12))
  ```
  - Increase the divisor (`/12`) for a smaller font.
  - Decrease it for a larger font.

### Text Spacing

- **Modify text density** by adjusting `step_x` and `step_y`:
  ```python
  step_x = text_width * 1  # Horizontal spacing
  step_y = text_height * 2  # Vertical spacing
  ```
  - Increase values for more spaced-out text.
  - Decrease values for a denser watermark pattern.

### Shadow Opacity

- **Increase or decrease watermark visibility** by modifying the shadow fill opacity:
  ```python
  draw.text((x + 2, y + 2), watermark_text, fill=(0, 0, 0, 20), font=font)
  ```
  - Increase `20` to a higher value (e.g., `50`) for a darker shadow.
  - Reduce it for a lighter shadow.

### Watermark Transparency

- **Adjust the opacity of the main watermark text** by modifying this line:
  ```python
  draw.text((x, y), watermark_text, fill=(255, 255, 255, 50), font=font)
  ```
  - Increase `50` for a stronger watermark.
  - Decrease it for a more subtle effect.

## License

This project is licensed under the MIT License.

## Author

[Ashley Booth](https://github.com/Booth-Ashley)

