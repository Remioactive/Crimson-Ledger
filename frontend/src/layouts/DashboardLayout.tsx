import React from "react";

type DashboardLayoutProps = {
    summary: React.ReactNode;
    market: React.ReactNode;
    opportunities: React.ReactNode;
};

function DashboardLayout({
    summary,
    market,
    opportunities,
}: DashboardLayoutProps) {
    return (
        <main className="dashboard-layout">

            {summary}

            <div className="dashboard-content">

                <section className="dashboard-panel dashboard-market">

                    {market}

                </section>

                <aside className="dashboard-panel dashboard-opportunities">

                    {opportunities}

                </aside>

            </div>

        </main>
    );
}

export default DashboardLayout;