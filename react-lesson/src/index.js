import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import App from './App';
import reportWebVitals from './reportWebVitals';
// import Activity3 from './Lesson/Activity3';
import Activity1 from './Lesson/Activity1';
import Activity2 from './Lesson/Activity2';
import Activity1Lesson2 from './LessonComponent/Activity1';
import Activity2Lesson2 from './LessonComponent/Activity2';
import Lesson3A1 from './LessonProps/Activity1';
import Lesson3A2 from './LessonProps/Activity2';
import Lesson3A3 from './LessonProps/Activity3';
import Lesson3A4 from './LessonProps/Activity4';
import Lesson4A1 from './LessonState/Activity1';
import Lesson4A2 from './LessonState/Activity2';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Lesson4A2/>
    {/* <Activity2Lesson2/> */}
    {/* <Activity3/> */}
    {/* <Activity1/> */}
    {/* <Activity2/> */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
