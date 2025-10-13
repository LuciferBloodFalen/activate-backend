// Landing page: show profile preview when a user object is present in localStorage
// NOTE: Password verification and auth flows must be handled by the backend only.
document.addEventListener('DOMContentLoaded',()=>{
  const guestActions = document.getElementById('guestActions');
  const profileCard = document.getElementById('profileCard');
  const avatar = document.getElementById('avatar');
  const profileName = document.getElementById('profileName');
  const profileEmail = document.getElementById('profileEmail');
  const memberSince = document.getElementById('memberSince');
  const logoutBtn = document.getElementById('logout');

  // Demo helper: visit ?demo=1 to populate a fake user for preview only
  const urlParams = new URLSearchParams(window.location.search);
  if(urlParams.get('demo') === '1'){
    const demoUser = {username:'johndoe',email:'john@example.com',created:'2023-08-01'};
    localStorage.setItem('activate_user_demo', JSON.stringify(demoUser));
  }

  // Check for a demo user object in localStorage (key: activate_user_demo)
  const raw = localStorage.getItem('activate_user_demo');
  if(raw){
    try{
      const user = JSON.parse(raw);
      showProfile(user);
    }catch(e){
      console.warn('Invalid user object in localStorage');
    }
  }

  function showProfile(user){
    guestActions.style.display = 'none';
    profileCard.style.display = 'flex';
    const initial = (user.username && user.username[0]) || (user.email && user.email[0]) || 'A';
    avatar.textContent = initial.toUpperCase();
    profileName.textContent = user.username || 'User';
    profileEmail.textContent = user.email || '';
    memberSince.textContent = user.created || '—';
    document.getElementById('goToAccount').setAttribute('href','../login/index.html');
  }

  logoutBtn.addEventListener('click', ()=>{
    // For demo purposes, clear the demo user only.
    localStorage.removeItem('activate_user_demo');
    profileCard.style.display = 'none';
    guestActions.style.display = 'flex';
  });
});
