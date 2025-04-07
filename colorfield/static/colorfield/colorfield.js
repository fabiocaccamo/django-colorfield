window.addEventListener('load', function () {
  const inputs = document.getElementsByClassName('colorfield_field coloris');
  for (const input of inputs) {
    try {
      const id = input.getAttribute('id');
      // convert python dict into json object
      const options = input.getAttribute('data-coloris')
        .replaceAll("'", '"')
        .replaceAll('True', 'true')
        .replaceAll("False", 'false');
      Coloris.setInstance(`.colorfield_field.coloris.${id}`, JSON.parse(options));
    } catch (_ignore) {
      console.debug('cannot read data-coloris attribute in input', id);
    }
  }
});
