function ResultDisplay({ result }) {
  if (!result) return null;

  const isCancer = result.label === "Cancer";

  return (
    <div>
      <h3>
        Result:
        <span style={{ color: isCancer ? "red" : "green" }}>
          {" "}
          {result.label}
        </span>
      </h3>

      <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>

      {result.heatmap && (
        <img
          src={`data:image/jpeg;base64,${result.heatmap}`}
          alt="heatmap"
          width="300"
        />
      )}
    </div>
  );
}

export default ResultDisplay;
