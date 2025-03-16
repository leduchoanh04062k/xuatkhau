function getCSRFToken() {
	return document.querySelector('meta[name="csrf-token"]').getAttribute("content");
}

function before_view_uv_info() {
	var myModal = new bootstrap.Modal(document.getElementById('viewUVInfoModal'));
	myModal.show();
	return false; 
}
function action_view_uv_info(uv_id) {
	var myModal = bootstrap.Modal.getInstance(document.getElementById('viewUVInfoModal'));
	myModal.hide();

	$.ajax({
		url: "/employers/view_candidate",
		type: "POST",
		data: {
			uv_id: uv_id,
		},
		headers: {
            "X-CSRFToken": getCSRFToken()
        },
        success: function (response) {
        	if (response.success) {
        		$("#phone_" + uv_id).text(response.phone ? response.phone : "********");
        		$("#zalo_" + uv_id).text(response.zalo ? response.zalo : "********");
        		if (response.facebook) {
        			$("#facebook_" + uv_id).html('<a href="' + response.facebook + '" target="_blank">' + response.facebook + '</a>');
        		} else {
        			$("#facebook_" + uv_id).html(''); 
        		}

        	} else {
        		alert(response.message);
        	}
        },
        error: function () {
        	alert("Có lỗi xảy ra, vui lòng thử lại!");
        }
    });

	return false;
}

