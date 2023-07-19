let order = JSoN.parse(localStorage.getItem(order));
let total = localStorage.getItem('total');

if(order === null || order === undefined ) {
    localStorage.setItem('order', JSON.stringify([]));
    order = JSON.parse(localStorage.getItem('order'));
}

if(order === null || order === undefined ) {
    localStorage.setItem('total', 0);
    total = localStorage.getItem('total');
}

