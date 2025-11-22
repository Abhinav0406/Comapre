# File Compare Tool

A powerful web application for comparing CSV and Excel files side-by-side with visual highlighting. Upload two files and instantly see differences with an intuitive, modern interface.

## Features

- 📊 **Compare CSV and Excel files** (.xlsx, .xls)
- 🔍 **Visual highlighting** of differences in red
- 📈 **Order-agnostic comparison** - finds rows that don't match regardless of order
- 📥 **Export results** to CSV or Excel format
- 🎨 **Modern, clean UI** with compact design
- 🔄 **Smart comparison** - treats text numbers as equal to numeric values (e.g., "123" = 123)
- 📱 **Progressive Web App (PWA)** - installable on mobile and desktop
- 💻 **Electron desktop app** - run as a native desktop application

## How It Works

1. **Upload two files** - CSV or Excel format
2. **Click Compare** - the app automatically detects file types and encoding
3. **View differences** - side-by-side comparison with highlighted differences
4. **Export results** - download comparison reports in CSV or Excel format

## Comparison Features

- **Cell-by-cell comparison** with visual highlighting
- **Order-agnostic row matching** - finds unmatched rows even if files have different row orders
- **Text/number normalization** - "123" (text) is treated as equal to 123 (number)
- **Compact diff view** - see only the differences in a clean format
- **Multiple export options** - CSV, Excel with highlighting, side-by-side reports

## Use Cases

- Compare inventory exports from different systems
- Verify data migrations and transfers
- Find discrepancies between file versions
- Audit data consistency across sources
- Quick data validation and quality checks

## Technology

Built with:
- **Streamlit** - Python web framework
- **Pandas** - Data analysis and comparison
- **OpenPyXL** - Excel file handling
- **Electron** - Desktop app wrapper
- **PWA** - Progressive Web App support



                              **THANK YOU**