window.addEventListener('load', function () {
  const inputs = document.getElementsByClassName('colorfield_field coloris');
  for (const input of inputs) {
    const id = input.getAttribute('id');
    const options = JSON.parse(decodeURIComponent(input.getAttribute('data-coloris')));
    Coloris.setInstance(`.colorfield_field.coloris.${id}`, options);
  }
});
