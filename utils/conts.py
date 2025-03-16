class Conts():
	ROLE_CHOICES = (
		('admin', "Admin"),
		('applicant', "Ứng viên"),
		('employer', "Nhà tuyển dụng"),
	)

	MENH_GIA =(
		('Triệu', 'Triệu'),
		('Yên', 'Yên'),
		('Man', 'Man'),
		('Đài Tệ', 'Đài Tệ'),
		('Usd', 'Usd'),
		('Euro', 'Euro'),
		('Đô Sing', 'Đô Sing'),
		('Aud', 'Aud'),
		('Bgn', 'Bgn'),
		('Cad', 'Cad'),
		('Cny', 'Cny'),
		('Bảng Anh', 'Bảng Anh'),
		('Hkd', 'Hkd'),
		('Huf', 'Huf'),
		('Myr', 'Myr'),
		('Nzd', 'Nzd'),
		('Pln', 'Pln'),
		('Leu', 'Leu'),
		('Rub', 'Rub'),
		('Sar', 'Sar'),
		('Won', 'Won')
	)

	LAM_THEM =(
		('Làm thêm nhiều', 'Làm thêm nhiều'),
		('Làm thêm 1 - 2 h/ngày', 'Làm thêm 1 - 2 h/ngày'),
		('Làm thêm 2 - 3 h/ngày', 'Làm thêm 2 - 3 h/ngày'),
		('Làm thêm 2 - 4 h/ngày', 'Làm thêm 2 - 4 h/ngày'),
		('Làm thêm 3 - 5 h/ngày', 'Làm thêm 3 - 5 h/ngày'),
		('Làm thêm 4 - 6 h/ngày', 'Làm thêm 4 - 6 h/ngày'),
		('Làm thêm trung bình', 'Làm thêm trung bình'),
		('Không có làm thêm', 'Không có làm thêm'),
	)

	HOP_DONG =(
		('Không giới hạn', 'Không giới hạn'),
		('01 năm', '01 năm'),
		('02 năm', '02 năm'),
		('03 năm', '03 năm'),
		('04 năm', '04 năm'),
		('05 năm', '05 năm'),
		('06 năm', '06 năm'),
		('07 năm', '07 năm'),
		('08 năm', '08 năm'),
		('09 năm', '09 năm'),
		('10 năm', '10 năm'),
		)


	TRINH_DO_HOC_VAN_CHOICES = (
		("Không", "Không"),
		("Tốt nghiệp cấp 2 trở lê", "Tốt nghiệp cấp 2 trở lên"),
		("Tốt nghiệp cấp 3 trở lên", "Tốt nghiệp cấp 3 trở lên"),
		("Bằng nghề trở lên", "Bằng nghề trở lên"),
		("Tốt nghiệp cao đẳng trở lên", "Tốt nghiệp cao đẳng trở lên"),
		("Tốt nghiệp đại học trở lên", "Tốt nghiệp đại học trở lên"),
	)


	CHUYEN_NGANH_CHOICES =  (
		('Không yêu cầu', 'Không yêu cầu'),
		('Các ngành kinh tế', 'Các ngành kinh tế'),
		('Các ngành nghề khác', 'Các ngành nghề khác'),
		('Các ngành về y dược', 'Các ngành về y dược'),
		('Cơ khí, cơ điện tử', 'Cơ khí, cơ điện tử'),
		('Công nghệ thông tin, phần mềm', 'Công nghệ thông tin, phần mềm'),
		('Dệt may', 'Dệt may'),
		('Điện tử, điện lạnh, tự động hóa', 'Điện tử, điện lạnh, tự động hóa'),
		('Nhà hàng, khách sạn, du lịch', 'Nhà hàng, khách sạn, du lịch'),
		('Nông nghiệp, lâm nghiệp, chăn nuôi, thú y', 'Nông nghiệp, lâm nghiệp, chăn nuôi, thú y'),
		('Sinh học, thực phẩm, thủy sản', 'Sinh học, thực phẩm, thủy sản'),
		('Viễn thông, truyền thông', 'Viễn thông, truyền thông'),
		('Xây dựng, kiến trúc, địa chất', 'Xây dựng, kiến trúc, địa chất')
	)

	NGOAI_NGU_CHOICES = (
		('Không', 'Không'),
		('Tiếng Nhật', 'Tiếng Nhật'),
		('Tiếng Trung', 'Tiếng Trung'),
		('Tiếng Anh', 'Tiếng Anh'),
		('Tiếng Hàn', 'Tiếng Hàn'),
		('Ngoại ngữ khác', 'Ngoại ngữ khác'),
	)


	YEU_CAU_HOC_TIENG_CHOICES = (
		('Không yêu cầu', 'Không yêu cầu'),
		('01 tháng', '01 tháng'),
		('02 tháng', '02 tháng'),
		('03 tháng', '03 tháng'),
		('04 tháng', '04 tháng'),
		('05 tháng', '05 tháng'),
		('06 tháng', '06 tháng'),
	)


	TINH_TRANG_SUC_KHOE_CHOICES = (
		('Không yêu cầu', 'Không yêu cầu'),
		('Tốt', 'Tốt'),
	)


	THI_LUC_CHOICES = (
		('Tốt', 'Tốt'),
		('Nhận cận thị', 'Nhận cận thị'),
		('Không nhận cận thị', 'Không nhận cận thị'),
	)

	VIEM_GAN_B_CHOICES = (
		('Không yêu cầu', 'Không yêu cầu'),
		('Nhận VGB', 'Nhận VGB'),
		('Không nhận VGB', 'Không nhận VGB'),
	)

	XAM_HINH_CHOICES = (
		('Không yêu cầu', 'Không yêu cầu'),
		('Có nhận', 'Có nhận'),
		('Không nhận', 'Không nhận'),
	)

	GIOI_TINH_CHOICES = (
		('', 'Vui lòng chọn'),
		('Nam', 'Nam'),
		('Nữ', 'Nữ'),
	)

	XAM_CHOICES = (
		('Không', 'Không'),
		('Có', 'Có'),
	)			
	
