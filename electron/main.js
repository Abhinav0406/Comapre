const { app, BrowserWindow, shell } = require('electron');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

let mainWindow;
let streamlitProcess;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 1000,
    minHeight: 700,
    icon: path.join(__dirname, '../logo.svg'),
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      enableRemoteModule: false,
      webSecurity: true,
      preload: path.join(__dirname, 'preload.js')
    },
    titleBarStyle: 'default',
    show: false
  });

  // Start Streamlit server
  const streamlitPath = path.join(__dirname, '..');
  const pythonCommand = process.platform === 'win32' ? 'python' : 'python3';
  
  streamlitProcess = spawn(pythonCommand, ['-m', 'streamlit', 'run', 'app.py', '--server.headless', 'true'], {
    cwd: streamlitPath,
    env: { ...process.env, STREAMLIT_SERVER_PORT: '8501' }
  });

  streamlitProcess.stdout.on('data', (data) => {
    console.log(`Streamlit: ${data}`);
  });

  streamlitProcess.stderr.on('data', (data) => {
    console.error(`Streamlit Error: ${data}`);
  });

  // Wait for Streamlit to be ready, then load the app
  setTimeout(() => {
    mainWindow.loadURL('http://localhost:8501');
    mainWindow.show();
    
    // Open DevTools in development
    if (process.argv.includes('--dev')) {
      mainWindow.webContents.openDevTools();
    }
  }, 3000);

  // Handle window closed
  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  // Handle external links
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });
}

// App event handlers
app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  // Kill Streamlit process
  if (streamlitProcess) {
    streamlitProcess.kill();
  }
  
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', () => {
  // Ensure Streamlit is killed on quit
  if (streamlitProcess) {
    streamlitProcess.kill();
  }
});

// Handle certificate errors (for localhost)
app.on('certificate-error', (event, webContents, url, error, certificate, callback) => {
  if (url.startsWith('http://localhost')) {
    event.preventDefault();
    callback(true);
  } else {
    callback(false);
  }
});

