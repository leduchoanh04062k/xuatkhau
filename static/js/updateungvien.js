document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("#update-form");
    const messageContainer = document.querySelector("#my_custom_alert");
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
