document.addEventListener("DOMContentLoaded", function () {
    // ====================== MENU DROPDOWN ======================
    const menuItems = document.querySelectorAll(".has-sub-menu > a");
    menuItems.forEach((item) => {
        item.addEventListener("click", function (event) {
            event.preventDefault();
            let parentLi = this.closest("li");
            let subMenu = parentLi.querySelector(".sub-menu");
            let iconPlus = this.querySelector(".fa-plus");
            let iconMinus = this.querySelector(".fa-minus");

            if (subMenu) {
                if (subMenu.style.display === "block") {
                    subMenu.style.display = "none";
                    parentLi.classList.remove("current-dropdown");
                    if (iconPlus && iconMinus) {
                        iconPlus.style.display = "inline-block";
                        iconMinus.style.display = "none";
                    }
                } else {
                    document.querySelectorAll(".has-sub-menu .sub-menu").forEach((menu) => {
                        menu.style.display = "none";
                    });

                    document.querySelectorAll(".has-sub-menu").forEach((li) => {
                        li.classList.remove("current-dropdown");
                        let plusIcon = li.querySelector(".fa-plus");
                        let minusIcon = li.querySelector(".fa-minus");
                        if (plusIcon && minusIcon) {
                            plusIcon.style.display = "inline-block";
                            minusIcon.style.display = "none";
                        }
                    });

                    subMenu.style.display = "block";
                    parentLi.classList.add("current-dropdown");
                    if (iconPlus && iconMinus) {
                        iconPlus.style.display = "none";
                        iconMinus.style.display = "inline-block";
                    }
                }
            }
        });
    });

    // ====================== MODAL ĐĂNG NHẬP / ĐĂNG KÝ ======================
    const modalElement = document.getElementById("popupModal");
    if (modalElement) {
        const modal = new bootstrap.Modal(modalElement);
        const modalTitle = document.getElementById("popupModalLabel");

        const loginForm = document.getElementById("loginform");
        const resetPassForm = document.getElementById("resetPassForm");
        const registerForm = document.getElementById("registerform");
        const registerStepTab = document.querySelector(".register-step-tab");

        function hideAllForms() {
            loginForm.style.display = "none";
            resetPassForm.style.display = "none";
            registerForm.style.display = "none";
            registerStepTab.style.display = "none";
        }

        hideAllForms();
        loginForm.style.display = "block";

        document.querySelectorAll("[data-modal-title]").forEach((button) => {
            button.addEventListener("click", function () {
                const title = this.getAttribute("data-modal-title");
                modalTitle.innerText = title;
                hideAllForms();

                if (title.includes("Khởi tạo lại mật khẩu")) {
                    resetPassForm.style.display = "block";
                } else if (title.includes("Đăng ký mở tài khoản")) {
                    registerStepTab.style.display = "block";
                } else if (title.includes("Tôi là Ứng viên tìm việc") || title.includes("Tôi là Nhà tuyển dụng")) {
                    registerForm.style.display = "block";
                } else {
                    loginForm.style.display = "block";
                }

                modal.show();
            });
        });

        document.querySelectorAll(".bluecolor").forEach((button) => {
            button.addEventListener("click", function () {
                modalTitle.innerText = "Ứng viên đăng nhập";
                hideAllForms();
                loginForm.style.display = "block";
                modal.show();
            });
        });
    }

    // ====================== MODAL TƯ VẤN ======================
    const tuVanModalElement = document.getElementById("popupModalTuVan");
    if (tuVanModalElement) {
        const tuVanModal = new bootstrap.Modal(tuVanModalElement);
        document.querySelectorAll(".products-list-more").forEach((button) => {
            button.addEventListener("click", function () {
                tuVanModal.show();
            });
        });
    }
});
