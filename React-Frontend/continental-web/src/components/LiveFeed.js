import React, {useState, useEffect} from 'react'
import Vid from '../videos/video.mp4'
import Table from 'react-bootstrap/Table';
import Badge from 'react-bootstrap/Badge';
import axios from "axios";


const LiveFeed = () => {

  const [tableData, setTableData] = useState([])

  useEffect(() => {
    let interval = setInterval(() => {
      axios.post('http://localhost:5000/get_data',{"a":10},
      {
        headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
      }})
      .then((response) => {
        setTableData(response.data.cycles);
        console.log(response.data)
      });
    }, 5000);
    return () => {
      clearInterval(interval);
    };
  }, []);


  return (
    <div>
      <div className='color-box live-feed'></div>
      { tableData.map((data, key) => {
        return(
          <div key={key} className='feed-contain'>
            <video width="45%" controls style={{margin: 10}}>
              <source src={Vid} type="video/mp4"/>
            </video>
            
            <Table hover size="sm" className='table'>
              <thead>
                <tr>
                  <th>S. No.</th>
                  <th>Task</th>
                  <th>Time(sec)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>Light Guide</td>
                  <td>{data.tasks.tasks[0].time_taken}</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Diffuser</td>
                  <td>{data.tasks.tasks[1].time_taken}</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Adhesive Tape Check</td>
                  <td>{data.tasks.tasks[2].time_taken}</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>LCD</td>
                  <td>{data.tasks.tasks[3].time_taken}</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Metal Stacker</td>
                  <td>{data.tasks.tasks[4].time_taken}</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>Grown Check</td>
                  <td>{data.tasks.tasks[5].time_taken}</td>
                </tr>
              </tbody>
            </Table>
          </div>
        );
      }) }
    </div>
  )
}

export default LiveFeed