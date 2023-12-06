from PIL import Image, ImageDraw, ImageFont
import random


def add_watermark(input_image_path, output_image_path, watermark_text=None, watermark_image_path=None):
    # Open the original image
    original_image = Image.open(input_image_path)
    
    # Create a drawing object
    draw = ImageDraw.Draw(original_image)
    
    def generate_text_style(style):
        font_size = random.randint(30, 50)  # Adjust the font size range as needed
        font = ImageFont.truetype("arial.ttf", font_size)  # You can change the font type if needed
        text = watermark_text

        # Get text size
        text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]

        if style == 'big':
            # Only one text, big font
            x_position = (original_image.width - text_width) // 2
            y_position = (original_image.height - text_height) // 2
            draw.text((x_position, y_position), text, font=font, fill=(255, 255, 255, 128))

        elif style == 'vertical':
            # Many texts in vertical direction, organized in lines with equal spacing
            line_count = 5  # Adjust the number of lines as needed
            spacing = original_image.height // (line_count + 1)
            for i in range(line_count):
                x_position = random.randint(0, original_image.width - text_width)
                y_position = (i + 1) * spacing
                draw.text((x_position, y_position), text * 5, font=font, fill=(255, 255, 255, 128))

        elif style == 'diagonal_up':
            # Many texts from bottom left to top right, organized in lines with equal spacing
            line_count = 5  # Adjust the number of lines as needed
            spacing = original_image.width // (line_count + 1)
            for i in range(line_count):
                x_position = (i + 1) * spacing
                y_position = original_image.height - (i + 1) * text_height
                draw.text((x_position, y_position), text * 5, font=font, fill=(255, 255, 255, 128))

        elif style == 'diagonal_down':
            # Many texts from bottom right to top left, organized in lines with equal spacing
            line_count = 5  # Adjust the number of lines as needed
            spacing = original_image.width // (line_count + 1)
            for i in range(line_count):
                x_position = original_image.width - (i + 1) * spacing
                y_position = (i + 1) * text_height
                draw.text((x_position, y_position), text * 5, font=font, fill=(255, 255, 255, 128))
    
    # Choose a random style
    styles = ['big', 'vertical', 'diagonal_up', 'diagonal_down']
    selected_style = random.choice(styles)

    generate_text_style(selected_style)

    # Save the watermarked image
    original_image.save(output_image_path)
    

    # elif watermark_image_path:
    #     # Add image watermark
    #     watermark = Image.open(watermark_image_path)
    #     watermark = watermark.resize((original_image.width // 4, original_image.height // 4))
    #     original_image.paste(watermark, (10, 10), watermark)
        
    # # Save the watermarked image
    # original_image.save(output_image_path)
    
if __name__ == "__main__":
    input_image_path = r"C:\Users\hoang\OneDrive\Desktop\nghich_prj\remove_watermarks\data\raw\Abstract_architecture\image_1_20231205183613104_d6f425d0-b659-4d11-9f98-5afd9a2ee706.jpg"
    output_image_path = r"C:\Users\hoang\OneDrive\Desktop\nghich_prj\remove_watermarks\data\watermark\image_1_20231205183613104_d6f425d0-b659-4d11-9f98-5afd9a2ee706.jpg"
    
    
    watermark_text = "Your Watermark Text"
    add_watermark(input_image_path, output_image_path, watermark_text=watermark_text)