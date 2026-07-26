
import os

def fix_bib(file_path, backup_path):
    # Try reading the backup with different encodings
    content = ""
    try:
        with open(backup_path, 'r', encoding='utf-16') as f:
            content = f.read()
    except UnicodeError:
        try:
            with open(backup_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeError:
            with open(backup_path, 'r', encoding='latin-1') as f:
                content = f.read()

    # Remove null bytes if any
    content = content.replace('\x00', '')

    # Missing entries to append
    missing_entries = """

% ===========================
% X. RÉFÉRENCES MANQUANTES (AJOUTÉES POUR COMPILATION)
% ===========================

@article{star_griesemer_boundary_objects,
  author = {Star, Susan Leigh and Griesemer, James R.},
  title = {Institutional Ecology, 'Translations' and Boundary Objects: Amateurs and Professionals in Berkeley's Museum of Vertebrate Zoology, 1907-39},
  journal = {Social Studies of Science},
  volume = {19},
  number = {3},
  pages = {387--420},
  year = {1989},
  publisher = {Sage Publications}
}

@misc{projet_methode_tlem,
  author = {Huber, M.},
  title = {Apprendre en projets : la pédagogie du projet-élèves},
  publisher = {Chronique sociale},
  year = {2005},
  note = {Méthodologie de projet}
}
"""
    
    # Check if missing entries are already present to avoid duplication
    if "star_griesemer_boundary_objects" not in content:
        content += missing_entries

    # Fix 'and others' if present (simple replace)
    content = content.replace("author = {Briant, N. and others}", "author = {Briant, N.}")
    content = content.replace("author  = {Briant, N. and others}", "author  = {Briant, N.}")

    # Write back to the main file as UTF-8
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully fixed {file_path}")

if __name__ == "__main__":
    base_dir = r"c:\Users\estebe\Documents\vae-5\vae-main-5"
    bib_file = os.path.join(base_dir, "VAE-MEEF-Bibliographie.bib")
    backup_file = os.path.join(base_dir, "VAE-MEEF-Bibliographie.bib.bak")
    
    if os.path.exists(backup_file):
        fix_bib(bib_file, backup_file)
    else:
        print("Backup file not found!")
