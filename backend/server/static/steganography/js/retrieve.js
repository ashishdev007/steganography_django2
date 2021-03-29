var inputs = document.querySelectorAll('.inputfile');
var statusId = null;

inputs.forEach((input) => {
  input.addEventListener('change', fileUpload);
});

var nextBtn = document.getElementById('nextBtn');

const handleSubmit = async (event) => {
  event.preventDefault();

  let image = event.target.elements.image.files[0];

  fetch(window.location.origin + '/status/')
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
  document.getElementById('progressHeader').innerHTML =
    'Retrieving the Message...';

  fetch(window.location.origin + `/decode/${statusId}`, {
    method: 'POST',
    body: data,
  })
    .then((res) => res.blob())
    .then((blob) => {
      window.open(URL.createObjectURL(blob));
    });
}

document.querySelector('form').addEventListener('submit', handleSubmit);
