function click2Copy(element) {
	let copyText = element.value;
	navigator.clipboard.writeText(copyText).then(() => {
		alert("Đã sao chép: " + copyText);
	}).catch(err => {
		console.error("Lỗi sao chép: ", err);
	});
}


