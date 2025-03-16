document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("file-input-media");
    const previewLabel = document.getElementById("click-chose-media");
    fileInput.addEventListener("change", function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                previewLabel.style.backgroundImage = `url(${e.target.result})`;
                previewLabel.style.backgroundSize = "cover";
                previewLabel.style.backgroundPosition = "center";
                previewLabel.style.height = "150px";
                previewLabel.style.border = "1px solid #ccc";
                previewLabel.style.display = "block";
            };

            reader.readAsDataURL(file);
        }
    });
});
$(document).ready(function () {
    document.querySelectorAll("#editor, #id_cong_viec_cu_the, #id_quyen_loi_khac, #id_chuong_trinh_ho_tro, #id_yeu_cau_khac").forEach((element) => {
    ClassicEditor.create(element)
        .then((editor) => {
            console.log("CKEditor init", element.id);
            const initialData = element.value;
            editor.setData(initialData);
        })
        .catch((error) => {
            console.error(error);
        });
});

  
    function calculateBirthYear(age) {
        let currentYear = new Date().getFullYear();
        return currentYear - age;
    }

    $("#nam_sinh").on("input", function () {
        let age = $(this).val();
        if ($.isNumeric(age) && age > 0) {
            let birthYear = calculateBirthYear(age);
            $("#nam_sinh_tu_dong").val(birthYear);
        } else {
            $("#nam_sinh_tu_dong").val("");
        }
    });

    $("#ket_thuc_nam_sinh").on("input", function () {
        let age = $(this).val();
        if ($.isNumeric(age) && age > 0) {
            let birthYear = calculateBirthYear(age);
            $("#nam_sinh_ket_thuc_nam_sinh").val(birthYear);
        } else {
            $("#nam_sinh_ket_thuc_nam_sinh").val("");
        }
    });

    var picker = new Pikaday({
        field: document.getElementById("depart"),
        format: "DD-MM-YYYY",
        toString(date) {
            return moment(date).format("DD-MM-YYYY");
        },
        onSelect: function () {
            let d = this.getDate();
        },
    });

    var picker2 = new Pikaday({
        field: document.getElementById("retur"),
        format: "DD-MM-YYYY",
        toString(date) {
            return moment(date).format("DD-MM-YYYY");
        },
        onSelect: function () {
            let d = this.getDate();
        },
    });

    $(
        "#country, #province, #id_luong_co_ban_menh_gia, #id_lam_them,#id_thu_nhap_du_kien_menh_gia,#id_hop_dong,#id_phi_xuat_canh_menh_gia,#id_trinh_do_hoc_van,#id_chuyen_nganh,#id_ngoai_ngu,#id_yeu_cau_hoc_tieng,#id_tinh_trang_suc_khoe,#id_thi_luc,#id_viem_gan_b,#id_xam_hinh,#du_kien_xuat_canh"
        ).select2();
    function loadProvinces(country_id) {
        if (country_id !== "") {
            $.ajax({
                url: "/getProvinces",
                type: "GET",
                data: { country_id: country_id },
                dataType: "json",
                success: function (response) {
                    $("#province").empty().append('<option value="">Toàn quốc</option>');
                    $.each(response, function (key, value) {
                        $("#province").append('<option value="' + key + '">' + value + "</option>");
                    });
                },
            });
        } else {
            $("#province").empty().append('<option value="">Toàn quốc</option>');
        }
    }
    $("#country").change(function () {
        var country_id = $(this).val();
        loadProvinces(country_id);
    });
    var initial_country = $("#country").val();
    if (initial_country) {
        loadProvinces(initial_country);
    }

    $("#postJobForm").on("submit", function (e) {
        e.preventDefault();
        let formData = new FormData(this);

        $.ajax({
            url: "/employers/add_job",
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                if (response.success) {
                    showMessage("Đăng tin thành công!", "success", 2000);
                    setTimeout(function () {
                        window.location.href = response.redirect_url;
                    }, 2000); 
                } else {
                    showMessage(response.message, "danger", 3000);
                }
            },
            error: function () {
                showMessage("Có lỗi xảy ra. Vui lòng thử lại!", "danger", 3000);
            },
        });
    });

    function showMessage(message, type, duration = 3000) {
        let bgColor = type === "success" ? "greenbg" : type === "info" ? "bluebg" : "redbg";

        $("#my_custom_alert").html(`<div class="${bgColor}" onclick="$(this).fadeOut();">${message}</div>`).fadeIn();

        setTimeout(function () {
            $("#my_custom_alert").fadeOut();
        }, duration);
    }

    $("#id_is_confirmed").on("change", function () {
        if ($(this).is(":checked")) {
            alert("Tôi cam kết những thông tin trên là đúng sự thật và tôi hoàn toàn chịu trách nhiệm về những nội dung mình đăng tải.");
        }
    });
});
