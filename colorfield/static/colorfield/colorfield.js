/** global: django */

if (typeof(django) !== 'undefined' && typeof(django.jQuery) !== 'undefined') {
    (function($) {
        // add colopicker to inlines added dynamically
        $(document).on('formset:added', function onFormsetAdded(event, row) {
            $(row['0']).find('.colorfield_field.jscolor').not('.jscolor-active').each(function(index, el) {
                var picker = new jscolor($(el).get(0));
            });
        });
    }(django.jQuery));
}
