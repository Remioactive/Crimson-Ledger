import { useEffect, useState } from "react";

const BLOOD_BAGS = [
    "Blood Bag : O+",
    "Blood Bag : O-",
    "Blood Bag : A+",
    "Blood Bag : A-",
    "Blood Bag : B+",
    "Blood Bag : B-",
    "Blood Bag : AB+",
    "Blood Bag : AB-",
    "Blood Bag : Irradiated",
];

function MyPrices() {

    const [prices, setPrices] = useState<Record<string, number>>({});

    useEffect(() => {

        const saved = localStorage.getItem("sellingPrices");

        if (saved) {
            setPrices(JSON.parse(saved));
        }

    }, []);

    function updatePrice(item: string, value: string) {

        setPrices(prev => ({
            ...prev,
            [item]: Number(value)
        }));

    }

    function savePrices() {

        localStorage.setItem(
            "sellingPrices",
            JSON.stringify(prices)
        );

        alert("Selling prices saved!");

    }

    return (

        <section className="card">

            <h1>💰 My Selling Prices</h1>

            <p>
                These prices are used to calculate your expected profit.
            </p>

            <br />

            {BLOOD_BAGS.map(item => (

                <div
                    key={item}
                    className="price-row"
                >

                    <span>

                        {item.replace("Blood Bag : ", "")}

                    </span>

                    <input
                        type="number"
                        value={prices[item] ?? ""}
                        onChange={(e) =>
                            updatePrice(item, e.target.value)
                        }
                        className="price-input"
                    />

                </div>

            ))}

            <br />

            <button
                className="buy-button"
                onClick={savePrices}
            >
                Save Prices
            </button>

        </section>

    );

}

export default MyPrices;