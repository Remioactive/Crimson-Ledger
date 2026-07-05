type Opportunity = {
    key: string;
    item: string;
    buy_score: number;
    recommendation: string;
    current_price?: number;
};

type Props = {
    item: Opportunity;
};

function OpportunityCard({ item }: Props) {
    const scoreColor =
        item.buy_score >= 70
            ? "#22c55e"
            : item.buy_score >= 60
            ? "#eab308"
            : "#ef4444";

    const badgeClass =
        item.recommendation === "Consider Buying"
            ? "badge-good"
            : item.recommendation === "Watch"
            ? "badge-watch"
            : "badge-bad";

    return (
        <div className="opportunity-card">

            <div className="opportunity-header">

                <div className="blood-icon">🩸</div>

                <div>
                    <h3>{item.item.replace("Blood Bag : ", "")}</h3>

                    <span className={badgeClass}>
                        {item.recommendation}
                    </span>
                </div>

            </div>

            <div className="score-section">

                <div className="score-label">

                    <span>Buy Score</span>

                    <strong>{item.buy_score}</strong>

                </div>

                <div className="score-bar">

                    <div
                        className="score-fill"
                        style={{
                            width: `${item.buy_score}%`,
                            background: scoreColor,
                        }}
                    />

                </div>

            </div>

            <div className="price">

                <span>Lowest Price</span>

                <strong>

                    {item.current_price
                        ? `$${item.current_price.toLocaleString()}`
                        : "--"}

                </strong>

            </div>

        </div>
    );
}

export default OpportunityCard;