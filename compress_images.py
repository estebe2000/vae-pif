from PIL import Image
import os
import sys

def compress_image(file_path, max_size_mb=1.0):
    try:
        if not os.path.exists(file_path):
            return
        
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb <= max_size_mb:
            print(f"Skipping {file_path} ({file_size_mb:.2f} MB)")
            return

        print(f"Compressing {file_path} ({file_size_mb:.2f} MB)...")
        
        img = Image.open(file_path)
        
        # Convert RGBA to RGB if necessary (for saving as JPEG)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        # Save as JPEG with lower quality iteratively until size is met
        quality = 90
        step = 5
        filename, ext = os.path.splitext(file_path)
        # We might change extension to .jpg for better compression if it's png
        # But user might refer to .png in latex. 
        # Latex handles .png, but .jpg is smaller.
        # If we change ext, we break latex references unless we update them.
        # So we try to keep ext if possible, or force overwrite as generic format?
        # PNG is hard to compress below 1MB if it's large complex image.
        # Strategy: Resize if extremely large dimensions, then optimize.
        
        # Let's try resizing first if > 2000px width/height?
        max_dim = 2048
        if max(img.size) > max_dim:
             ratio = max_dim / max(img.size)
             new_size = (int(img.size[0]*ratio), int(img.size[1]*ratio))
             img = img.resize(new_size, Image.Resampling.LANCZOS)
             
        # For PNG, we can only do so much. If originally PNG and massive, suggest converting to JPG.
        # However, checking if replacing with same name works. 
        # If file is .png, saving as .png with optimize=True.
        
        if ext.lower() == '.png':
            # Try saving as optimized PNG first
            img.save(file_path, "PNG", optimize=True)
            if os.path.getsize(file_path) / (1024*1024) > max_size_mb:
                # If still too big, convert to JPG but keep .png extension ?? No that's bad.
                # We strictly need <1MB. 
                # Converting to JPG is best bet. 
                # We will save as .jpg and user might need to update latex, 
                # OR we just resize strictly until it fits.
                pass
        
        # If still too big or is JPG, use JPEG compression
        current_path = file_path
        
        # If we must stick to original format for compatibility?
        # Let's try to aggressively resize if still too big.
        while os.path.getsize(current_path) / (1024*1024) > max_size_mb and quality > 10:
             # Just resize down by 10% each time? or use JPEG compression if jpg
             if ext.lower() in ['.jpg', '.jpeg']:
                 img.save(current_path, "JPEG", quality=quality)
                 quality -= step
             else:
                 # For PNG, Resize is main tool
                 w, h = img.size
                 img = img.resize((int(w*0.9), int(h*0.9)), Image.Resampling.LANCZOS)
                 img.save(current_path, optimize=True)
                 
        print(f"Final size: {os.path.getsize(current_path) / (1024*1024):.2f} MB")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for f in sys.argv[1:]:
            compress_image(f)
    else:
        # Default behavior: scan sources/medias
        target_dir = 'sources/medias'
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    compress_image(os.path.join(root, file))
