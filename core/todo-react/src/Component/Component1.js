import Component2 from './Component2';
import { useState, useEffect, useRef } from 'react';

let count = 0;
export default function Component1() {
    const[todos, setTodos] = useState([]);
    const inputTextRef = useRef(null);
    const inputHrRef = useRef(null);
    const inputMinRef = useRef(null);

    function handleAddBtn() {
        var obj = document.querySelector('.todo-add');
        obj.classList.add("pressed");
        setTimeout(() => {
            obj.classList.remove("pressed");
        }, 100);

        setTodos([...todos, {no:count++, activity_name:inputTextRef.current.value, hour: inputHrRef.current.value, min: inputMinRef.current.value, display: ""}]);
        inputTextRef.current.value = "";
        inputHrRef.current.value = "";
        inputMinRef.current.value = "";
        localStorage.setItem("todo_count", count);
    };

    function handleInputChecker(obj) {
        let inputValue = obj.target.value;
        inputValue = inputValue.replace(/[^0-9]/g, '');
        obj.target.value = inputValue;
    }

    useEffect(() => {
        setTimeout(() => {
            console.log(todos);
            localStorage.setItem("todos",JSON.stringify(todos));
        }, 100)
    }, [todos]);

    useEffect(()=>{
        setTodos(JSON.parse(localStorage.getItem("todos")));
        count = localStorage.getItem("todos_count");
    },[]);

    return(
        <div className="container1">
            <h1 className="todo-heading">To-Do List</h1>
            <div className="todo-action">
                <div className="todo-input">
                    <input ref={inputTextRef} type="text" placeholder="Add Your Task" className="task-input" />
                    <div className="task-time">
                        <input ref={inputHrRef} maxLength="2" onInput={handleInputChecker} type="text" placeholder="hr" className="task-time-hr" />
                        <input ref={inputMinRef} maxLength="2" onInput={handleInputChecker} type="text" placeholder="min" className="task-time-min" />
                    </div>
                </div>
                <div className="todo-add" onClick={handleAddBtn}>ADD</div>
            </div>
            <div className="todo-list">
                {todos.map((item, index)=>{
                    return <Component2 key={index} no={item.no} setTodos={setTodos} activity_name={item.activity_name} hour={item.hour} min={item.min} display={item.display}/>
                })}
            </div>
        </div>
    );
}