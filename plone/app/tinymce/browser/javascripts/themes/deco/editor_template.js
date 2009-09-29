/**
 * This is a theme used for Deco
 *
 * @author              Rob Gietema
 * @version             0.1
 */
;(function() {
    var DOM = tinymce.DOM;

    tinymce.create('tinymce.themes.PloneTheme', {
        init : function(ed, url) {
            var t = this, s = ed.settings;
            t.editor = ed;
        },

        renderUI : function(o) {
            return {
                deltaHeight : 0
            };
        },

        getInfo : function() {
            return {
                longname : 'Deco theme',
                author : 'Four Digits',
                authorurl : 'http://www.fourdigits.nl',
                version : tinymce.majorVersion + "." + tinymce.minorVersion
            }
        }
    });

    tinymce.ThemeManager.add('deco', tinymce.themes.PloneTheme);
})();
