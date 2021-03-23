var inputs = document.querySelectorAll('.inputfile');
var statusId = null;

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

const handleSubmit = async (event) => {
  event.preventDefault();

  let image = event.target.elements.image.files[0];

  console.log('Here ' + image);

  //   await new Promise((r) => setTimeout(r, 20000));

  fetch('http://127.0.0.1:8000/status/')
    .then((res) => res.json())
    .then((data) => {
      statusId = data['id'];
      sendForDecoding(statusId, image);
    });
};

function sendForDecoding(statusId, image) {
  let data = new FormData();
  data.append('image', image);
  switchDisplays('first', 'second');
  move(statusId);

  fetch(`http://127.0.0.1:8000/decode/${statusId}`, {
    method: 'POST',
    body: data,
  })
    .then((res) => res.blob())
    .then((blob) => {
      window.open(URL.createObjectURL(blob));
    });
}

document.querySelector('form').addEventListener('submit', handleSubmit);

function switchDisplays(hide, show) {
  let forHiding = document.querySelectorAll(`.${hide}`);
  forHiding.forEach((element) => {
    element.style.display = 'none';
  });

  let forShow = document.querySelectorAll(`.${show}`);

  forShow.forEach((element) => {
    element.setAttribute('style', 'display: block !important;');
  });
}
