const SignUpButton = document.getElementById('signUp');
const SignInButton = document.getElementById('signIn');
const container = document.getElementById('container');

SignUpButton.addEventListener('click', () => container.classList.add('right-panel-active'));

SignInButton.addEventListener('click', () => container.classList.remove('right-panel-active'));

// Code Summary: Used .addEventListener to add a new class to container class in HTML anytime that the sign up button is clicked.
// The rest of the animations were done by selecting the new class added by Javascript in styles.css and then used the transform property to add the ease in and out swipe animations. -Vincent Ogbu