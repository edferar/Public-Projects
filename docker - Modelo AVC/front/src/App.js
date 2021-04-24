
import React from 'react';
import { FormularioAvc } from "./components/formularioAvc";
import ScoreIndicador from "./components/indicador";
import { useJson } from "./providers/json"
import NavBar from './components/navBar';
import Cabecalho from './components/cabecalho';
import Footer from './components/footer';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  const { string } = useJson();


  console.log(string);


  return (
    <div>
      <NavBar String="Deploy de modelo com React (Risco AVC)" />
      <Cabecalho />
      <ScoreIndicador value={string.data} />
      <FormularioAvc />


      <Footer />










    </div>
  );



}



export default App;
