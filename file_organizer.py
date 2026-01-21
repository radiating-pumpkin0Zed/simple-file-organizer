import os
import shutil
from pathlib import Path
from collections import defaultdict

FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go'],
    'Executables': ['.exe', '.msi', '.apk', '.app', '.dmg'],
}

def get_file_category(file_extension):
    """Determine the category of a file based on its extension."""
    file_extension = file_extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return 'Others'

def organize_files(directory, dry_run=True):
    """
    Organize files in the specified directory.
    
    Args:
        directory: Path to the directory to organize.
        dry_run: If True, only print the actions without making changes.   
    """
    directory = Path(directory)
    
    if not directory.exists():
        print(f"Error: '{directory}' is not a directory!")
        return

    file_count = defaultdict(list)
    
    for item in directory.iterdir():
        if item.is_file():
            category = get_file_category(item.suffix)
            file_count[category].append(item)
    
    if not any(file_count.values()):
        print("No files to organize.")
        return
    
    print(f"\n{'='*60}")
    print(f"File Organization {'Preview' if dry_run else 'Report'}")
    print(f"Directory: {directory}")
    print(f"{'='*60}\n")
    
    total_files = sum(len(files) for files in file_count.values())
    print(f"Found {total_files} files to organize:\n")
    
    for category, files in file_count.items():
        print(f"{category}: {len(files)} file(s)")
        
    print(f"\n{'='*60}\n")
    
    if dry_run:
        print("DRY RUN MODE - No files will be moved")
        print("Run with --execute flag to actually organize files.\n")
        
        for category, files in sorted(file_count.items()):
            print(f"\n{category}:")
            for file in files[:5]:
                print(f" - {file.name}")
            if len(files) > 5:
                print(f" ... and {len(files) - 5} more files.")
    else:
        
        moved_count = 0
        for category, files in file_count.items():
            category_folder = directory / category
            category_folder.mkdir(exist_ok=True)
            
            for file in files:
                try: 
                    destination = category_folder / file.name
                    counter = 1
                    while destination.exists():
                        stem = file.stem
                        suffix = file.suffix
                        destination = category_folder / f"{stem}({counter}){suffix}"
                        counter += 1
                        
                    shutil.move(str(file), str(destination))
                    moved_count += 1
                    print(f"Moved: {file.name} -> {category}/")
                
                except Exception as e:
                    print(f"Error moving file {file.name}: {e}")
                    
        print(f"\n✓ Successfully organized {moved_count} file(s)!")
        
def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Organize files in a directory by type',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python file_organizer.py ~/Downloads              # Preview organization
  python file_organizer.py ~/Downloads --execute    # Actually organize files
        """
    )
    
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Directory to organize (default: current directory)'
    )
    
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Actually move files (default is dry-run mode)'
    )
    
    args = parser.parse_args()
    
    organize_files(args.directory, dry_run=not args.execute)

if __name__ == '__main__':
    main()