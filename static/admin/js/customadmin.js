jQuery(document).ready(function($) {
    var getUrlParameter = function getUrlParameter(sParam) {
        var sPageURL = window.location.search.substring(1),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;
        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
            }
        }
        return false;
    };
    var url = $(location).attr('href');
    url = getUrlParameter('_changelist_filters');
    if (url){
        url =url.split("=");
        var id = url[1];
        $("#id_cake").val(id).change();
    }
    
});