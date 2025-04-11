/*
 * Use onload method to avoid conflicts in production with Content-Security-Policy.
 */
function onLoad () {
  const inputs = document.getElementsByClassName('colorfield_field coloris');
  for (const input of inputs) {
    try {
      const id = input.getAttribute('id');
      // convert pseudo-json into real json object
      const options = input.getAttribute('data-coloris').replaceAll("'", '"');
      Coloris.setInstance(`.colorfield_field.coloris.${id}`, JSON.parse(options));
    } catch (_ignore) {
      console.debug('cannot read data-coloris attribute in input', id)
    }
  }
}

window.addEventListener('load', onLoad);
