function print_page(){
    var button =document.getElementById('print_pdf');
    button.remove();
    window.print();
    location.reload();
}