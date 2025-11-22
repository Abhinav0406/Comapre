"""
Create simple placeholder PNG icons from the SVG logo
Uses PIL/Pillow to create basic icons
"""
from PIL import Image, ImageDraw
import os

def create_icon(size, filename):
    """Create a simple gradient icon"""
    # Create image with gradient background
    img = Image.new('RGB', (size, size), color='#667eea')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple comparison icon
    # Left document
    doc_left = [(size * 0.2, size * 0.2), (size * 0.45, size * 0.8)]
    draw.rectangle(doc_left, fill='white', outline='#764ba2', width=2)
    
    # Right document
    doc_right = [(size * 0.55, size * 0.2), (size * 0.8, size * 0.8)]
    draw.rectangle(doc_right, fill='white', outline='#764ba2', width=2)
    
    # Arrows in middle
    mid_x = size * 0.5
    arrow_y1 = size * 0.4
    arrow_y2 = size * 0.6
    
    # Left arrow
    draw.line([(size * 0.3, arrow_y1), (size * 0.45, arrow_y1)], fill='white', width=3)
    draw.polygon([(size * 0.45, arrow_y1 - 5), (size * 0.45, arrow_y1 + 5), (size * 0.5, arrow_y1)], fill='white')
    
    # Right arrow
    draw.line([(size * 0.5, arrow_y2), (size * 0.65, arrow_y2)], fill='white', width=3)
    draw.polygon([(size * 0.65, arrow_y2 - 5), (size * 0.65, arrow_y2 + 5), (size * 0.6, arrow_y2)], fill='white')
    
    # Save
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    img.save(filename)
    print(f"Created {filename} ({size}x{size})")

def main():
    # Create assets directory
    os.makedirs("assets", exist_ok=True)
    
    # Generate PWA icons
    create_icon(192, "icon-192.png")
    create_icon(512, "icon-512.png")
    
    # Generate Electron icons
    for size in [16, 32, 48, 64, 128, 256, 512]:
        create_icon(size, f"assets/icon-{size}.png")
    
    print("\nPlaceholder icons created!")
    print("For better quality icons, run: python generate_icons.py")

if __name__ == "__main__":
    main()

