import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App'
import './index.css'

// DEMO mode: render the whole UI with sample data and no backend (VITE_DEMO=1).
if (import.meta.env.VITE_DEMO === '1') {
  const { installMock } = await import('./demo/installMock')
  installMock()
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
