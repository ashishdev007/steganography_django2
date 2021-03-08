var inputs = document.querySelectorAll('.inputfile');
console.log(inputs);

function fileUpload(e) {
  e.preventDefault();
  var label = e.target.nextElementSibling;
  let labelVal = label.innerHTML;
  var fileName = '';
  console.log(e);

  if (this.files && this.files.length > 1)
    fileName = (this.getAttribute('data-multiple-caption') || '').replace(
      '{count}',
      this.files.length
    );
  else fileName = e.target.value.split('\\').pop();

  if (fileName) {
    label.querySelector('span').innerHTML = fileName;
    nextBtn = document.querySelector('#nextBtn');
    nextBtn.style.display = 'block';
  } else label.innerHTML = labelVal;
}

inputs.forEach((input) => {
  input.addEventListener('change', fileUpload);
});

document.getElementById('test').addEventListener('change', fileUpload);

Array.prototype.forEach.call(inputs, function (input) {
  var label = input.nextElementSibling;
  let labelVal = label.innerHTML;

  input.addEventListener('change', function (e) {
    var fileName = '';
    console.log('Changing');

    if (this.files && this.files.length > 1)
      fileName = (this.getAttribute('data-multiple-caption') || '').replace(
        '{count}',
        this.files.length
      );
    else fileName = e.target.value.split('\\').pop();

    if (fileName) {
      label.querySelector('span').innerHTML = fileName;
      nextBtn = document.querySelector('#nextBtn');
      nextBtn.style.display = 'block';
    } else label.innerHTML = labelVal;
  });
});

var nextBtn = document.getElementById('nextBtn');

nextBtn.addEventListener('click', (event) => {
  event.preventDefault();
  switchDisplays();
});

function switchDisplays() {
  let firsts = document.querySelectorAll('.first');
  firsts.forEach((element) => {
    element.style.display = 'none';
  });

  let seconds = document.querySelectorAll('.second');

  seconds.forEach((element) => {
    element.setAttribute('style', 'display: block !important;');
  });
}

function onSubmit() {
  fetch('http://127.0.0.1:8000/encode/');
}
