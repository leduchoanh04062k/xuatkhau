$(document).ready(function() {
    $("#poup_data_company_country_ids, #popup_data_nganh_nghe").select2({
        dropdownParent: $("#updateForm"),
        placeholder: "Chọn một hoặc nhiều mục",
        allowClear: true,
        width: '100%',
    });
});