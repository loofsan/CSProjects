import { useState } from "react";
import "./App.css";
import Header from "./components/Header";
import Display from "./components/Display";
import CalculatorForm from "./components/CalculatorForm";

function App() {
  const [futureValue, setFutureValue] = useState(null);
  const [errorMsg, setErrorMsg] = useState("");

  const calculateFutureValue = (amount, years, rate) => {
    if (amount <= 0 || years <= 0 || rate <= 0) {
      setErrorMsg("All values must be greater than zero");
      setFutureValue(null);
      return;
    }

    setErrorMsg("");

    const monthlyRate = rate / 100 / 12;
    const totalMonths = years * 12;

    const fv =
      amount * ((Math.pow(1 + monthlyRate, totalMonths) - 1) / monthlyRate);

    setFutureValue(fv);
  };

  return (
    <>
      <Header />
      <CalculatorForm onSubmit={calculateFutureValue} />
      <Display value={futureValue} errorMsg={errorMsg} />
    </>
  );
}

export default App;
