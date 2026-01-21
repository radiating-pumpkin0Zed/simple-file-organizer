# File Organizer

A simple Python CLI tool to automatically organize files in a directory by their type.

## Features

- 📁 Organizes files into categorized folders (Images, Documents, Videos, etc.)
- 🔍 Dry-run mode to preview changes before executing
- 🛡️ Handles duplicate filenames automatically
- ⚡ Fast and lightweight
- 🎯 Works with common file types out of the box

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/file-organizer.git
cd file-organizer
```

2. Make sure you have Python 3.6+ installed:
```bash
python --version
```

## Usage

### Preview mode (dry-run)
See what would be organized without actually moving files:
```bash
python file_organizer.py /path/to/directory
```

### Execute mode
Actually organize the files:
```bash
python file_organizer.py /path/to/directory --execute
```

### Organize current directory
```bash
python file_organizer.py .
```

## File Categories

The tool organizes files into the following categories:

- **Images**: jpg, jpeg, png, gif, bmp, svg, webp, ico
- **Documents**: pdf, doc, docx, txt, rtf, odt, xls, xlsx, ppt, pptx
- **Videos**: mp4, avi, mkv, mov, wmv, flv, webm
- **Audio**: mp3, wav, flac, aac, ogg, wma, m4a
- **Archives**: zip, rar, 7z, tar, gz, bz2
- **Code**: py, js, html, css, java, cpp, c, php, rb, go
- **Executables**: exe, msi, apk, app, dmg
- **Others**: Any file type not listed above

## Example

Before:
```
Downloads/
├── photo.jpg
├── document.pdf
├── song.mp3
├── video.mp4
└── script.py
```

After running with `--execute`:
```
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── document.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── video.mp4
└── Code/
    └── script.py
```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

MIT License - feel free to use this project however you'd like!

## Author

Your Name - [GitHub Profile](https://github.com/YOUR_USERNAME)