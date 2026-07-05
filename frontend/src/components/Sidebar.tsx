type Props = {
    page: string;
    setPage: (page: string) => void;
};

function Sidebar({ page, setPage }: Props) {

    const pages = [
        { id: "dashboard", label: "📊 Dashboard" },
        { id: "prices", label: "💰 My Prices" },
        { id: "history", label: "📈 History" },
        { id: "settings", label: "⚙️ Settings" },
    ];

    return (
        <aside className="sidebar">

            <h2>🩸 Crimson Ledger</h2>

            {pages.map((p) => (

                <button
                    key={p.id}
                    className={
                        page === p.id
                            ? "sidebar-button active"
                            : "sidebar-button"
                    }
                    onClick={() => setPage(p.id)}
                >
                    {p.label}
                </button>

            ))}

        </aside>
    );
}

export default Sidebar;