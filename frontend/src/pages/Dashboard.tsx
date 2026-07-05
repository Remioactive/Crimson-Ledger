function Dashboard() {
  return (
    <div className="dashboard">
      <header className="hero">
        <h1>🩸 Crimson Ledger</h1>
        <p>Market Intelligence for Torn</p>
      </header>

      <section className="card">
        <h2>Backend Status</h2>

        <div className="status">
          <span className="dot"></span>
          <span>Ready to Connect</span>
        </div>

        <p className="subtitle">
          FastAPI backend will be connected in Feature 2.
        </p>
      </section>

      <section className="card">
        <h2>Coming Soon</h2>

        <ul>
          <li>📊 Market Overview</li>
          <li>🩸 Top Buy Opportunities</li>
          <li>📈 Price Charts</li>
          <li>📦 Bulk Analysis</li>
          <li>⚡ Live Refresh</li>
        </ul>
      </section>
    </div>
  );
}

export default Dashboard;