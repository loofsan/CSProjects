import "./Display.css";

// Helper function for currency formatting

const formatToCurrency = (value) => {
  return value.toLocaleString("en-US", {
    style: "currency",
    currency: "USD",
  });
};

const Display = ({ value, errorMsg }) => (
  <div className="display">
    {errorMsg && <div className="error">{errorMsg}</div>}

    {!errorMsg && value != null && (
      <div>Future Value: {formatToCurrency(value)}</div>
    )}
  </div>
);
export default Display;
