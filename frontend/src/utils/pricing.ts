const STORAGE_KEY = "sellingPrices";

type Prices = Record<string, number>;

export function getSellingPrices(): Prices {

    const saved = localStorage.getItem(STORAGE_KEY);

    if (!saved) {
        return {};
    }

    try {
        return JSON.parse(saved);
    } catch {
        return {};
    }

}

export function getSellingPrice(item: string): number {

    const prices = getSellingPrices();

    return prices[item] ?? 0;

}

export function calculateProfit(
    item: string,
    buyPrice: number
): number {

    const sellPrice = getSellingPrice(item);

    return sellPrice - buyPrice;

}

export function calculateROI(
    item: string,
    buyPrice: number
): number {

    const profit = calculateProfit(item, buyPrice);

    if (buyPrice <= 0) {
        return 0;
    }

    return Number(((profit / buyPrice) * 100).toFixed(2));

}

export function calculateBulkProfit(
    item: string,
    buyPrice: number,
    quantity: number
): number {

    return calculateProfit(item, buyPrice) * quantity;

}