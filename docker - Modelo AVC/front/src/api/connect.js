import axios from "axios";

const GetPredicao = (json, event) => {

  event.preventDefault()
  axios.post(
    'http://127.0.0.1:5000/get_predicao_modelo',
    {
      age: json[0],
      avg_glucose_level: json[1],
      bmi: json[2],
      gender: json[3],
      hypertension: json[4],
      heart_disease: json[5],
      ever_married: json[6],
      work_type: json[7],
      Residence_type: json[8],
      smoking_status: json[9],
    }
  ).then(response => {
    localStorage.setItem("string", JSON.stringify({ data: response.data.return_pred , status : true}));
    console.log(response.data)
    window.location.href = 'App.js'


  }).catch(error => {
    console.log(error)
    alert('Falha ao gerar score')
  })

}

export { GetPredicao };

