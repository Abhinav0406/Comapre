#!/bin/bash

# Setup script for File Compare Tool

echo "🚀 Setting up File Compare Tool..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found. Electron features will not be available."
    echo "   Install Node.js from https://nodejs.org/"
else
    # Install Node dependencies
    echo "📦 Installing Node.js dependencies..."
    npm install
fi

# Generate icons if possible
if command -v python3 &> /dev/null; then
    echo "🎨 Generating icons..."
    pip install cairosvg pillow 2>/dev/null || echo "⚠️  Could not install icon generation dependencies"
    python3 generate_icons.py 2>/dev/null || echo "⚠️  Could not generate icons (this is optional)"
fi

echo "✅ Setup complete!"
echo ""
echo "To run the app:"
echo "  Web: streamlit run app.py"
echo "  Electron: npm run electron"

