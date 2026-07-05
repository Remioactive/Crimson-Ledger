import { useEffect, useState } from "react";

import { getDashboard } from "../api/dashboard";

import SummaryCard from "../components/SummaryCard";
import MarketTable from "../components/MarketTable";
import OpportunityCard from "../components/OpportunityCard";
import DashboardLayout from "../layouts/DashboardLayout";

type TopBuy = {
    key: string;
    item: string;
    buy_score: number;
    recommendation: string;
    current_price?: number;
};

type MarketItem = {
    key: string;
    name: string;
    lowest_price: number;
    buy500_average: number;
    listing_count: number;
};

type DashboardData = {
    last_scan: string;
    items: number;
    market: MarketItem[];
    top_buys: TopBuy[];
};

function Dashboard() {
    const [dashboard, setDashboard] = useState<DashboardData | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

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

    if (loading) {
        return (
            <div className="dashboard">
                <h1>🩸 Crimson Ledger</h1>
                <p>Loading...</p>
            </div>
        );
    }

    if (error || !dashboard) {
        return (
            <div className="dashboard">
                <h1>🩸 Crimson Ledger</h1>
                <p>{error || "Dashboard unavailable."}</p>
            </div>
        );
    }

    const summary = (
        <section className="summary-grid">

            <SummaryCard
                icon="🟢"
                title="Backend"
                value="Online"
            />

            <SummaryCard
                icon="📦"
                title="Items"
                value={dashboard.items}
            />

            <SummaryCard
                icon="🕒"
                title="Last Scan"
                value={dashboard.last_scan.split(" ")[1]}
            />

            <SummaryCard
                icon="🩸"
                title="Best Buy"
                value={dashboard.top_buys[0]?.item.replace("Blood Bag : ", "")}
            />

        </section>
    );

    const market = (
        <MarketTable market={dashboard.market} />
    );

    const opportunities = (
        <section className="card">

            <h2>Top Buy Opportunities</h2>

            <div className="opportunity-grid">

                {dashboard.top_buys.map((item) => (

                    <OpportunityCard
                        key={item.key}
                        item={item}
                    />

                ))}

            </div>

        </section>
    );

    return (
        <div className="dashboard">

            <header className="hero">
                <h1>🩸 Crimson Ledger</h1>
                <p>Market Intelligence for Torn</p>
            </header>

            <DashboardLayout
                summary={summary}
                market={market}
                opportunities={opportunities}
            />

        </div>
    );
}

export default Dashboard;