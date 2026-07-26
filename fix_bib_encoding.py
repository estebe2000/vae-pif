import shutil
import os

target_file = 'VAE-MEEF-Bibliographie.bib'
backup_file = 'VAE-MEEF-Bibliographie.bib.bak_encoding'

# Create backup
shutil.copy2(target_file, backup_file)

try:
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The file content is "Mojibake": UTF-8 bytes read as Windows-1252
    # To fix: Encode back to Windows-1252 bytes, then decode as UTF-8
    fixed_content = content.encode('cp1252').decode('utf-8')

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Successfully fixed encoding.")

except UnicodeEncodeError as e:
    print(f"Error: Could not encode with cp1252. The file might contain characters not in Windows-1252. {e}")
    # Fallback: Replace common patterns manually
    replacements = {
        'Ã©': 'é',
        'Ã¨': 'è',
        'Ã\xa0': 'à', # Ã + NBSP
        'Ã ': 'à',    # Ã + space (sometimes converted)
        'Ã¢': 'â',
        'Ãª': 'ê',
        'Ã®': 'î',
        'Ã´': 'ô',
        'Ãû': 'û',
        'Ã«': 'ë',
        'Ã¯': 'ï',
        'Ã¼': 'ü',
        'Ã§': 'ç',
        'Ã‰': 'É',
        'Ã€': 'À',
        'Ã\x89': 'É', # Alternative representation
        'â€™': "'",   # Smart quote mojibake often seen
        'â€œ': '"',
        'â€\x9d': '"',
    }
    fixed_content = content
    for bad, good in replacements.items():
        fixed_content = fixed_content.replace(bad, good)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    print("Applied manual replacements as fallback.")

except UnicodeDecodeError as e:
    print(f"Error: Could not decode bytes as UTF-8. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
