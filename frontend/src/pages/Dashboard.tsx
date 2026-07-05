import { useEffect, useMemo, useState } from "react";

import { getDashboard } from "../api/dashboard";

import SummaryCard from "../components/SummaryCard";
import MarketTable from "../components/MarketTable";
import BloodBagDetails from "../components/BloodBagDetails";
import OpportunityCenter from "../components/OpportunityCenter";
import DashboardLayout from "../layouts/DashboardLayout";

type Signal = {
    impact: string;
    message: string;
};

type Analytics = {
    key: string;
    item: string;

    buy_score: number;
    rating: string;
    recommendation: string;

    current_price: number;

    buy100_average: number;
    buy500_average: number;
    buy1000_average: number;

    current_supply: number;
    listing_count: number;

    market_health: string;
    volatility: number;

    historical_average_price: number;
    historical_average_supply: number;

    price_difference_from_history: number;
    supply_difference_from_history: number;

    signals: Signal[];
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

    analytics: Analytics[];
};

function Dashboard() {

    const [dashboard, setDashboard] = useState<DashboardData | null>(null);
    const [selected, setSelected] = useState("");

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {

        async function loadDashboard() {

            try {

                const data = await getDashboard();

                setDashboard(data);

                if (data.analytics.length > 0) {
                    setSelected(data.analytics[0].key);
                }

            } catch (err) {

                console.error(err);

                setError("Unable to connect to backend.");

            } finally {

                setLoading(false);

            }

        }

        loadDashboard();

    }, []);

    const selectedBag = useMemo(() => {

        if (!dashboard) return null;

        return (
            dashboard.analytics.find(
                bag => bag.key === selected
            ) ?? null
        );

    }, [dashboard, selected]);

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
                <p>{error}</p>
            </div>
        );

    }

    return (

        <div className="dashboard">

            <header className="hero">

                <h1>🩸 Crimson Ledger</h1>

                <p>Market Intelligence for Torn</p>

            </header>

            <OpportunityCenter
                analytics={dashboard.analytics}
            />

            <DashboardLayout

                summary={

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
                            value={
                                dashboard.last_scan
                                    ? dashboard.last_scan.split(" ")[1]
                                    : "--:--:--"
                            }
                        />

                        <SummaryCard
                            icon="🩸"
                            title="Selected"
                            value={
                                selectedBag
                                    ? selectedBag.item.replace("Blood Bag : ", "")
                                    : "-"
                            }
                        />

                    </section>

                }

                market={

                    <MarketTable
                        market={dashboard.market}
                        selected={selected}
                        onSelect={setSelected}
                    />

                }

                opportunities={

                    <BloodBagDetails
                        bag={selectedBag}
                    />

                }

            />

        </div>

    );

}

export default Dashboard;