$(".register-step-tab button").click(function () {
	let role = $(this).data("modal-title").includes("Ứng viên") ? "applicant" : "employer";
	$("#role").val(role);
});

function getCSRFToken() {
	let cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		let cookies = document.cookie.split(";");
		for (let i = 0; i < cookies.length; i++) {
			let cookie = cookies[i].trim();
			if (cookie.startsWith("csrftoken=")) {
				cookieValue = decodeURIComponent(cookie.substring("csrftoken=".length));
				break;
			}
		}
	}
	return cookieValue;
}
$(document).ready(function () {
	$("#registerform").submit(function (e) {
		e.preventDefault();
		$.ajax({
			type: "POST",
			url: "/register",
			data: $(this).serialize(),
			success: function (response) {
				if (response.success) {
					$("#my_custom_alert").html(
						`<div class="greenbg" onclick="$(this).fadeOut();">${response.message}</div>`
						).fadeIn();

					setTimeout(() => {
						$("#my_custom_alert").fadeOut();
					}, 3000);
				} else {
					$("#my_custom_alert").html(
						`<div class="redbg" onclick="$(this).fadeOut();">${response.message}</div>`
						).fadeIn();
				}
				if (response.success) {
					if (response.showLoginForm) {
						$("#registerform")[0].reset();
						$("#registerform").hide();
						$("#loginform").show();
					} else if (response.showOtpForm) {
						$("#registerform").hide();
						$("#otpform").show();

						$("#otpform .otp_display").html(
							`<div class="alert alert-info">Mã OTP của bạn: 
							<strong id="otp_code">${response.otp_code}</strong> 
							<button onclick="copyOtp()" class="btn btn-sm btn-primary">Copy</button></div>`
							).fadeIn();
					}
				}
			}
		});
	});

	$("#verifyOtp").click(function (e) {
		e.preventDefault();
		$.ajax({
			type: "POST",
			url: "/verify-otp",
			data: { otp: $("#otp").val(), username: $("#user_name").val(), csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val() },
			success: function (response) {
				if (response.success) {
					$("#my_custom_alert").html(
						`<div class="greenbg" onclick="$(this).fadeOut();">${response.message}</div>`
						).fadeIn();

					setTimeout(() => {
						$("#my_custom_alert").fadeOut();
					}, 3000);
				} else {
					$("#my_custom_alert").html(
						`<div class="redbg" onclick="$(this).fadeOut();">${response.message}</div>`
						).fadeIn();
				}
				if (response.success) {
					$("#otpform").hide();
					$("#loginform").show();
				}
			}
		});
	});



	$("#resetPassForm button.btn-success").click(function (e) {
		e.preventDefault();
		$.ajax({
			type: "POST",
			url: "/send_otp_reset_password",
			data: $("#resetPassForm").serialize(),
			success: function (response) {
				$("#my_custom_alert").html(
					`<div class="${response.success ? 'greenbg' : 'redbg'}" onclick="$(this).fadeOut();">${response.message}</div>`
					).fadeIn();

				if (response.success) {
					$("#resetPassForm").hide();
					$("#verifyform").show();
					$("#verifyform .otp_display").html(
						`<div class="alert alert-info">Mã OTP của bạn: 
						<strong id="otp_code">${response.otp_code}</strong> 
						<button onclick="copyOtp()" class="btn btn-sm btn-primary">Copy</button></div>`
						).fadeIn();
				}
			}
		});
	});

	$("#verifyform").submit(function (e) {
		e.preventDefault();
		$.ajax({
			type: "POST",
			url: "/verify_otp_reset_password",
			data: $(this).serialize(),
			success: function (response) {
				$("#my_custom_alert").html(
					`<div class="${response.success ? 'greenbg' : 'redbg'}" onclick="$(this).fadeOut();">${response.message}</div>`
					).fadeIn();

				if (response.success) {
					$("#verifyform")[0].reset();
					$("#verifyform").hide();
					$("#loginform").show();
				}
			}
		});
	});

	$("#updateForm").submit(function (event) {
	event.preventDefault();

	let formData = {
		ho_va_ten_dem: $("#data_full_name").val(),
		gioi_tinh: $("#popup_data_gioi_tinh").val(),
		nam_sinh: $("#popup_data_nam_sinh").val(),
		tinh_thanh_pho: $("#poup_data_province_id").val(),
		countries: $("#poup_data_company_country_ids").val() || [],
		professions: $("#popup_data_nganh_nghe").val() || []
	};

	$.ajax({
		url: "/update_user_info",
		type: "POST",
		data: JSON.stringify(formData),
		contentType: "application/json",
		headers: {
			"X-CSRFToken": getCSRFToken()
		},
		success: function (response) {
			$("#my_custom_alert1").html(
				`<div class="${response.success ? 'greenbg' : 'redbg'}" onclick="$(this).fadeOut();">${response.message}</div>`
			).fadeIn();

			if (response.success) {
				setTimeout(() => {
					let modalElement = document.getElementById("updateModal");
					let modalInstance = bootstrap.Modal.getInstance(modalElement);
					modalInstance.hide();
					setTimeout(() => {
						location.reload();
					}, 500);
				}, 3000);
			}
		},
		error: function () {
			alert("Có lỗi xảy ra khi cập nhật thông tin.");
		}
	});
});


});
function copyOtp() {
	var otpText = document.getElementById("otp_code").innerText;
	navigator.clipboard.writeText(otpText).then(() => {
		alert("Đã sao chép mã OTP!");
	});
}


document.querySelectorAll(".logoutBtn").forEach(button => {
	button.addEventListener("click", function (e) {
        e.preventDefault();
        let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]')?.value ||
        document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];

        fetch("/logout_view", { 
        	method: "POST",
        	headers: {
        		"X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": csrftoken
            },
        })
        .then(response => {
        	if (!response.ok) {
        		throw new Error(`HTTP error! Status: ${response.status}`);
        	}
        	return response.json();
        })
        .then(data => {
        	if (data.success) {
        		alert(data.message);
        		window.location.href = "/";  
        	} else {
        		alert("Lỗi khi đăng xuất!");
        	}
        })
        .catch(error => {
        	console.error("Lỗi đăng xuất:", error);
        	alert("Có lỗi xảy ra khi đăng xuất. Vui lòng thử lại!");
        });
    });
});


