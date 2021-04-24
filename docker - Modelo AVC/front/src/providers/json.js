import React, { useEffect, useState } from "react";

export const JsonContext = React.createContext({});

export const JsonProvider = (props) => {
  const [string, setString] = useState({
    data: "",
    status : false
  });

  useEffect(() => {
    const stringStorage = localStorage.getItem("string");
    if (stringStorage) {
      setString(JSON.parse(stringStorage));
    } else {
      setString({
        data: "",
        status : false
      });
    }
  }, []);

  return (
    <JsonContext.Provider value={{ string, setString }}>
      {props.children}
    </JsonContext.Provider>
  );
};

export const useJson = () => React.useContext(JsonContext);
