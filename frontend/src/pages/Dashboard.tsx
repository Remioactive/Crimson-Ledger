import { useEffect, useState } from "react";
import { getDashboard } from "../api/dashboard";

type DashboardData = {
    last_scan: string;
    items: number;
    top_buys: {
        key: string;
        item: string;
        buy_score: number;
        recommendation: string;
    }[];
};

function Dashboard() {

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [dashboard, setDashboard] = useState<DashboardData | null>(null);

    useEffect(() => {

        async function loadDashboard() {

            try {

                const data = await getDashboard();
                setDashboard(data);

            } catch (err) {

                console.error(err);
                setError("Unable to connect to backend.");

            } finally {

                setLoading(false);

            }

        }

        loadDashboard();

    }, []);

    return (

        <div className="dashboard">

            <header className="hero">
                <h1>🩸 Crimson Ledger</h1>
                <p>Market Intelligence for Torn</p>
            </header>

            <section className="card">

                <h2>System Status</h2>

                {loading && <p>Connecting...</p>}

                {!loading && error && (
                    <p style={{ color: "#ff6666" }}>{error}</p>
                )}

                {!loading && dashboard && (
                    <>
                        <div className="status">
                            <span className="dot" style={{ background: "limegreen" }}></span>
                            <span>Backend Online</span>
                        </div>

                        <p>
                            <strong>Last Scan:</strong> {dashboard.last_scan}
                        </p>

                        <p>
                            <strong>Items Tracked:</strong> {dashboard.items}
                        </p>
                    </>
                )}

            </section>

            {dashboard && (

                <section className="card">

                    <h2>Top Buy Opportunities</h2>

                    {dashboard.top_buys.map((item) => (

                        <div key={item.key} style={{ marginBottom: "20px" }}>

                            <strong>{item.item}</strong>

                            <br />

                            Buy Score: {item.buy_score}

                            <br />

                            Recommendation: {item.recommendation}

                        </div>

                    ))}

                </section>

            )}

        </div>

    );

}

export default Dashboard;