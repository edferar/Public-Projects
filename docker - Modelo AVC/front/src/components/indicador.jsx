import React from 'react'
import ReactStoreIndicator from 'react-score-indicator'
import { Modal, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useJson } from "../providers/json";




const ScoreIndicador = ({value}) => {
  const { string } = useJson()
 // const { setJson } = useJson;
/*
  const { string } = useJson()
  const [show, setShow] = useState(string.status)
  console.log(string.status)*/

  const handleClose = () => {
    localStorage.setItem("string", JSON.stringify({ data: "", status : false}));
    window.location.href = 'App.js';
  }


  return (
    <div>
      <>
        <Modal size="sm" show={string.status} onHide={handleClose} animation={false}>
          <Modal.Body>
          <ReactStoreIndicator
        value={value}
        maxValue={100}
        stepsColors={[
          '#3da940',
          '#3da940',
          '#3da940',
          '#53b83a',
          '#84c42b',
          '#f1bc00',
          '#ed8d00',
          '#d12000',]}
      />

          </Modal.Body>
          <Modal.Footer>
            <Button variant="success" onClick={handleClose}>
              Nova Predição
          </Button>
          </Modal.Footer>
        </Modal>





      </>
    </div>
  )
}



export default ScoreIndicador;