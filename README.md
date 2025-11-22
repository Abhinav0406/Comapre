# File Compare Tool

A powerful web application for comparing CSV and Excel files side-by-side with visual highlighting. Available as a Progressive Web App (PWA) and Electron desktop application.

## Features

- 📊 Compare CSV and Excel files (.xlsx, .xls)
- 🔍 Visual highlighting of differences
- 📈 Order-agnostic row comparison
- 📥 Export results to CSV or Excel
- 🎨 Modern, responsive UI
- 🔄 Text numbers treated as equal to numeric values (e.g., "123" = 123)

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Generate icons (optional, for PWA/Electron):
```bash
pip install cairosvg pillow
python generate_icons.py
```

## Usage

### Web App (Streamlit)

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

### Electron Desktop App

1. Install Electron dependencies:
```bash
npm install
```

2. Run Electron app:
```bash
npm run electron
```

3. Build for distribution:
```bash
# Windows
npm run build:win

# macOS
npm run build:mac

# Linux
npm run build:linux

# All platforms
npm run build:all
```

### Progressive Web App (PWA)

1. Deploy the Streamlit app to a web server
2. Ensure `manifest.json` and `service-worker.js` are accessible
3. Users can install the app from their browser

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── compare.py             # Comparison logic
├── logo.svg              # App logo (SVG)
├── manifest.json         # PWA manifest
├── service-worker.js     # PWA service worker
├── package.json          # Electron configuration
├── electron/
│   ├── main.js          # Electron main process
│   └── preload.js       # Electron preload script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Development

### Running in Development Mode

**Streamlit:**
```bash
streamlit run app.py
```

**Electron (with DevTools):**
```bash
npm run electron:dev
```

## Building

### Electron Builds

Builds are configured in `package.json` using electron-builder. Output will be in the `dist/` directory.

### PWA Deployment

1. Deploy your Streamlit app (e.g., Streamlit Cloud, Heroku, etc.)
2. Ensure all PWA files are accessible:
   - `manifest.json`
   - `service-worker.js`
   - Icon files (`icon-192.png`, `icon-512.png`)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

