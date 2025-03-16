document.addEventListener("DOMContentLoaded", function () {
	const form = document.querySelector("#updateFormNTD");
	const messageContainer = document.querySelector("#my_custom_alert");
	const previewImage = document.querySelector("#previewImage");
	const anhBiaInput = document.querySelector("#anhBiaInput");
	form.addEventListener("submit", function (event) {
		event.preventDefault(); 
		let formData = new FormData(form); 

		fetch(form.action, {
			method: "POST",
			body: formData,
			headers: {
				"X-Requested-With": "XMLHttpRequest",
				"X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
			},
		})
		.then(response => response.json()) 
		.then(data => {
			if (data.success) {
				showMessage("Cập nhật thành công!", "greenbg");
				if (!anhBiaInput.files.length && previewImage.src) {
					previewImage.style.display = "block";
				}
				setTimeout(() => {
					location.reload();
				}, 3000);
			} else {
				showMessage("Có lỗi xảy ra! Vui lòng kiểm tra lại.", "redbg");
			}
		})
		.catch(error => {
			console.error("Lỗi:", error);
			showMessage("Lỗi kết nối! Hãy thử lại sau.", "redbg");
		});
	});
	function showMessage(message, bgClass) {
		messageContainer.innerHTML = `<div class="${bgClass}" onclick="$(this).fadeOut();">${message}</div>`;
		$(messageContainer).fadeIn();
		setTimeout(() => {
			$(messageContainer).fadeOut(); 
		}, 2500);
	}
});
document.addEventListener("DOMContentLoaded", function () {
	const fileInput = document.getElementById("file-input-media");
	const avatarImg = document.getElementById("avatar-img");
	const chooseBtn = document.getElementById("choose-avatar");
	fileInput.addEventListener("change", function (event) {
		const file = event.target.files[0];
		if (file) {
			const reader = new FileReader();
			reader.onload = function (e) {
				avatarImg.src = e.target.result;
			};
			reader.readAsDataURL(file);
		}
	});
});

ClassicEditor
.create(document.querySelector('#editor'))
.then(editor => {
	window.editor = editor;
	console.log('CKEditor init');
	const initialData = document.querySelector('#editor').value;
	editor.setData(initialData);  
})
.catch(error => {
	console.error(error);
});


document.getElementById("anhBiaInput").addEventListener("change", function(event) {
	const file = event.target.files[0];
	if (file) {
		const reader = new FileReader();
		reader.onload = function(e) {
			const previewImage = document.getElementById("previewImage");
			previewImage.src = e.target.result; 
			previewImage.style.display = "block"; 
		};
		reader.readAsDataURL(file); 
	}
});