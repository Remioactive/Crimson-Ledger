type Signal = {
    impact: string;
    message: string;
};

type Props = {
    signal: Signal;
};

function SignalBadge({ signal }: Props) {
    const badgeClass =
        signal.impact === "positive"
            ? "signal-positive"
            : signal.impact === "negative"
            ? "signal-negative"
            : "signal-neutral";

    return (
        <div className={`signal-badge ${badgeClass}`}>
            {signal.message}
        </div>
    );
}

export default SignalBadge;