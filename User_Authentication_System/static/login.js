document.addEventListener('DOMContentLoaded',()=>{
  const form = document.getElementById('loginForm');
  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const user = document.getElementById('user');
    const password = document.getElementById('password');
    let errors = [];
    if(!user.value.trim()) errors.push('Enter username or email');
    if(!password.value || password.value.length < 6) errors.push('Password must be at least 6 characters');
    if(errors.length){
      alert(errors.join('\n'));
      return;
    }
    // Not connected yet - just show a message
    alert('Form validated — not connected to backend yet.');
  });
});
