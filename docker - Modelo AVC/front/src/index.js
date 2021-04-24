import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { JsonProvider } from "./providers/json";
import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    <JsonProvider>
      <App />
    </JsonProvider>
  </React.StrictMode>,
  document.getElementById("root")
);
/*
import reportWebVitals from "./reportWebVitals";
reportWebVitals();
*/