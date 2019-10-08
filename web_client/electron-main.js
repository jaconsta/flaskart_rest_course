const { app, BrowserWindow } = require('electron')

// Global variable to prevent garbage collector.
let mainWindow

const createWindow = () => {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
  })

  mainWindow.loadURL('http://localhost:3000')

  // Open dev tools
  mainWindow.webContents.openDevTools()

  mainWindow.on('closed', () => mainWindow = null)
}

app.on('ready', createWindow)

// Quit when all windows are closed
app.on('window-all-closed', () => {
  // Prevent quit on macOS
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // MacOs If all windows are closing, open the app
  if (mainWindow === null) {
    createWindow()
  }
})
