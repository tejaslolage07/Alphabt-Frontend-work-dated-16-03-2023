import React, { useState } from 'react'
import NavbarComponent from './NavbarComponent'
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import axios from "axios";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const Dashboard = () => {

  const [taskData, setTaskData] = React.useState([]);

  function getData() {
    var formdata = new FormData();
    // formdata.append("startD", startDate / 1000)
    // formdata.append("endD", endDate / 1000)
    console.log(startDate + ' to ' + endDate)
    let startD = new Date(startDate);
    let endD = new Date(endDate);
    formdata.append("startD", startD.toISOString())
    formdata.append("endD", endD.toISOString())
    console.log("toISOString endD:", endD.toISOString())

    // axios.post('http://127.0.0.1:5000/excel', { "startD": "2023-03-15", "endD": "2023-03-16" },
    //   {
    //     headers: {
    //       'Access-Control-Allow-Origin': '*',
    //       'Content-Type': 'application/json',
    //     }
    //   })
    //   .then((response) => {
    //     setTaskData(response.data);
    //     console.log(response.data)
    //   });

    // This works:-
    axios({
      method: 'POST',
      url: 'http://127.0.0.1:5000/excel',
      data: formdata,
      headers: {
        'Access-Control-Allow-Origin': '*',
        "Content-Type": "multipart/form-data"
      }
    });

    // fetch("http://127.0.0.1:5000/excel", {
    //   method: "POST",
    //   body: formdata,
    //   headers: {
    //     "Content-Type": "multipart/form-data",
    //     'Access-Control-Allow-Origin': "*",
    //   }
    // });
  }

  const [startDate, setStartDate] = useState(new Date().getTime());
  const [endDate, setEndDate] = useState(new Date().getTime());

  function OnClick() {
    console.log(startDate)
    console.log(endDate)
  }

  return (
    <div className='dash'>
      <NavbarComponent />
      <div className='color-box dashboard'></div>
      <div className="select-container">
        <div className='give-margin'>
          <p>From</p>
          <DatePicker
            wrapperClassName="datePicker"
            selected={startDate}
            onChange={(date) => setStartDate(date.getTime())}
            selectsStart
            startDate={startDate}
            endDate={endDate}
            timeInputLabel="Time:"
            dateFormat="dd/MM/yyyy h:mm aa"
            showTimeInput
          />
        </div>
        <div className='give-margin'>
          <p>To</p>
          <DatePicker
            selected={endDate}
            onChange={(date) => setEndDate(date.getTime())}
            selectsEnd
            startDate={startDate}
            endDate={endDate}
            minDate={startDate}
            timeInputLabel="Time:"
            dateFormat="dd/MM/yyyy h:mm aa"
            showTimeInput
          />
        </div>
        <button onClick={getData} type="submit" className='button'>Get Results</button>
      </div>
    </div>
  )
}

export default Dashboard