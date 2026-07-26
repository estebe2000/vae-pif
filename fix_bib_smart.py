import shutil

target_file = 'VAE-MEEF-Bibliographie.bib'
backup_file = 'VAE-MEEF-Bibliographie.bib.bak_smart'

# Create backup
shutil.copy2(target_file, backup_file)

def generate_mojibake_map():
    mapping = {}
    
    # Handle C3 prefix (Latin-1 Supplement) -> Ã + char
    # UTF-8 bytes: C3 xx
    # Mojibake: Decode(C3, cp1252) + Decode(xx, cp1252)
    # Range of second byte for C3 is 80-BF (But C3 8x is 008x which is control/latin1 suppl)
    # Valid UTF-8 continuation is 80-BF.
    
    prefix = b'\xc3'
    prefix_char = prefix.decode('cp1252') # 'Ã'
    
    for b in range(0x80, 0xC0): # 128 to 191
        byte_val = bytes([b])
        try:
            # Reconstruct the intended UTF-8 char
            utf8_char = (prefix + byte_val).decode('utf-8')
            
            # Reconstruct the Mojibake sequence
            # Note: Some bytes in 80-9F range are undefined in cp1252 or special.
            # Windows-1252 maps 80-9F to printable chars (mostly).
            try:
                suffix_char = byte_val.decode('cp1252')
                mojibake = prefix_char + suffix_char
                mapping[mojibake] = utf8_char
            except UnicodeDecodeError:
                pass 
        except UnicodeDecodeError:
            pass

    # Handle C2 prefix (Latin-1 Supplement lower) -> Â + char
    prefix = b'\xc2'
    prefix_char = prefix.decode('cp1252') # 'Â'
    for b in range(0xA0, 0xC0): # A0 to BF (C2 80-9F is C1 control, often unused in text)
        byte_val = bytes([b])
        try:
            utf8_char = (prefix + byte_val).decode('utf-8')
            try:
                suffix_char = byte_val.decode('cp1252')
                mojibake = prefix_char + suffix_char
                mapping[mojibake] = utf8_char
            except:
                pass
        except:
            pass
            
    # Add 3-byte common sequences (mostly punctuation)
    # â€™ (E2 80 99) -> ’
    # â€“ (E2 80 93) -> –
    # â€œ (E2 80 9C) -> “
    # â€\x9d (E2 80 9D) -> ” (Note: 9D is undefined in pure CP1252 but often handled)
    
    # We construct them manually for safety
    manual_maps = {
        'â€™': '’',
        'â€“': '–',
        'â€œ': '“',
        'â€¦': '…',
        'Ã‰': 'É', # Specifically explicit for safety
    }
    mapping.update(manual_maps)
    
    # Handle the weird right quote if it appears differently
    # 9D in CP1252 might be read as nothing/error, but if it exists in string:
    # E2 80 9D
    try:
        s = b'\xe2\x80\x9d'.decode('utf-8') # ”
        # Mojibake representation:
        # E2 -> â
        # 80 -> €
        # 9D -> ? (Windows-1252 undefined)
        # If Python read it as \x9d or similar
        mapping['â€\x9d'] = s
    except:
        pass

    return mapping

def fix_file():
    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        mapping = generate_mojibake_map()
        
        # Sort keys by length descending to replace longest matches first (important for 3-byte vs 2-byte)
        sorted_keys = sorted(mapping.keys(), key=len, reverse=True)
        
        count = 0
        fixed_content = content
        for bad in sorted_keys:
            if bad in fixed_content:
                occurrences = fixed_content.count(bad)
                count += occurrences
                fixed_content = fixed_content.replace(bad, mapping[bad])
        
        print(f"Replaced {count} Mojibake sequences.")
        
        if count > 0:
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print("File saved.")
        else:
            print("No Mojibake found.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    fix_file()
