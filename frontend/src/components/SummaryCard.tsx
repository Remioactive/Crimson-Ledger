type SummaryCardProps = {
    icon: string;
    title: string;
    value: string | number;
};

function SummaryCard({ icon, title, value }: SummaryCardProps) {
    return (
        <div className="summary-card">
            <div className="summary-icon">{icon}</div>

            <div className="summary-content">
                <div className="summary-title">{title}</div>
                <div className="summary-value">{value}</div>
            </div>
        </div>
    );
}

export default SummaryCard;