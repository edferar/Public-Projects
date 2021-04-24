import React from 'react'
import { Jumbotron } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';





const Cabecalho = ({value}) => {

    return(

<>
<Jumbotron>
  <h1>Olá!</h1>
  <p>
    O formulário abaixo foi desenvolvido com fim didático, 
    visando demonstrar o deploy de um modelo de machine learning 
    utilizando docker dentre outras tecnologias, tais como o próprio react.

    Faça sua simulação e divirta-se!
  </p>

</Jumbotron>
</>
)}

export default Cabecalho;