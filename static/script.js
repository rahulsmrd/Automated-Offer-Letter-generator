function preview() {
    var name = document.getElementById('name');
    var course=document.getElementById('course');
    var start_date=document.getElementById('start_date');
    var end_date=document.getElementById('end_date');
    console.log(name,course,start_date,end_date,'2222');
    if (name.value!='') {
        document.getElementById('preview_name').innerHTML = name.value;
    }
    if (course.value!='') {
        document.getElementById('preview_course').innerHTML = course.value;
    }
    if (start_date.value!='') {
        document.getElementById('preview_start_date').innerHTML = dateFormating(start_date.value);
    }
    if (end_date.value!='') {
        document.getElementById('preview_end_date').innerHTML = dateFormating(end_date.value);
    }
}
function dateFormating(date){
    var array=date.split('-');
    if (array[1]==1) {
        var month="January"
    }
    else if (array[1]==2) {
        var month="February"
    }
    else if (array[1]==3) {
        var month="March"
    }
    else if (array[1]==4) {
        var month="April"
    }
    else if (array[1]==5) {
        var month="May"
    }
    else if (array[1]==6) {
        var month="June"
    }
    else if (array[1]==7) {
        var month="July"
    }
    else if (array[1]==8) {
        var month="August"
    }
    else if (array[1]==9) {
        var month="September"
    }
    else if (array[1]==10) {
        var month="October"
    }
    else if (array[1]==11) {
        var month="November"
    }
    else {
        var month="December"
    }
    return `${array[2]} ${month} ${array[0]}`
}

function print_page(){
    var button =document.getElementById('print_pdf');
    button.remove();
    window.print();
    location.reload();
}
