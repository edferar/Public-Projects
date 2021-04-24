import React, { useState } from "react";
import { GetPredicao } from "../api/connect";
import { Form, Button, Container, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './formularioAvc.css';


const FormularioAvc = () => {
  const [rangeAge, setAge] = useState(0)
  const [rangeGl, setGl] = useState(0)
  const [rangeImc, setIMC] = useState(0)
  const [gender, setGender] = useState("")
  const [hypertension, setHypertension] = useState("")

  const [heart_disease, setHeartDisease] = useState("")
  const [ever_married, setEverMarried] = useState("")
  const [work_type, setWorkType] = useState("")
  const [Residence_type, setResidenceType] = useState("")
  const [smoking_status, setSmokingStatus] = useState("")

  /* const[json_file, setJsonFile] = useState("")
 
  const setJsonfile = useJson();*/

  const onInputRangeRangeImc = () => {
    var input = document.getElementById("rangeImc").value;
    if ((input !== 0) & (input !== "")) {
      setIMC(input)
    } else {
      setIMC(0)
    }
  }

  const onInputRangeRangeGl = () => {
    var input = document.getElementById("rangeGl").value;
    if ((input !== 0) & (input !== "")) {
      setGl(input)
    } else {
      setGl(0)
    }
  }
  const onInputRangeRangeAge = () => {
    var input = document.getElementById("rangeAge").value;
    if ((input !== 0) & (input !== "")) {
      setAge(input)
    } else {
      setAge(0)
    }
  }

  const onInputTextRangeIMC = () => {
    var input = document.getElementById("inputImc").value;
    if ((input !== 0) & (input !== "")) {
      setIMC(input)
    } else {
      setIMC(rangeImc)
    }
  }
  const onInputTextRangeAge = () => {
    var input = document.getElementById("inputAge").value;
    if ((input !== 0) & (input !== "")) {
      setAge(input)
    } else {
      setAge(rangeAge)
    }
  }
  const onInputTextRangeGl = () => {
    var input = document.getElementById("inputGl").value;
    if ((input !== 0) & (input !== "")) {
      setGl(input)
    } else {
      setGl(rangeGl)
    }
  }

  const setGenderFunc = () => {
    var gender_value = document.querySelector('input[name="gender"]:checked').value;
    setGender(gender_value)

  }

  const setHypertensionFunc = () => {
    var hypertension_value = document.querySelector('input[name="hypertension"]:checked').value;
    setHypertension(hypertension_value)
  }

  const setHeartDiseaseFunc = () => {
    var heart_disease_value = document.querySelector(
      'input[name="heart_disease"]:checked'
    ).value;
    setHeartDisease(heart_disease_value)
  }


  const setEverMarriedFunc = () => {
    var ever_married_value = document.querySelector(
      'input[name="ever_married"]:checked'
    ).value;
    setEverMarried(ever_married_value)
  }

  const setResidenceTypeFunc = () => {
    var Residence_type_value = document.querySelector(
      'input[name="Residence_type"]:checked'
    ).value;
    setResidenceType(Residence_type_value)
  }


  const setWorkTypeFunc = () => {
    var work_type_value = document.getElementById("work_type").value;
    setWorkType(work_type_value);
  }

  const setSmokingStatusFunc = () => {
    var smoking_status_value = document.getElementById("smoking_status").value;
    setSmokingStatus(smoking_status_value);
  }
  /*
  
  
    /*
    get_date() {
      
      setState({ [{getdate]: "2" });
      alert({getdate)
    }
  */
  const get_form_validado = () => {

    var states = new Map()
    states.set("rangeAge", rangeAge);
    states.set("rangeGl", rangeGl);
    states.set("rangeImc", rangeImc);
    states.set("gender", gender);
    states.set("hypertension", hypertension);
    states.set("heart_disease", heart_disease);
    states.set("ever_married", ever_married);
    states.set("work_type", work_type);
    states.set("Residence_type", Residence_type);
    states.set("smoking_status", smoking_status);

    var erros = ''

    for (var [key, value] of states) {
      if (value == "") {
        erros = erros + key + ','
      }/*else{
        values = values + key + ":" + value  + "," 
      }*/

    }


    if (erros !== '') {
      return [0, erros]
    } else {

      return [1, Object.fromEntries(states)]
    }


  }

  const get_data_predicao = (event) => {
    var result = get_form_validado();



    if (result[0] == 0) {
      alert('Os campos ' + result[1] + ' não foram preenchidos corretamente')
    } else {
      GetPredicao(Object.values(result[1]), event)


    }

  }

  return (
    <>
      <Container className="form_container">
        <Form onSubmit={get_data_predicao} id="my_form">
          <Form.Group>
            <Form.Group>
              <Form.Row>
                <Form.Group as={Col} >
                  <Col>
                    <Form.Label>Com qual genero você se identifica?</Form.Label>

                  </Col>
                  <Col>

                    <Form.Check
                      required
                      custom
                      inline
                      label="Masculino"
                      id="male"
                      name="gender"
                      value="0"
                      type="radio"
                      onChange={setGenderFunc}
                    />

                    <Form.Check
                      custom
                      inline
                      label="Feminino"
                      id="female"
                      name="gender"
                      value="1"
                      type="radio"
                      onChange={setGenderFunc}
                    />
                    <Form.Check
                      custom
                      inline
                      label="Outro"
                      id="other"
                      name="gender"
                      value="2"
                      type="radio"
                      onChange={setGenderFunc}
                    />
                  </Col>

                </Form.Group>


                <Form.Group as={Col} >
                  <Col>
                    <Form.Label>Possui hipertensão?</Form.Label>
                  </Col>
                  <Col>
                    <Form.Check
                      required
                      custom
                      inline
                      label="Sim"
                      id="hypertension_yes"
                      name="hypertension"
                      value="1"
                      type="radio"
                      onChange={setHypertensionFunc}
                    />

                    <Form.Check
                      required
                      custom
                      inline
                      label="Não"
                      id="hypertension_no"
                      name="hypertension"
                      value="0"
                      type="radio"
                      onChange={setHypertensionFunc}
                    />
                  </Col>
                </Form.Group>




                <Form.Group as={Col} >
                  <Col>

                    <Form.Label>Possui doença cardíaca?</Form.Label>
                  </Col>
                  <Col>

                    <Form.Check
                      required
                      custom
                      inline
                      label="Sim"
                      id="heart_disease_yes"
                      name="heart_disease"
                      value="1"
                      type="radio"
                      onChange={setHeartDiseaseFunc}
                    />

                    <Form.Check
                      required
                      custom
                      inline
                      label="Não"
                      id="heart_disease_no"
                      name="heart_disease"
                      value="0"
                      type="radio"
                      onChange={setHeartDiseaseFunc}
                    />
                  </Col>

                </Form.Group>
              </Form.Row>
            </Form.Group>

            <Form.Group>
              <Form.Row>
                <Form.Group as={Col} >
                  <Col>

                    <Form.Label>Em que tipo de zona sua residencia se encontra?</Form.Label>
                  </Col>
                  <Col>
                    <Form.Check
                      required
                      custom
                      inline
                      label="Urbana"
                      id="Urbana"
                      name="Residence_type"
                      value="1"
                      type="radio"
                      onChange={setResidenceTypeFunc}
                    />

                    <Form.Check
                      required
                      custom
                      inline
                      label="Rural"
                      id="Rural"
                      name="Residence_type"
                      value="0"
                      type="radio"
                      onChange={setResidenceTypeFunc}
                    />
                  </Col>
                </Form.Group>

                <Form.Group as={Col} >
                  <Col>

                    <Form.Label>Já foi ou é casado?</Form.Label>
                  </Col>
                  <Col>

                    <Form.Check
                      required
                      custom
                      inline
                      label="Sim"
                      id="ever_married_yes"
                      name="ever_married"
                      value="1"
                      type="radio"
                      onChange={setEverMarriedFunc}
                    />

                    <Form.Check
                      required
                      custom
                      inline
                      label="Não"
                      id="ever_married_no"
                      name="ever_married"
                      value="0"
                      type="radio"
                      onChange={setEverMarriedFunc}
                    />
                  </Col>

                </Form.Group>
              </Form.Row>
            </Form.Group>

            <Form.Group>
              <Form.Row>
                <Form.Group as={Col} >
                  <Col>
                    <Form.Label>Selecione o seu tipo de trabalho?</Form.Label>
                  </Col>


                  <Col>
                    <Form.Control as="select"
                      custom
                      require
                      name="work_type"
                      id="work_type"
                      onClick={setWorkTypeFunc} defaultValue={""}>
                      <option value="" ></option>
                      <option value="0">Empresa Privada </option>
                      <option value="1">Autônomo </option>
                      <option value="4">Nunca trabalhou</option>
                      <option value="3">Servidor</option>x
              <option value="2">Criança</option>
                    </Form.Control>
                  </Col>

                </Form.Group>

                <Form.Group as={Col} >
                  <Col>

                    <Form.Label>Vocè é fumante?</Form.Label>
                  </Col>

                  <Col>
                    <Form.Control as="select"
                      custom
                      require
                      name="smoking_status"
                      id="smoking_status"
                      onClick={setSmokingStatusFunc}  defaultValue={""} >
                      <option value=""></option>
                      <option value="0">nunca fumei</option>
                      <option value="1">Desconhecido </option>
                      <option value="2">Parei de fumar </option>
                      <option value="3">Sim</option>
                    </Form.Control>
                  </Col>


                </Form.Group>
              </Form.Row>
            </Form.Group>


            <Form.Group >
              <Form.Row>
                <Form.Group as={Col} >
                  <Col>
                    <Form.Label>Sua idade é?</Form.Label>
                  </Col>
                  <Col>
                    <Form.Control type="range"
                      id="rangeAge"
                      min="0"
                      max="120"
                      value={rangeAge}
                      step="1"
                      onChange={onInputRangeRangeAge} />

                    <Form.Control type="number"
                      required
                      id="inputAge"
                      value={rangeAge}
                      onInput={onInputTextRangeAge}
                      placeholder="0" />
                  </Col>

                </Form.Group>

                <Form.Group as={Col} >
                  <Col>
                    <Form.Label>Informe o seu IMC(Índice de massa corporal)?</Form.Label>
                  </Col>
                  <Col>
                    <Form.Control type="range"
                      id="rangeImc"
                      min="0"
                      max="200"
                      value={rangeImc}
                
                      step="0.11"
                      onChange={onInputRangeRangeImc} />

                    <Form.Control type="number"
                      required
                      id="inputImc"
                      value={rangeImc}
                      onInput={onInputTextRangeIMC}
                      placeholder="0" />
                  </Col>
                </Form.Group>

                <Form.Group as={Col} >
                  <Col>
                    <Form.Label>Informe seu nível médio de glicose?</Form.Label>
                  </Col>
                  <Col>
                    <Form.Control type="range"
                      id="rangeGl"
                      min="0"
                      max="200"
                      value={rangeGl}
                      step="0.11"
                      onChange={onInputRangeRangeGl} />


                    <Form.Control type="number"
                      required
                      id="inputGl"
                      value={rangeGl}
                      onInput={onInputTextRangeGl}
                      placeholder="0" />
                  </Col>
                </Form.Group>


              </Form.Row>
            </Form.Group>
            <Form.Row>


              <Button variant="success" type="submit">Enviar</Button>
              <Button variant="light" type="reset">Limpar</Button>

            </Form.Row>
          </Form.Group>
        </Form>

      </Container>
    </>
  );


}



export { FormularioAvc }