"""
Script to generate PNG icons from SVG logo for PWA and Electron
Requires: pip install cairosvg pillow
"""
import os
try:
    import cairosvg
    from PIL import Image
    import io
except ImportError:
    print("Installing required packages...")
    os.system("pip install cairosvg pillow")
    import cairosvg
    from PIL import Image
    import io

def generate_icon(size, output_path):
    """Generate PNG icon from SVG"""
    svg_path = "logo.svg"
    if not os.path.exists(svg_path):
        print(f"Error: {svg_path} not found")
        return False
    
    try:
        # Convert SVG to PNG
        png_data = cairosvg.svg2png(url=svg_path, output_width=size, output_height=size)
        
        # Save PNG
        with open(output_path, 'wb') as f:
            f.write(png_data)
        
        print(f"Generated {output_path} ({size}x{size})")
        return True
    except Exception as e:
        print(f"Error generating {output_path}: {e}")
        return False

def main():
    # Create assets directory if it doesn't exist
    os.makedirs("assets", exist_ok=True)
    
    # Generate icons for PWA
    sizes = [192, 512]
    for size in sizes:
        generate_icon(size, f"icon-{size}.png")
    
    # Generate icons for Electron
    electron_sizes = [16, 32, 48, 64, 128, 256, 512]
    for size in electron_sizes:
        generate_icon(size, f"assets/icon-{size}.png")
    
    # Generate Windows ICO (requires additional conversion)
    print("\nNote: For Windows .ico file, you may need to use an online converter")
    print("or install: pip install icoextract")
    
    print("\nIcon generation complete!")

if __name__ == "__main__":
    main()

