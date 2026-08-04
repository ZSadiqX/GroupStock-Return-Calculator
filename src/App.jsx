import { useState } from 'react'

function App() {
  const [formData, setFormData] = useState({
    stock_symbol: '',
    buy_price: '',
    current_price: '',
    quantity: '',
    fees: '0',
    dividends: '0'
  })

  const [results, setResults] = useState(null)
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResults(null)

    try {
      const response = await fetch('/api/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          buy_price: parseFloat(formData.buy_price),
          current_price: parseFloat(formData.current_price),
          quantity: parseInt(formData.quantity, 10),
          fees: parseFloat(formData.fees || 0),
          dividends: parseFloat(formData.dividends || 0)
        })
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || 'Failed to calculate')
      }

      setResults(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const getStatusClass = (net_pl) => {
    if (net_pl > 0) return 'profit'
    if (net_pl < 0) return 'loss'
    return 'break-even'
  }

  const getStatusText = (net_pl) => {
    if (net_pl > 0) return '✅ Profit'
    if (net_pl < 0) return '❌ Loss'
    return '➖ Break-even'
  }

  return (
    <div className="container">
      <div className="glass-card">
        <h1 className="title">GroupStock Calculator</h1>
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="stock_symbol">Stock Symbol</label>
            <input 
              type="text" 
              id="stock_symbol"
              name="stock_symbol"
              placeholder="e.g. AAPL"
              value={formData.stock_symbol}
              onChange={handleChange}
              required
            />
          </div>

          <div style={{ display: 'flex', gap: '1rem' }}>
            <div className="form-group" style={{ flex: 1 }}>
              <label htmlFor="buy_price">Buy Price ($)</label>
              <input 
                type="number" 
                id="buy_price"
                name="buy_price"
                step="0.01"
                min="0"
                value={formData.buy_price}
                onChange={handleChange}
                required
              />
            </div>
            
            <div className="form-group" style={{ flex: 1 }}>
              <label htmlFor="current_price">Current Price ($)</label>
              <input 
                type="number" 
                id="current_price"
                name="current_price"
                step="0.01"
                min="0"
                value={formData.current_price}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="quantity">Quantity (Shares)</label>
            <input 
              type="number" 
              id="quantity"
              name="quantity"
              min="1"
              value={formData.quantity}
              onChange={handleChange}
              required
            />
          </div>

          <div style={{ display: 'flex', gap: '1rem' }}>
            <div className="form-group" style={{ flex: 1 }}>
              <label htmlFor="fees">Brokerage Fees ($)</label>
              <input 
                type="number" 
                id="fees"
                name="fees"
                step="0.01"
                min="0"
                value={formData.fees}
                onChange={handleChange}
              />
            </div>
            
            <div className="form-group" style={{ flex: 1 }}>
              <label htmlFor="dividends">Dividends Received ($)</label>
              <input 
                type="number" 
                id="dividends"
                name="dividends"
                step="0.01"
                min="0"
                value={formData.dividends}
                onChange={handleChange}
              />
            </div>
          </div>

          <button type="submit" className="btn-submit" disabled={loading}>
            {loading ? 'Calculating...' : 'Calculate Return'}
          </button>
        </form>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {results && (
          <div className="results-card">
            <h3>Calculated Metrics {formData.stock_symbol ? `for ${formData.stock_symbol.toUpperCase()}` : ''}</h3>
            
            <div className="result-row">
              <span className="result-label">Total Investment:</span>
              <span className="result-value">${results['Total Investment'].toFixed(2)}</span>
            </div>
            
            <div className="result-row">
              <span className="result-label">Current Value:</span>
              <span className="result-value">${results['Current Value'].toFixed(2)}</span>
            </div>
            
            <div className="result-row">
              <span className="result-label">Net Profit/Loss:</span>
              <span className={`result-value ${getStatusClass(results['Net Profit/Loss'])}`}>
                {results['Net Profit/Loss'] > 0 ? '+' : ''}${results['Net Profit/Loss'].toFixed(2)}
              </span>
            </div>
            
            <div className="result-row">
              <span className="result-label">Status:</span>
              <span className={`result-value ${getStatusClass(results['Net Profit/Loss'])}`}>
                {getStatusText(results['Net Profit/Loss'])}
              </span>
            </div>

            <div className="result-row" style={{ marginTop: '0.5rem', paddingTop: '0.5rem', borderTop: '1px dashed rgba(255,255,255,0.1)' }}>
              <span className="result-label">Total Return (%):</span>
              <span className={`result-value ${getStatusClass(results['Net Profit/Loss'])}`}>
                {results['Total Return (%)'].toFixed(2)}%
              </span>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
