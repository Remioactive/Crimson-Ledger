type Props = {
    label: string;
    value: string | number;
};

function StatRow({ label, value }: Props) {
    return (
        <div className="stat-row">

            <span className="stat-label">
                {label}
            </span>

            <span className="stat-value">
                {value}
            </span>

        </div>
    );
}

export default StatRow;