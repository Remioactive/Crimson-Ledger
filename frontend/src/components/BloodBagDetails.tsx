import StatRow from "./StatRow";
import SignalBadge from "./SignalBadge";

import {
    calculateBulkProfit,
    calculateProfit,
    calculateROI,
    getSellingPrice,
} from "../utils/pricing";

const ITEM_IDS: Record<string, number> = {
    "Blood Bag : A+": 732,
    "Blood Bag : A-": 733,
    "Blood Bag : B+": 734,
    "Blood Bag : B-": 735,
    "Blood Bag : AB+": 736,
    "Blood Bag : AB-": 737,
    "Blood Bag : O+": 738,
    "Blood Bag : O-": 739,
    "Blood Bag : Irradiated": 1012,
};

type Signal = {
    impact: string;
    message: string;
};

type BloodBag = {
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

type Props = {
    bag: BloodBag | null;
};

function BloodBagDetails({ bag }: Props) {

    if (!bag) {
        return (
            <section className="card">
                <h2>Blood Bag Details</h2>
                <p>Select a blood bag.</p>
            </section>
        );
    }

    function openTornMarket() {

        const itemID = ITEM_IDS[bag.item];

        if (!itemID) {
            alert("Unknown Item ID");
            return;
        }

        window.open(
            `https://www.torn.com/page.php?sid=ItemMarket#/market/view=search&itemID=${itemID}`,
            "_blank"
        );
    }

    const scoreColor =
        bag.buy_score >= 80
            ? "#22c55e"
            : bag.buy_score >= 60
            ? "#eab308"
            : "#ef4444";

    const sellPrice = getSellingPrice(bag.item);

    const profit = calculateProfit(
        bag.item,
        bag.current_price
    );

    const roi = calculateROI(
        bag.item,
        bag.current_price
    );

    return (
        <section className="card">

            <h2>{bag.item}</h2>

            <div className="detail-score">
                <span>Trading Score</span>
                <strong>{bag.buy_score}/100</strong>
            </div>

            <div className="score-bar">
                <div
                    className="score-fill"
                    style={{
                        width: `${bag.buy_score}%`,
                        background: scoreColor,
                    }}
                />
            </div>

            <StatRow
                label="Recommendation"
                value={bag.recommendation}
            />

            <StatRow
                label="Lowest Price"
                value={`$${bag.current_price.toLocaleString()}`}
            />

            <StatRow
                label="Your Sell Price"
                value={
                    sellPrice
                        ? `$${sellPrice.toLocaleString()}`
                        : "Not Set"
                }
            />

            <StatRow
                label="Profit / Bag"
                value={`$${profit.toLocaleString()}`}
            />

            <StatRow
                label="ROI"
                value={`${roi}%`}
            />

            <StatRow
                label="Profit (100)"
                value={`$${calculateBulkProfit(
                    bag.item,
                    bag.current_price,
                    100
                ).toLocaleString()}`}
            />

            <StatRow
                label="Profit (500)"
                value={`$${calculateBulkProfit(
                    bag.item,
                    bag.current_price,
                    500
                ).toLocaleString()}`}
            />

            <StatRow
                label="Profit (1000)"
                value={`$${calculateBulkProfit(
                    bag.item,
                    bag.current_price,
                    1000
                ).toLocaleString()}`}
            />

            <StatRow
                label="Historical Avg"
                value={`$${Math.round(
                    bag.historical_average_price
                ).toLocaleString()}`}
            />

            <StatRow
                label="Price vs History"
                value={`${bag.price_difference_from_history}%`}
            />

            <StatRow
                label="Current Supply"
                value={bag.current_supply.toLocaleString()}
            />

            <StatRow
                label="Historical Supply"
                value={Math.round(
                    bag.historical_average_supply
                ).toLocaleString()}
            />

            <StatRow
                label="Supply vs History"
                value={`${bag.supply_difference_from_history}%`}
            />

            <StatRow
                label="Listings"
                value={bag.listing_count}
            />

            <StatRow
                label="Market Health"
                value={bag.market_health}
            />

            <StatRow
                label="Volatility"
                value={`${bag.volatility}%`}
            />

            <h3 style={{ marginTop: 24 }}>
                Market Signals
            </h3>

            {bag.signals.map((signal, index) => (
                <SignalBadge
                    key={index}
                    signal={signal}
                />
            ))}

            <button
                className="buy-button"
                onClick={openTornMarket}
            >
                🛒 Buy In Torn
            </button>

        </section>
    );
}

export default BloodBagDetails;