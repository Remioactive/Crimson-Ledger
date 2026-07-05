type MarketItem = {
    key: string;
    name: string;
    lowest_price: number;
    buy500_average: number;
    listing_count: number;
};

type Props = {
    market: MarketItem[];
};

function MarketTable({ market }: Props) {
    return (
        <section className="card">

            <div className="table-header">
                <h2>Market Overview</h2>
                <span>{market.length} Blood Types</span>
            </div>

            <table className="market-table">

                <thead>
                    <tr>
                        <th>Blood Type</th>
                        <th>Lowest Price</th>
                        <th>Buy 500 Avg</th>
                        <th>Listings</th>
                    </tr>
                </thead>

                <tbody>

                    {market.map((item) => (

                        <tr key={item.key}>

                            <td>
                                🩸 {item.name.replace("Blood Bag : ", "")}
                            </td>

                            <td>
                                ${item.lowest_price.toLocaleString()}
                            </td>

                            <td>
                                ${Math.round(item.buy500_average).toLocaleString()}
                            </td>

                            <td>
                                {item.listing_count}
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </section>
    );
}

export default MarketTable;