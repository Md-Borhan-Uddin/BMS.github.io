


const loanbtn = document.getElementById('loan');
const withdrawbtn = document.getElementById('withdraw');
const depositbtn = document.getElementById('deposit');
const form = document.getElementById('form');
const submitbtn = document.getElementById('submitBtn');

const data  = document.currentScript.dataset

loanbtn.addEventListener('click',()=>{
form.setAttribute('action',`${data.url}?type=Loan`)
submitbtn.innerText = 'Request Loan'
})