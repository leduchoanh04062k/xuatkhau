document.addEventListener("DOMContentLoaded", function () {
	document.getElementById("sendOtpBtn").addEventListener("click", function () {
		let phoneNumber = document.getElementById("username").value; 
		document.getElementById("username_hidden").value = phoneNumber; 
	});
});

document.getElementById("verifyform").addEventListener("submit", function (e) {
	let hiddenPhone = document.getElementById("username_hidden").value;
	if (!hiddenPhone) {
		e.preventDefault();
		alert("Lỗi! Không tìm thấy số điện thoại. Vui lòng thử lại.");
	}
});

window.onload = function () {
	document.getElementById("username_hidden").value = document.getElementById("username").value;
};


document.querySelector("#loginform").addEventListener("submit", function (e) {
	e.preventDefault();
	let formData = new FormData(this);

	fetch("/login_view", { 
		method: "POST",
		body: formData,
		headers: {
			"X-Requested-With": "XMLHttpRequest",
		},
	})
	.then(response => response.json())
	.then(data => {
		$("#my_custom_alert").html(
			`<div class="${data.success ? 'greenbg' : 'redbg'}" onclick="$(this).fadeOut();">${data.message}</div>`
			).fadeIn();
		if (data.success) {
			$("#loginform")[0].reset();
			setTimeout(() => {
				let loginModal = bootstrap.Modal.getInstance(document.getElementById("popupModal"));
				if (loginModal) {
					loginModal.hide();
				}
				$(".modal-backdrop").remove();
				$("body").removeClass("modal-open");
				if (data.show_update_modal) {
					let updateModalElement = document.getElementById("updateModal");
					let updateModal = new bootstrap.Modal(document.getElementById("updateModal"), { backdrop: 'static', keyboard: false });
					updateModal.show();
					updateModalElement.addEventListener("hidden.bs.modal", function () {
                        window.location.reload(); 
                    });
				} else {
					window.location.href = "/"; 
				}
			}, 1000);
		}
	})
	.catch(error => {
		console.error("Lỗi đăng nhập:", error);
		alert("Có lỗi xảy ra khi đăng nhập. Vui lòng thử lại!");
	});
});

document.addEventListener("DOMContentLoaded", function () {
	const roleInput = document.getElementById("role");
	const registerButton = document.getElementById("sendOtp");

	function updateButtonText() {
		if (roleInput.value === "applicant") {
			registerButton.innerText = "Đăng ký Ứng viên";
		} else if (roleInput.value === "employer") {
			registerButton.innerText = "Đăng ký Tuyển dụng";
		}
	}
	updateButtonText();
	document.querySelector('.btn-success[data-modal-title="Tôi là Ứng viên tìm việc"]').addEventListener("click", function () {
		roleInput.value = "applicant";
		updateButtonText();
	});
	document.querySelector('.btn-primary[data-modal-title="Tôi là Nhà tuyển dụng"]').addEventListener("click", function () {
		roleInput.value = "employer";
		updateButtonText();
	});
});

