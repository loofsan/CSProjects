import { useState } from "react";
import "./CalculatorForm.css";

const CalculatorForm = ({ onSubmit }) => {
  // state variables for input fields
  const [amount, setAmount] = useState("");
  const [years, setYears] = useState("");
  const [rate, setRate] = useState("");

  // event handler for form submission
  const handleSubmit = (e) => {
    // prevent default form submission
    e.preventDefault();

    // convert input values from strings to numbers
    const numAmount = Number(amount);
    const numYears = Number(years);
    const numRate = Number(rate);
    // call the function sent from the parent
    onSubmit(numAmount, numYears, numRate);
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="amount">Monthly amount</label>
          <input
            type="number"
            id="amount"
            name="amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
            autoFocus
          />
        </div>

        <div>
          <label htmlFor="years">Number of years</label>
          <input
            type="number"
            id="years"
            name="years"
            value={years}
            onChange={(e) => setYears(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="rate">Interest rate</label>
          <input
            type="number"
            id="rate"
            name="rate"
            value={rate}
            onChange={(e) => setRate(e.target.value)}
            required
          />
        </div>

        <div>
          <button type="submit">Calculate</button>
        </div>
      </form>
    </>
  );
};

export default CalculatorForm;
