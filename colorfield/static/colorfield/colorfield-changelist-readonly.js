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

    function renderColorPreview(element, choices = []) {
        // change only elements with text content only
        if (element.children.length > 0) {
            return;
        }

        const color = getColor(element.textContent, choices);
        if (!color) {
            return;
        }

        const container = document.createElement('div');
        container.className = 'clr-field-readonly';

        const preview = document.createElement('span');
        preview.className = 'clr-field-readonly__preview';
        preview.style.backgroundColor = color;
        container.append(preview);

        const value = document.createElement('span');
        value.className = 'clr-field-readonly__value';
        value.textContent = element.textContent;
        container.append(value);

        element.textContent = '';
        element.prepend(container);
    }

    const script = document.querySelector("script[id='colorfield-list-of-fields']");
    const fields = JSON.parse(script?.textContent ?? '[]');

    for (const value of fields) {
        const [field, choices] = Array.isArray(value) ? value : [value];

        // change-list fields
        const listElements = document.querySelectorAll(`td.field-${field}`);
        for (const element of listElements) {
            renderColorPreview(element, choices);
        }

        // change-form fields
        const formElements = document.querySelectorAll(`div.field-${field} div.readonly`);
        for (const element of formElements) {
            renderColorPreview(element, choices);
        }
    }
});
