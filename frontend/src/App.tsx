import { useState } from "react";

import "./App.css";

import Sidebar from "./components/Sidebar";

import Dashboard from "./pages/Dashboard";
import MyPrices from "./pages/MyPrices";

function App() {

    const [page, setPage] = useState("dashboard");

    return (

        <div className="app">

            <Sidebar
                page={page}
                setPage={setPage}
            />

            <main className="page-content">

                {page === "dashboard" && <Dashboard />}

                {page === "prices" && <MyPrices />}

                {page === "history" && (

                    <section className="card">

                        <h1>📈 History</h1>

                        <p>Coming Soon</p>

                    </section>

                )}

                {page === "settings" && (

                    <section className="card">

                        <h1>⚙️ Settings</h1>

                        <p>Coming Soon</p>

                    </section>

                )}

            </main>

        </div>

    );

}

export default App;