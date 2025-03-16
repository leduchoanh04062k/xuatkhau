document.addEventListener("DOMContentLoaded", function () {
		document.querySelectorAll(".delete-job-btn").forEach(button => {
			button.addEventListener("click", function () {
				if (!confirm("Bạn có chắc chắn muốn xóa tin này?")) {
					return;
				}

				let jobId = this.getAttribute("data-job-id");

				fetch(`/employers/remove_job/${jobId}`, {
					method: "POST",
					headers: {
						"X-CSRFToken": getCookie("csrftoken"), 
						"Content-Type": "application/json"
					},
				})
				.then(response => response.json())
				.then(data => {
					if (data.success) {
						alert("Xóa tin thành công!");
						location.reload();
					} else {
						alert(data.message);
					}
				})
				.catch(error => {
					console.error("Lỗi:", error);
					alert("Có lỗi xảy ra, vui lòng thử lại.");
				});
			});
		});

		
		document.querySelectorAll(".up-job-btn").forEach(button => {
			button.addEventListener("click", function () {
				let jobId = this.getAttribute("data-job-id");
				fetch(`/employers/up_tin/?id=${jobId}`, {
					method: "GET",
					headers: {
						"X-CSRFToken": getCookie("csrftoken"),
					},
				})
				.then(response => response.json())
				.then(data => {
					if (data.success) {
						alert("Up tin thành công!");
						location.reload();
					} else {
						alert(data.message);
						if (data.redirect_url) {
							window.location.href = data.redirect_url;
						}
					}
				})
				.catch(error => {
					console.error("Lỗi:", error);
					alert("Có lỗi xảy ra, vui lòng thử lại.");
				});
			});
		});


		document.querySelectorAll(".hot-job-btn").forEach(button => {
			button.addEventListener("click", function () {
				let jobId = this.getAttribute("data-job-id");

				fetch(`/employers/set_hot_tin?id=${jobId}`, {  
					method: "GET",
					headers: {
						"X-CSRFToken": getCookie("csrftoken"),
					},
				})
				.then(response => response.json())
				.then(data => {
					if (data.success) {
						alert("Tin đã được nâng thành HOT!");
						location.reload();
					} else {
						alert(data.message);
						if (data.redirect_url) {
							window.location.href = data.redirect_url;
						}
					}
				})
				.catch(error => {
					console.error("Lỗi:", error);
					alert("Có lỗi xảy ra, vui lòng thử lại.");
				});
			});
		});
		function getCookie(name) {
			let cookieValue = null;
			if (document.cookie && document.cookie !== "") {
				document.cookie.split(";").forEach(cookie => {
					let trimmedCookie = cookie.trim();
					if (trimmedCookie.startsWith(name + "=")) {
						cookieValue = decodeURIComponent(trimmedCookie.substring(name.length + 1));
					}
				});
			}
			return cookieValue;
		}
	});
