window.addEventListener('load', function () {
  function getColor(initialColor, choices = []) {
    let color = initialColor;
    if (color?.length && choices?.length) {
      // get color value from choices [(value, label)]
      color = choices.find(choice => choice[1] === color)?.[0];
    }
    // looks like color value
    return color?.length > 6 ? color : null;
  }

  function printColor(element, choices = []) {
    // change elements with only text content
    if (element.children.length > 0) return;

    const color = getColor(element.textContent, choices);
    if (!color) return;

    const box = document.createElement('div');
    box.className = 'clr-field-ro-box';
    box.style.background = color;

    const content = document.createElement('div');
    content.className = 'clr-field-ro-content';
    content.textContent = element.textContent;

    const div = document.createElement('div');
    div.className = 'clr-field-ro';
    div.append(box);
    div.append(content);

    element.textContent = '';
    element.prepend(div);
  }

  const script = document.querySelector("script[id='colorfield-list-of-fields']");
  const fields = JSON.parse(script.textContent);

  for (const value of fields) {
    const [field, choices] = Array.isArray(value) ? value : [value];
    // change-list fields
    const listElements = document.querySelectorAll(`td.field-${field}`);
    for (const element of listElements) {
      printColor(element, choices);
    }

    // change-form fields
    const formElements = document.querySelectorAll(`div.field-${field} div.readonly`);
    for (const element of formElements) {
      printColor(element, choices);
    }
  }
});
