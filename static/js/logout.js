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
