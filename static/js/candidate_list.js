document.querySelectorAll('select').forEach(function(select) {
	select.addEventListener('change', function() {
		let url = new URL(window.location.href);
		document.querySelectorAll('select').forEach(function(select) {
			const name = select.name;
			const value = select.value;
			if (value) {
				url.searchParams.set(name, value);
			} else {
				url.searchParams.set(name, '');
			}
		});
		window.location.href = url.toString();
	});
});
window.addEventListener('DOMContentLoaded', function() {
	const urlParams = new URLSearchParams(window.location.search);
	document.querySelectorAll('select').forEach(function(select) {
		const paramValue = urlParams.get(select.name);
		if (paramValue) {
			select.value = paramValue;
		}
	});
});