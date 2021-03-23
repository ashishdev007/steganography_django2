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

function applyChange(input) {
  var label = input.nextElementSibling;
  let labelVal = label.innerHTML;

  input.addEventListener('change', function (e) {
    var fileName = '';

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
}
