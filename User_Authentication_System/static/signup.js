document.addEventListener('DOMContentLoaded',()=>{
  const form = document.getElementById('signupForm');
  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const confirm = document.getElementById('confirm');
    let errors = [];
    if(!username.value.trim()) errors.push('Enter a username');
    if(!email.value.trim() || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email.value)) errors.push('Enter a valid email');
    if(!password.value || password.value.length < 6) errors.push('Password must be at least 6 characters');
    if(password.value !== confirm.value) errors.push('Passwords do not match');
    if(errors.length){
      alert(errors.join('\n'));
      return;
    }
    // Not connected yet - just show a message
    alert('Signup validated — not connected to backend yet.');
  });
});
