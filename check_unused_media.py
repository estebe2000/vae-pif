import os
import re

def find_used_images(root_dir):
    used_images = set()
    tex_files = []
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.tex'):
                tex_files.append(os.path.join(root, file))
    
    print(f"Scanning {len(tex_files)} .tex files...")
    
    for tex_file in tex_files:
        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Regex for \includegraphics[...]{path} or \includegraphics{path}
                matches = re.findall(r'\\includegraphics(?:\[.*?\])?\{(.*?)\}', content)
                for match in matches:
                    # Normalize path: generic separators, ignore extensions sometimes
                    path = match.strip()
                    basename = os.path.basename(path)
                    used_images.add(basename)
                    # Also add without extension just in case
                    used_images.add(os.path.splitext(basename)[0])
        except Exception as e:
            print(f"Error reading {tex_file}: {e}")
            
    return used_images

def check_unused(media_dir, used_set):
    unused = []
    print(f"\nChecking directory: {media_dir}")
    if not os.path.exists(media_dir):
        print("Media directory not found.")
        return []

    for f in os.listdir(media_dir):
        if os.path.isfile(os.path.join(media_dir, f)):
            # Check if file is in used list
            # We check strict equality, and also filename without extension
            name = f
            name_no_ext = os.path.splitext(f)[0]
            
            if name in used_set or name_no_ext in used_set:
                pass # It is used
            else:
                unused.append(f)
                
    return unused

if __name__ == '__main__':
    root = '.'
    media_dir = 'sources/medias'
    
    used = find_used_images(root)
    print(f"Found {len(used)} referenced distinct image filenames/basenames.")
    
    unused_files = check_unused(media_dir, used)
    
    print("\n--- Unused Files in sources/medias ---")
    for f in unused_files:
        print(f"[UNUSED] {f}")
        
    print(f"\nTotal unused files: {len(unused_files)}")
