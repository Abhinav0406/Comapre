# Quick Start Guide

## 🚀 Running the Web App

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   streamlit run app.py
   ```

3. **Open in browser:**
   Navigate to `http://localhost:8501`

## 📱 Using as PWA

1. Deploy the app to a web server (Streamlit Cloud, Heroku, etc.)
2. Ensure `manifest.json` and `service-worker.js` are accessible
3. Users can install the app from their browser's install prompt

## 💻 Running Electron Desktop App

1. **Install Node.js** (if not already installed):
   - Download from https://nodejs.org/

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run Electron app:**
   ```bash
   npm run electron
   ```

4. **Build for distribution:**
   ```bash
   # Windows
   npm run build:win
   
   # macOS  
   npm run build:mac
   
   # Linux
   npm run build:linux
   ```

## 🎨 Logo & Icons

Icons have been generated automatically. For higher quality icons from the SVG:

```bash
pip install cairosvg pillow
python generate_icons.py
```

## 📝 Notes

- The app automatically treats text numbers (e.g., "123") as equal to numeric values (123)
- Supports CSV and Excel files (.xlsx, .xls)
- All comparison results can be exported to CSV or Excel

