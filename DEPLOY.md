# Deployment Guide

## 🚀 Streamlit Cloud (Recommended - Easiest)

Streamlit Cloud is the best option for deploying Streamlit apps. It's free and made specifically for Streamlit.

### Steps:

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy to Streamlit Cloud:**
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Your app will be live at:**
   `https://<your-app-name>.streamlit.app`

---

## 🌐 Vercel (Alternative - Requires Setup)

Vercel doesn't natively support Streamlit, but you can use it with serverless functions. However, **Streamlit Cloud is much easier and recommended**.

### Option 1: Use Streamlit Cloud (Recommended)
This is the easiest and best option for Streamlit apps.

### Option 2: Convert to a Web App
If you want to use Vercel, you'd need to convert the app to a different framework (Flask/FastAPI + React), which requires significant changes.

---

## 📦 Other Deployment Options

### Railway
1. Go to https://railway.app/
2. New Project → Deploy from GitHub
3. Select your repo
4. Add build command: `pip install -r requirements.txt`
5. Add start command: `streamlit run app.py --server.port $PORT`

### Render
1. Go to https://render.com/
2. New → Web Service
3. Connect GitHub repo
4. Build command: `pip install -r requirements.txt`
5. Start command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

### Heroku
1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```
3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

---

## ✅ Recommended: Streamlit Cloud

For Streamlit apps, **Streamlit Cloud is the best choice** because:
- ✅ Free
- ✅ Made specifically for Streamlit
- ✅ One-click deployment from GitHub
- ✅ Automatic HTTPS
- ✅ No configuration needed
- ✅ Easy updates (just push to GitHub)

