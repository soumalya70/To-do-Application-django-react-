import tick from '../assets/tick.png';
import not_tick from '../assets/not_tick.png';
import cross from '../assets/cross.png';

const Component2 = ({no, setTodos, activity_name, hour, min, display}) => {

    const deleteTodo = (no) => {
        let data = JSON.parse(localStorage.getItem("todos"));
        data = data.filter((todo) => todo.no !== no);
        setTodos(data);
    }

    const toggle = (no) => {
        let data = JSON.parse(localStorage.getItem("todos"));
        for(let i=0;i<data.length;++i){
            if (data[i].no === no){
                if (data[i].display === ""){
                    data[i].display = "line-through";
                }
                else {
                    data[i].display = "";
                }
                break;
            }
        }
        setTodos(data);
    }
  return (
    <div className='todoitems'>
      <div className={`todoitems-container ${display}`} onClick={()=>{toggle(no)}}>
        {display===""?<img src={not_tick} alt="" />:<img src={tick} alt="" />}
        <div className="todoitems-text">
            <div className="todoitems-text_activity_name">{activity_name}</div>
            <div className="todoitems-text_time">{hour}:{min}</div>
        </div>
      </div>
      <img className='todoitems-cross-icon' onClick={() => {deleteTodo(no)}} src={cross} alt="" />
    </div>
  )
}

export default Component2;