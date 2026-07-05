import {
    calculateProfit,
    calculateROI,
} from "../utils/pricing";

type MarketItem = {
    key: string;
    name: string;
    lowest_price: number;
    buy500_average: number;
    listing_count: number;
};

type Props = {
    market: MarketItem[];
    selected: string;
    onSelect: (key: string) => void;
};

function MarketTable({
    market,
    selected,
    onSelect,
}: Props) {

    return (

        <section className="card">

            <div className="table-header">

                <h2>Market Overview</h2>

                <span>{market.length} Blood Types</span>

            </div>

            <table className="market-table">

                <thead>

                    <tr>

                        <th>Blood</th>
                        <th>Lowest</th>
                        <th>Profit</th>
                        <th>ROI</th>
                        <th>Listings</th>

                    </tr>

                </thead>

                <tbody>

                    {market.map((item) => {

                        const itemName =
                            item.name;

                        const profit =
                            calculateProfit(
                                itemName,
                                item.lowest_price
                            );

                        const roi =
                            calculateROI(
                                itemName,
                                item.lowest_price
                            );

                        return (

                            <tr
                                key={item.key}
                                className={
                                    selected === item.key
                                        ? "selected-row"
                                        : ""
                                }
                                onClick={() =>
                                    onSelect(item.key)
                                }
                                style={{
                                    cursor: "pointer"
                                }}
                            >

                                <td>

                                    🩸{" "}

                                    {item.name.replace(
                                        "Blood Bag : ",
                                        ""
                                    )}

                                </td>

                                <td>

                                    ${item.lowest_price.toLocaleString()}

                                </td>

                                <td
                                    style={{
                                        color:
                                            profit >= 0
                                                ? "#22c55e"
                                                : "#ef4444",
                                        fontWeight: "bold",
                                    }}
                                >

                                    ${profit.toLocaleString()}

                                </td>

                                <td>

                                    {roi.toFixed(1)}%

                                </td>

                                <td>

                                    {item.listing_count}

                                </td>

                            </tr>

                        );

                    })}

                </tbody>

            </table>

        </section>

    );

}

export default MarketTable;