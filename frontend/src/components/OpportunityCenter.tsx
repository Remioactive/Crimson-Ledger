import { calculateProfit } from "../utils/pricing";

type Analytics = {
    item: string;
    current_price: number;
    buy_score: number;
};

type Props = {
    analytics: Analytics[];
};

function OpportunityCenter({ analytics }: Props) {

    if (analytics.length === 0) {
        return null;
    }

    const ranked = [...analytics].sort((a, b) => {

        const profitA = calculateProfit(
            a.item,
            a.current_price
        );

        const profitB = calculateProfit(
            b.item,
            b.current_price
        );

        return (
            (profitB + b.buy_score * 100)
            -
            (profitA + a.buy_score * 100)
        );

    });

    const best = ranked[0];

    const profit = calculateProfit(
        best.item,
        best.current_price
    );

    return (

        <section className="card">

            <h2>🔥 Best Opportunity</h2>

            <h1>
                {best.item.replace("Blood Bag : ", "")}
            </h1>

            <p>

                Buy Score: <strong>{best.buy_score}</strong>

            </p>

            <p>

                Expected Profit: <strong>${profit.toLocaleString()}</strong>

            </p>

        </section>

    );

}

export default OpportunityCenter;