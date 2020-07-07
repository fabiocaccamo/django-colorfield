/** global: django */

window.addEventListener('load', function(event) {
    if (typeof(django) !== 'undefined' && typeof(django.jQuery) !== 'undefined') {
        (function($) {
            // add colopicker to inlines added dynamically
            $(document).on('formset:added', function onFormsetAdded(event, row) {
                jscolor.installByClassName('jscolor');
            });
        })(django.jQuery);
    }
});
