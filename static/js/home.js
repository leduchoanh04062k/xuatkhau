function openTuVanForm(workId) {
	$("#tuvanForm input[name='work_id']").val(workId);
	$("#tuvanModal").show();
}
function openTuVanFormNTD() {
    $("#popupModalTuVan").modal('show');
}

function closeTuVanFormNTD() {
    $("#popupModalTuVan").modal('hide');
}
$(document).ready(function(){
	$("#tuvanForm").submit(function(event){
		event.preventDefault();
		var phone = $("input[name='phone']").val().trim();
		var name = $("input[name='name']").val().trim();
		var work_id = $("input[name='work_id']").val();  
		var phonePattern = /^(0\d{9})$/; 
		if (!phonePattern.test(phone)) {
			alert("Vui lòng nhập số điện thoại hợp lệ (10 chữ số, bắt đầu bằng 0).");
			return;
		}
		var formData = {
			"name": name,
			"phone": phone,
			"work_id": work_id
		};
		$.ajax({
			type: "POST",
			url: "/ajaxAdvisory", 
			data: formData,
			headers: { "X-CSRFToken": "{{ csrf_token }}" },
			success: function(response) {
				if (response.status == "OK") {
					$(".datafrom").hide();
					$(".datafrom2").css("display", "block"); 

					setTimeout(function(){
						$("#popupModalTuVan").modal("hide"); 
						$(".datafrom2").hide();
						$(".datafrom").fadeIn();
						$("#tuvanForm")[0].reset();
					}, 2000);
				} else {
					alert("Lỗi: " + response.message);
				}
			},
			error: function(xhr, status, error) {
				alert("Có lỗi xảy ra, vui lòng thử lại!");
			}
		});
	});
});

